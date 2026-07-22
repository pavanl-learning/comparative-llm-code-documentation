#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any

import torch
from datasets import Dataset
from peft import LoraConfig
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from trl import SFTConfig, SFTTrainer


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_no}: {exc}") from exc
    return rows


def normalize_doc(text: str) -> str:
    return " ".join(str(text or "").split()).strip()


def build_prompt(row: dict[str, Any]) -> str:
    """
    Build a zero-shot style training prompt aligned with your generation setup.
    If you already have row['prompt'], you could use it directly, but for SFT
    prompt-completion training it is better to keep the target separate.
    """
    instruction = (
        "Write a very short API-docstring-style description for the following function in plain text. "
        "Use exactly 1 sentence when possible, and never more than 2 short sentences. "
        "Start with the function's main purpose. "
        "Mention parameters or return value only if they are clearly inferable from the code and can be stated briefly. "
        "Use only information supported by the code. "
        "If details are unclear, keep the description general. "
        "Keep the wording brief, direct, and compact. "
        "Do not include markdown, code blocks, examples, headings, lists, implementation steps, or speculative details."
    )

    parts = [instruction, "", f"Language: {row['language']}"]

    func_name = str(row.get("resolved_func_name") or row.get("func_name") or "").strip()
    if func_name:
        parts.append(f"Function name: {func_name}")

    code = row.get("code", "")
    parts.extend([
        f"Code:\n{code}",
        "",
        "Documentation:",
    ])
    return "\n".join(parts)


def convert_to_prompt_completion(rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    converted: list[dict[str, str]] = []
    for row in rows:
        ref = normalize_doc(row.get("reference_documentation", ""))
        if not ref:
            continue

        converted.append({
            "prompt": build_prompt(row),
            "completion": ref,
        })
    return converted


def split_rows(
    rows: list[dict[str, str]],
    val_ratio: float,
    seed: int,
) -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    rows = rows[:]
    random.Random(seed).shuffle(rows)
    n_val = max(1, int(len(rows) * val_ratio)) if len(rows) > 1 else 0
    val_rows = rows[:n_val]
    train_rows = rows[n_val:]
    return train_rows, val_rows


def choose_target_modules(model_name: str) -> list[str]:
    name = model_name.lower()

    # Good default LoRA targets for modern decoder-only transformers.
    if "qwen" in name:
        return ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"]
    if "gemma" in name:
        return ["q_proj", "k_proj", "v_proj", "o_proj", "up_proj", "down_proj", "gate_proj"]

    # Generic fallback
    return ["q_proj", "k_proj", "v_proj", "o_proj"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Training JSONL with code and reference_documentation")
    parser.add_argument("--model", required=True, help="Base HF model name/path")
    parser.add_argument("--output-dir", required=True, help="Directory to save adapters/checkpoints")
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)

    parser.add_argument("--max-seq-length", type=int, default=1024)
    parser.add_argument("--learning-rate", type=float, default=2e-4)
    parser.add_argument("--num-train-epochs", type=float, default=2.0)
    parser.add_argument("--per-device-train-batch-size", type=int, default=2)
    parser.add_argument("--per-device-eval-batch-size", type=int, default=2)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--logging-steps", type=int, default=10)
    parser.add_argument("--save-steps", type=int, default=100)
    parser.add_argument("--eval-steps", type=int, default=100)
    parser.add_argument("--warmup-ratio", type=float, default=0.03)
    parser.add_argument("--weight-decay", type=float, default=0.0)

    parser.add_argument("--lora-r", type=int, default=16)
    parser.add_argument("--lora-alpha", type=int, default=32)
    parser.add_argument("--lora-dropout", type=float, default=0.05)

    parser.add_argument("--use-4bit", action="store_true", help="Enable QLoRA-style 4-bit loading")
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    raw_rows = read_jsonl(input_path)
    pc_rows = convert_to_prompt_completion(raw_rows)
    if not pc_rows:
        raise ValueError("No valid training rows found after prompt-completion conversion.")

    train_rows, val_rows = split_rows(pc_rows, args.val_ratio, args.seed)
    train_ds = Dataset.from_list(train_rows)
    eval_ds = Dataset.from_list(val_rows) if val_rows else None

    tokenizer = AutoTokenizer.from_pretrained(args.model, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    quant_config = None
    model_kwargs: dict[str, Any] = {"trust_remote_code": True}

    if args.use_4bit:
        quant_config = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        )
        model_kwargs["quantization_config"] = quant_config
        model_kwargs["device_map"] = "auto"
    else:
        if args.bf16:
            model_kwargs["torch_dtype"] = torch.bfloat16
        elif args.fp16:
            model_kwargs["torch_dtype"] = torch.float16

    model = AutoModelForCausalLM.from_pretrained(args.model, **model_kwargs)
    model.config.use_cache = False

    peft_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        bias="none",
        task_type="CAUSAL_LM",
        target_modules=choose_target_modules(args.model),
    )

    training_args = SFTConfig(
        output_dir=str(output_dir),
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        per_device_train_batch_size=args.per_device_train_batch_size,
        per_device_eval_batch_size=args.per_device_eval_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        eval_steps=args.eval_steps,
        eval_strategy="steps" if eval_ds is not None else "no",
        save_strategy="steps",
        warmup_ratio=args.warmup_ratio,
        weight_decay=args.weight_decay,
        lr_scheduler_type="cosine",
        bf16=args.bf16,
        fp16=args.fp16,
        max_length=args.max_seq_length,
        packing=False,
        completion_only_loss=True,
        report_to="none",
        seed=args.seed,
    )

    trainer = SFTTrainer(
        model=model,
        args=training_args,
        train_dataset=train_ds,
        eval_dataset=eval_ds,
        processing_class=tokenizer,
        peft_config=peft_config,
    )

    trainer.train()
    trainer.save_model(str(output_dir / "final_adapter"))
    tokenizer.save_pretrained(str(output_dir / "final_adapter"))

    # Save split summaries for reproducibility
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "train_size.txt").write_text(str(len(train_rows)), encoding="utf-8")
    (output_dir / "val_size.txt").write_text(str(len(val_rows)), encoding="utf-8")


if __name__ == "__main__":
    main()