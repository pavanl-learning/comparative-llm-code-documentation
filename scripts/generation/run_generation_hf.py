#!/usr/bin/env python3

import argparse
import json
import re
import time
from pathlib import Path

import torch
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM


SPECIAL_TOKENS_TO_REMOVE = [
    "<|file_separator|>",
    "<|endoftext|>",
    "<|fim_prefix|>",
    "<|fim_middle|>",
    "<|fim_suffix|>",
    "<bos>",
    "<eos>",
    "<pad>",
]

BAD_PREFIXES = [
    "Documentation:",
    "documentation:",
    "### Documentation:",
    "## Documentation:",
    "# Documentation:",
    "Description:",
    "Docstring:",
    "Answer:",
    "Response:",
]

CODE_FENCE_PATTERNS = [
    "```python",
    "```java",
    "```javascript",
    "```js",
    "```",
]


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run Hugging Face generation for documentation prompts."
    )

    parser.add_argument("--model", required=True)
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    parser.add_argument("--max-new-tokens", type=int, default=120)
    parser.add_argument("--limit", type=int, default=None)

    parser.add_argument("--overwrite", action="store_true")
    parser.add_argument("--start-from-existing-output", action="store_true")

    parser.add_argument("--do-sample", action="store_true")
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top-p", type=float, default=1.0)
    parser.add_argument("--top-k", type=int, default=50)

    parser.add_argument(
        "--no-chat-template",
        action="store_true",
        help="Disable tokenizer chat template. Use only for non-instruct/base models.",
    )

    return parser.parse_args()


def strip_special_tokens(text: str) -> str:
    text = text or ""
    for tok in SPECIAL_TOKENS_TO_REMOVE:
        text = text.replace(tok, "")
    return text.strip()


def strip_code_fences(text: str) -> str:
    text = text or ""
    for pat in CODE_FENCE_PATTERNS:
        text = text.replace(pat, "")
    return text.strip()


def strip_bad_prefixes(text: str) -> str:
    text = text.strip()
    changed = True

    while changed:
        changed = False
        for prefix in BAD_PREFIXES:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()
                changed = True

    return text


