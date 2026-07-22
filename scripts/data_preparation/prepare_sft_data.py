#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Any


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Source JSONL")
    parser.add_argument("--train-output", required=True)
    parser.add_argument("--val-output", required=True)
    parser.add_argument("--test-output", required=True)
    parser.add_argument("--language", default=None, help="Optional language filter: python/java/javascript")
    parser.add_argument("--train-ratio", type=float, default=0.8)
    parser.add_argument("--val-ratio", type=float, default=0.1)
    parser.add_argument("--test-ratio", type=float, default=0.1)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--exclude-sample-ids-file",
        default=None,
        help="Optional JSONL file whose sample_ids should be excluded from splitting",
    )
    args = parser.parse_args()

    total = args.train_ratio + args.val_ratio + args.test_ratio
    if abs(total - 1.0) > 1e-8:
        raise ValueError("train-ratio + val-ratio + test-ratio must sum to 1.0")

    rows = read_jsonl(Path(args.input))

    if args.language:
        lang = args.language.strip().lower()
        rows = [r for r in rows if str(r.get("language", "")).strip().lower() == lang]

    excluded_ids: set[str] = set()
    if args.exclude_sample_ids_file:
        for row in read_jsonl(Path(args.exclude_sample_ids_file)):
            sample_id = row.get("sample_id")
            if sample_id:
                excluded_ids.add(str(sample_id))

    if excluded_ids:
        rows = [r for r in rows if str(r.get("sample_id")) not in excluded_ids]

    if not rows:
        raise ValueError("No rows left after filtering.")

    rng = random.Random(args.seed)
    rng.shuffle(rows)

    n = len(rows)
    n_train = int(n * args.train_ratio)
    n_val = int(n * args.val_ratio)

    train_rows = rows[:n_train]
    val_rows = rows[n_train:n_train + n_val]
    test_rows = rows[n_train + n_val:]

    write_jsonl(Path(args.train_output), train_rows)
    write_jsonl(Path(args.val_output), val_rows)
    write_jsonl(Path(args.test_output), test_rows)

    print(f"Total rows: {n}")
    print(f"Train: {len(train_rows)}")
    print(f"Val:   {len(val_rows)}")
    print(f"Test:  {len(test_rows)}")

if __name__ == "__main__":
    main()