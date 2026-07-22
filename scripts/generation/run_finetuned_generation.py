#!/usr/bin/env python3
import argparse
import json
import time
from pathlib import Path
from typing import Any

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
    return rows


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

    # Keep it compact: at most first 2 sentences
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
        return str(prompt).strip()

    language = row.get("language", "")
    func_name = (
        row.get("resolved_func_name")
        or row.get("func_name")
        or row.get("raw_func_name")
        or ""
    )
    code = row.get("code", "")

    return (
        f"Write a very short API-docstring-style description for the following function in plain text. "
        f"Use exactly 1 sentence when possible, and never more than 2 short sentences. "
        f"Start with the function's main purpose.\n\n"
        f"Language: {language}\n"
        f"Function name: {func_name}\n"
        f"Code:\n{code}\n\n"
        f"Documentation:"
    )


def load_completed_ids(path: Path) -> set[str]:
    ids: set[str] = set()
    if not path.exists():
        return ids

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            row = json.loads(line)
            sample_id = row.get("sample_id")
            if sample_id:
                ids.add(str(sample_id))
    return ids


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input prompted/test JSONL")
    parser.add_argument("--output", required=True, help="Output generations JSONL")
    parser.add_argument(
        "--base-model",
        default="Qwen/Qwen2.5-Coder-1.5B-Instruct",
        help="Base model name",
    )
    parser.add_argument(
        "--adapter-path",
        required=True,
        help="Path to trained LoRA adapter directory",
    )
    parser.add_argument(
        "--model-name",
        default="qwen25_coder_1_5b_instruct_lora_multilang",
        help="Model name to record in JSONL output",
    )
    parser.add_argument("--max-new-tokens", type=int, default=64)
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--start-from-existing-output",
        action="store_true",
        help="Skip sample_ids already present in the output file",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    adapter_path = Path(args.adapter_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if not adapter_path.exists():
        raise FileNotFoundError(f"Adapter path not found: {adapter_path}")

    rows = load_jsonl(input_path)
    if args.limit is not None:
        rows = rows[:args.limit]

    completed_ids: set[str] = set()
    if args.start_from_existing_output:
        completed_ids = load_completed_ids(output_path)

    pending_rows = [r for r in rows if str(r.get("sample_id", "")) not in completed_ids]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(args.base_model, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print("Loading base model...")
    base_model = AutoModelForCausalLM.from_pretrained(
        args.base_model,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )

    print("Loading LoRA adapter...")
    model = PeftModel.from_pretrained(base_model, str(adapter_path))
    model.eval()

    write_mode = "a" if args.start_from_existing_output and output_path.exists() else "w"

    with output_path.open(write_mode, encoding="utf-8") as f:
        for idx, row in enumerate(pending_rows, start=1):
            prompt = build_prompt(row)

            inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

            start = time.time()
            with torch.no_grad():
                gen_kwargs = {
                    "max_new_tokens": args.max_new_tokens,
                    "do_sample": args.temperature > 0.0,
                    "temperature": args.temperature if args.temperature > 0.0 else None,
                    "top_p": args.top_p,
                    "pad_token_id": tokenizer.pad_token_id,
                    "eos_token_id": tokenizer.eos_token_id,
                }
                gen_kwargs = {k: v for k, v in gen_kwargs.items() if v is not None}

                output_ids = model.generate(
                    **inputs,
                    **gen_kwargs,
                )

            latency = time.time() - start

            generated_ids = output_ids[0][inputs["input_ids"].shape[1]:]
            raw_text = tokenizer.decode(generated_ids, skip_special_tokens=True)
            generated_text = clean_generated_text(raw_text)

            out = {
                "sample_id": row["sample_id"],
                "language": row["language"],
                "func_name": row.get("func_name", ""),
                "prompt_template_id": row.get("prompt_template_id", "ZS"),
                "model_name": args.model_name,
                "reference_documentation": row.get("reference_documentation", ""),
                "generated_documentation": generated_text,
                "latency_seconds": round(latency, 4),
            }

            if "resolved_func_name" in row:
                out["resolved_func_name"] = row.get("resolved_func_name", "")
            if "func_name_source" in row:
                out["func_name_source"] = row.get("func_name_source", "")

            f.write(json.dumps(out, ensure_ascii=False) + "\n")
            f.flush()

            print(
                f"[{idx}/{len(pending_rows)}] {row['sample_id']} "
                f"done in {latency:.2f}s"
            )

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()