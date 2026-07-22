#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Any

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig


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


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def clean_generated_text(text: str) -> str:
    text = (text or "").strip()

    prefixes = [
        "Documentation:",
        "Description:",
        "Docstring:",
        "Answer:",
        "Output:",
    ]
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()

    text = text.replace("```", " ")
    text = " ".join(text.split())

    bad_prefixes = (
        "def ",
        "class ",
        "return ",
        "if ",
        "for ",
        "while ",
        "try:",
        "except ",
        "with ",
        "function ",
        "const ",
        "let ",
        "var ",
        "public ",
        "private ",
        "protected ",
        "@param",
        "@returns",
        "@return",
    )

    if text.startswith(bad_prefixes):
        parts = text.split(". ")
        kept = []
        for part in parts:
            s = part.strip()
            if s.startswith(bad_prefixes):
                continue
            kept.append(part)
        text = ". ".join(kept).strip()

    sentences = []
    current = ""
    for ch in text:
        current += ch
        if ch in ".!?":
            sentences.append(current.strip())
            current = ""
            if len(sentences) == 2:
                break

    if sentences:
        text = " ".join(sentences).strip()
    else:
        words = text.split()
        text = " ".join(words[:30]).strip()

    return text


def build_prompt(row: dict[str, Any]) -> str:
    prompt = row.get("prompt")
    if prompt and str(prompt).strip():
        return str(prompt)

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

    parts.extend([
        f"Code:\n{row.get('code', '')}",
        "",
        "Documentation:",
    ])
    return "\n".join(parts)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-model", required=True, help="HF base model name/path")
    parser.add_argument("--adapter-path", required=True, help="Saved LoRA adapter directory")
    parser.add_argument("--input", required=True, help="Input JSONL")
    parser.add_argument("--output", required=True, help="Output JSONL")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--use-4bit", action="store_true")
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--fp16", action="store_true")
    parser.add_argument("--max-new-tokens", type=int, default=96)
    parser.add_argument("--temperature", type=float, default=0.2)
    parser.add_argument("--do-sample", action="store_true")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    if output_path.exists() and not args.overwrite:
        raise FileExistsError(f"Output file already exists: {output_path}")

    rows = read_jsonl(input_path)
    if args.limit is not None:
        rows = rows[:args.limit]

    if not rows:
        raise ValueError("No rows found in input.")

    tokenizer = AutoTokenizer.from_pretrained(args.base_model, use_fast=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model_kwargs: dict[str, Any] = {"trust_remote_code": True}

    if args.use_4bit:
        model_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_use_double_quant=True,
            bnb_4bit_compute_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        )
        model_kwargs["device_map"] = "auto"
    else:
        if args.bf16:
            model_kwargs["torch_dtype"] = torch.bfloat16
        elif args.fp16:
            model_kwargs["torch_dtype"] = torch.float16

    base_model = AutoModelForCausalLM.from_pretrained(args.base_model, **model_kwargs)
    model = PeftModel.from_pretrained(base_model, args.adapter_path)
    model.eval()

    output_rows: list[dict[str, Any]] = []

    for idx, row in enumerate(rows, start=1):
        prompt = build_prompt(row)

        inputs = tokenizer(prompt, return_tensors="pt")
        if hasattr(model, "device") and str(model.device) != "cpu":
            inputs = {k: v.to(model.device) for k, v in inputs.items()}

        start = time.time()
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=args.max_new_tokens,
                do_sample=args.do_sample,
                temperature=args.temperature if args.do_sample else None,
                pad_token_id=tokenizer.eos_token_id,
                eos_token_id=tokenizer.eos_token_id,
            )
        latency = time.time() - start

        gen_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        raw_text = tokenizer.decode(gen_tokens, skip_special_tokens=True)
        generated_text = clean_generated_text(raw_text)

        out = {
            "sample_id": row["sample_id"],
            "language": row["language"],
            "func_name": row.get("func_name", ""),
            "prompt_template_id": row.get("prompt_template_id", ""),
            "model_name": f"{args.base_model}+LoRA",
            "reference_documentation": row.get("reference_documentation", ""),
            "generated_documentation": generated_text,
            "latency_seconds": round(latency, 4),
        }

        if "resolved_func_name" in row:
            out["resolved_func_name"] = row.get("resolved_func_name", "")
        if "func_name_source" in row:
            out["func_name_source"] = row.get("func_name_source", "")

        output_rows.append(out)
        print(f"[{idx}/{len(rows)}] {row['sample_id']} done in {latency:.2f}s")

    write_jsonl(output_path, output_rows)
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()