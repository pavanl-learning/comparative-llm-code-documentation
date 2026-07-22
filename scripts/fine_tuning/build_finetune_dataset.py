#!/usr/bin/env python3
import argparse
import json
import random
from collections import defaultdict
from pathlib import Path


def load_jsonl(path: Path):
    rows = []
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


def write_jsonl(path: Path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def normalize_row(row):
    ref = (row.get("reference_documentation") or "").strip()
    code = (row.get("code") or "").strip()
    prompt = (row.get("prompt") or "").strip()

    if not ref or not code or not prompt:
        return None

    return {
        "sample_id": row.get("sample_id", ""),
        "language": row.get("language", ""),
        "func_name": row.get("resolved_func_name") or row.get("func_name") or "",
        "code": code,
        "reference_documentation": ref,
        "prompt": prompt,
        "completion": ref,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--train-out", required=True)
    parser.add_argument("--valid-out", required=True)
    parser.add_argument("--smoke-out", required=True)
    parser.add_argument("--train-per-language", type=int, default=1000)
    parser.add_argument("--valid-per-language", type=int, default=100)
    parser.add_argument("--smoke-per-language", type=int, default=8)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)

    rows = load_jsonl(Path(args.input))
    norm_rows = []

    for row in rows:
        nr = normalize_row(row)
        if nr is not None and nr["language"] in {"python", "javascript", "java"}:
            norm_rows.append(nr)

    by_lang = defaultdict(list)
    for row in norm_rows:
        by_lang[row["language"]].append(row)

    for lang in ["python", "javascript", "java"]:
        random.shuffle(by_lang[lang])

    train_rows = []
    valid_rows = []
    smoke_rows = []

    for lang in ["python", "javascript", "java"]:
        need_total = (
            args.train_per_language
            + args.valid_per_language
            + args.smoke_per_language
        )
        available = len(by_lang[lang])

        if available < need_total:
            raise ValueError(
                f"Not enough rows for {lang}. Need {need_total}, found {available}"
            )

        lang_rows = by_lang[lang]
        smoke = lang_rows[:args.smoke_per_language]
        valid = lang_rows[
            args.smoke_per_language : args.smoke_per_language + args.valid_per_language
        ]
        train = lang_rows[
            args.smoke_per_language + args.valid_per_language :
            args.smoke_per_language + args.valid_per_language + args.train_per_language
        ]

        smoke_rows.extend(smoke)
        valid_rows.extend(valid)
        train_rows.extend(train)

    random.shuffle(smoke_rows)
    random.shuffle(valid_rows)
    random.shuffle(train_rows)

    write_jsonl(Path(args.smoke_out), smoke_rows)
    write_jsonl(Path(args.valid_out), valid_rows)
    write_jsonl(Path(args.train_out), train_rows)

    print(f"Wrote smoke set: {args.smoke_out} ({len(smoke_rows)} rows)")
    print(f"Wrote valid set: {args.valid_out} ({len(valid_rows)} rows)")
    print(f"Wrote train set: {args.train_out} ({len(train_rows)} rows)")


if __name__ == "__main__":
    main()