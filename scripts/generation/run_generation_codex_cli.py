#!/usr/bin/env python3
import argparse
import json
import shlex
import subprocess
import time
from pathlib import Path


SYSTEM_PROMPT = (
    "Write a very short API-docstring-style description for the following function in plain text. "
    "Use exactly 1 sentence when possible, and never more than 2 short sentences. "
    "Start with the function's main purpose. "
    "Mention parameters or return value only if they are clearly inferable from the code and can be stated briefly. "
    "Use only information supported by the code. "
    "If details are unclear, keep the description general. "
    "Keep the wording brief, direct, and compact. "
    "Do not include markdown, code blocks, examples, headings, lists, implementation steps, or speculative details."
)


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def clean_generated_text(text: str) -> str:
    text = text.strip()

    prefixes = [
        "Documentation:",
        "Description:",
        "Docstring:",
    ]
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()

    bad_starts = (
        "```",
        "def ",
        "class ",
    )
    if text.startswith(bad_starts):
        lines = text.splitlines()
        non_code = []
        for line in lines:
            s = line.strip()
            if (
                s.startswith("def ")
                or s.startswith("class ")
                or s.startswith("return ")
                or s.startswith("if ")
                or s.startswith("for ")
                or s.startswith("while ")
                or s.startswith("try:")
                or s.startswith("except ")
                or s.startswith("with ")
                or s.startswith("```")
            ):
                continue
            non_code.append(line)
        text = " ".join(non_code).strip()

    text = " ".join(text.split())

    sentences = []
    current = ""
    for ch in text:
        current += ch
        if ch in ".!?":
            sentences.append(current.strip())
            current = ""
            if len(sentences) == 2:
                break
    if not sentences and text:
        return text
    return " ".join(sentences).strip()


def build_prompt(row: dict) -> str:
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"Language: {row['language']}\n"
        f"Function name: {row.get('func_name', '')}\n"
        f"Code:\n{row['code']}\n\n"
        f"Documentation:"
    )


def call_codex(prompt: str, codex_cmd: str, model_name: str | None = None) -> str:
    cmd = shlex.split(codex_cmd) + ["exec", "--skip-git-repo-check"]

    if model_name:
        cmd += ["-m", model_name]

    cmd += [prompt]

    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"Codex CLI failed with exit code {proc.returncode}\n"
            f"STDERR:\n{proc.stderr}\nSTDOUT:\n{proc.stdout}"
        )
    return proc.stdout.strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input JSONL file")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--model-name", default="codex-cli", help="Value to store in model_name")
    parser.add_argument("--codex-cmd", default="codex", help="Codex CLI executable name")
    parser.add_argument("--limit", type=int, default=None, help="Optional row limit")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if output_path.exists() and not args.overwrite:
        raise FileExistsError(f"Output file already exists: {output_path}")

    rows = load_jsonl(input_path)
    if args.limit is not None:
        rows = rows[:args.limit]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        for idx, row in enumerate(rows, start=1):
            prompt = build_prompt(row)
            start = time.time()
            raw = call_codex(prompt, args.codex_cmd, args.model_name)
            latency = time.time() - start
            generated_text = clean_generated_text(raw)

            out = {
                "sample_id": row["sample_id"],
                "language": row["language"],
                "func_name": row.get("func_name", ""),
                "prompt_template_id": row["prompt_template_id"],
                "model_name": args.model_name,
                "reference_documentation": row["reference_documentation"],
                "generated_documentation": generated_text,
                "latency_seconds": round(latency, 4),
            }
            f.write(json.dumps(out, ensure_ascii=False) + "\n")
            f.flush()
            print(f"[{idx}/{len(rows)}] {row['sample_id']} done in {latency:.2f}s")

    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()