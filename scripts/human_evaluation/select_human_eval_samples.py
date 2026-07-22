#!/usr/bin/env python3

import argparse
import json
import random
from pathlib import Path


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def extract_ids(path: Path):
    rows = load_jsonl(path)
    ids = [str(r["sample_id"]) for r in rows if "sample_id" in r]
    if not ids:
        raise ValueError(f"No sample_id values found in {path}")
    return ids


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--python_file", required=True)
    parser.add_argument("--javascript_file", required=True)
    parser.add_argument("--java_file", required=True)
    parser.add_argument("--n_per_language", type=int, default=20)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    random.seed(args.seed)

    py_ids = extract_ids(Path(args.python_file))
    js_ids = extract_ids(Path(args.javascript_file))
    java_ids = extract_ids(Path(args.java_file))

    if len(py_ids) < args.n_per_language:
        raise ValueError("Not enough Python samples")
    if len(js_ids) < args.n_per_language:
        raise ValueError("Not enough JavaScript samples")
    if len(java_ids) < args.n_per_language:
        raise ValueError("Not enough Java samples")

    selected_py = sorted(random.sample(py_ids, args.n_per_language))
    selected_js = sorted(random.sample(js_ids, args.n_per_language))
    selected_java = sorted(random.sample(java_ids, args.n_per_language))

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with out_path.open("w", encoding="utf-8") as f:
        for sid in selected_py:
            f.write(sid + "\n")
        for sid in selected_js:
            f.write(sid + "\n")
        for sid in selected_java:
            f.write(sid + "\n")

    print(f"Wrote {out_path}")
    print(f"Python: {len(selected_py)}")
    print(f"JavaScript: {len(selected_js)}")
    print(f"Java: {len(selected_java)}")
    print(f"Total: {len(selected_py) + len(selected_js) + len(selected_java)}")


if __name__ == "__main__":
    main()