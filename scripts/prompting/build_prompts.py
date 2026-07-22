#!/usr/bin/env python3
"""
Build prompted JSONL files from the processed balanced CodeSearchNet dataset.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List


INPUT_FILE = Path("data/processed/codesearchnet_balanced_15000.jsonl")
OUTPUT_DIR = Path("data/processed/prompted")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

P1_OUTPUT = OUTPUT_DIR / "P1_zero_shot_balanced_15000.jsonl"

PROMPT_INSTRUCTION = (
    "Write a very short API-docstring-style description for the following function in plain text. "
    "Use exactly 1 sentence when possible, and never more than 2 short sentences. Start with the function's main purpose. "
    "Mention parameters or return value only if they are clearly inferable from the code and can be stated briefly. "
    "Use only information supported by the code. If details are unclear, keep the description general. "
    "Keep the wording brief, direct, and compact. Do not include markdown, code blocks, examples, headings, lists, "
    "implementation steps, or speculative details."
)


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
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


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def build_p1_prompt(language: str, func_name: str, code: str) -> str:
    parts = [
        PROMPT_INSTRUCTION,
        "",
        f"Language: {language}",
    ]
    if func_name and func_name.strip():
        parts.append(f"Function name: {func_name}")
    parts.extend([
        f"Code:\n{code.rstrip()}",
        "",
        "Documentation:",
    ])
    return "\n".join(parts)


def main() -> None:
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found: {INPUT_FILE}")

    rows = read_jsonl(INPUT_FILE)
    prompted_rows: List[Dict[str, Any]] = []

    for row in rows:
        prompted_rows.append({
            "sample_id": row["sample_id"],
            "language": row["language"],
            "func_name": row.get("func_name", ""),
            "code": row["code"],
            "reference_documentation": row["reference_documentation"],
            "prompt_template_id": "P1_zero_shot",
            "prompt": build_p1_prompt(
                language=row["language"],
                func_name=row.get("func_name", ""),
                code=row["code"],
            ),
        })

    write_jsonl(P1_OUTPUT, prompted_rows)
    print(f"Wrote {P1_OUTPUT} ({len(prompted_rows)} rows)")


if __name__ == "__main__":
    main()