def normalize_whitespace(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def remove_obvious_code_leakage(text: str) -> str:
    """
    Stops only when obvious code begins after documentation text.
    This is intentionally less aggressive than the older version.
    """
    kept = []

    for line in text.splitlines():
        ln = line.strip()
        low = ln.lower()

        if not ln:
            continue

        if re.match(r"^(def |class |async def |import |from .* import )", ln):
            break

        if re.match(r"^(public|private|protected)\s+", ln):
            break

        if re.match(r"^(static|final|abstract|synchronized)\s+", ln):
            break

        if re.match(r"^(const|let|var)\s+[A-Za-z_$]", ln):
            break

        if re.match(r"^(if|for|while|switch|try|catch)\s*\(", ln):
            break

        if re.match(r"^[A-Za-z_$][A-Za-z0-9_$]*\s*=\s*", ln):
            break

        if low in {"{", "}", "};"}:
            break

        if low in {"script", "code:", "implementation:"}:
            break

        kept.append(ln)

    return " ".join(kept).strip()


def clean_generated_text(text: str) -> str:
    text = strip_special_tokens(text)
    text = strip_code_fences(text)
    text = strip_bad_prefixes(text)
    text = normalize_whitespace(text)
    text = remove_obvious_code_leakage(text)
    text = strip_special_tokens(text)

    text = re.sub(r"\s+", " ", text).strip()
    text = re.sub(r"\s*[:;,/-]\s*$", "", text).strip()

    if text in {'"""', "'''", "```", "``", "`"}:
        return ""

    return text


def classify_generation_error(text: str):
    stripped = (text or "").strip()

    if not stripped:
        return "empty_after_cleaning"

    if stripped in {'"""', "'''", "```", "``", "`"}:
        return "artifact_only_after_cleaning"

    if len(stripped.split()) < 5:
        return "too_short_after_cleaning"

    return None


def read_existing_sample_ids(out_path: Path):
    existing = set()

    if not out_path.exists():
        return existing

    with out_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            try:
                obj = json.loads(line)
                sample_id = obj.get("sample_id")
                if sample_id:
                    existing.add(sample_id)
            except json.JSONDecodeError:
                continue

    return existing


def build_prompt(tokenizer, raw_prompt: str, use_chat_template: bool) -> str:
    if not use_chat_template:
        return raw_prompt

    if getattr(tokenizer, "chat_template", None):
        return tokenizer.apply_chat_template(
            [{"role": "user", "content": raw_prompt}],
            tokenize=False,
            add_generation_prompt=True,
        )

    return raw_prompt


def main():
    args = parse_args()

    input_file = Path(args.input)
    out_path = Path(args.output)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    out_path.parent.mkdir(parents=True, exist_ok=True)

    if out_path.exists() and args.overwrite and args.start_from_existing_output:
        raise ValueError("Use either --overwrite or --start-from-existing-output, not both.")

    if out_path.exists() and not args.overwrite and not args.start_from_existing_output:
        raise FileExistsError(
            f"Output already exists: {out_path}. Use --overwrite or --start-from-existing-output."
        )

    rows = load_jsonl(input_file)

    if args.limit is not None:
        rows = rows[: args.limit]

    existing_ids = set()
    file_mode = "w"

    if args.start_from_existing_output and out_path.exists():
        existing_ids = read_existing_sample_ids(out_path)
        file_mode = "a"
        print(f"Resuming from {out_path}; found {len(existing_ids)} existing sample_ids.")

    if existing_ids:
        rows_to_generate = [
            row for row in rows if row.get("sample_id") not in existing_ids
        ]
    else:
        rows_to_generate = rows

    print(f"Rows requested: {len(rows)}")
    print(f"Rows remaining: {len(rows_to_generate)}")
    print(f"Loading model: {args.model}")

    tokenizer = AutoTokenizer.from_pretrained(args.model)

    # tokenizer.add_special_tokens(
    #     {
    #         "additional_special_tokens": [
    #             "<|file_separator|>",
    #             "<|fim_prefix|>",
    #             "<|fim_middle|>",
    #             "<|fim_suffix|>",
    #         ]
    #     }
    # )

    if tokenizer.pad_token_id is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
        device_map="auto",
        low_cpu_mem_usage=True,
    )

    # model.resize_token_embeddings(len(tokenizer))
    model.config.pad_token_id = tokenizer.pad_token_id
    model.eval()

    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"Pad token id: {tokenizer.pad_token_id}")
    print(f"EOS token id: {tokenizer.eos_token_id}")
    print(f"Chat template used: {not args.no_chat_template}")

    with out_path.open(file_mode, encoding="utf-8") as f:
        for row in tqdm(rows_to_generate, desc="Generating"):
            raw_prompt = row["prompt"]
            prompt = build_prompt(
                tokenizer=tokenizer,
                raw_prompt=raw_prompt,
                use_chat_template=not args.no_chat_template,
            )

            start = time.time()

            inputs = tokenizer(
                prompt,
                return_tensors="pt",
                truncation=True,
            ).to(model.device)

            gen_kwargs = {
                "max_new_tokens": args.max_new_tokens,
                "do_sample": args.do_sample,
                "pad_token_id": tokenizer.pad_token_id,
                "eos_token_id": tokenizer.eos_token_id,
            }

            if args.do_sample:
                gen_kwargs["temperature"] = args.temperature
                gen_kwargs["top_p"] = args.top_p
                gen_kwargs["top_k"] = args.top_k

            with torch.no_grad():
                outputs = model.generate(**inputs, **gen_kwargs)

            prompt_len = inputs["input_ids"].shape[1]
            generated_ids = outputs[0][prompt_len:]

            raw_generated_text = tokenizer.decode(
                generated_ids,
                skip_special_tokens=True,
            )

            raw_stripped = strip_special_tokens(raw_generated_text).strip()

            if not raw_stripped:
                generated_text = ""
                generation_error = "empty_raw_generation"
            else:
                generated_text = clean_generated_text(raw_generated_text)
                generation_error = classify_generation_error(generated_text)

            latency = time.time() - start

            out = {
                "sample_id": row["sample_id"],
                "language": row["language"],
                "func_name": row.get("func_name", ""),
                "prompt_template_id": row["prompt_template_id"],
                "model_name": args.model,
                "reference_documentation": row["reference_documentation"],
                "generated_documentation": generated_text,
                "raw_generated_text": raw_generated_text,
                "latency_seconds": round(latency, 4),
            }

            if generation_error:
                out["generation_error"] = generation_error

            if "resolved_func_name" in row:
                out["resolved_func_name"] = row["resolved_func_name"]

            if "func_name_source" in row:
                out["func_name_source"] = row["func_name_source"]

            f.write(json.dumps(out, ensure_ascii=False) + "\n")
            f.flush()

    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()