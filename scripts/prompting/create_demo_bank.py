import json
from pathlib import Path
from collections import defaultdict

INPUT_FILE = Path("data/processed/prompted/P1_zero_shot.jsonl")
EVAL_FILE = Path("data/processed/prompted/P1_zero_shot_balanced_300.jsonl")
OUTPUT_FILE = Path("data/processed/demo_bank.jsonl")

TARGETS = {
    "python": 3,
    "java": 3,
    "javascript": 3,
}


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def main():
    all_rows = load_jsonl(INPUT_FILE)
    eval_rows = load_jsonl(EVAL_FILE)
    eval_ids = {r["sample_id"] for r in eval_rows}

    buckets = defaultdict(list)
    for row in all_rows:
        if row["sample_id"] in eval_ids:
            continue
        buckets[row["language"]].append(row)

    selected = []
    for language, target in TARGETS.items():
        chosen = buckets[language][:target]
        selected.extend(chosen)

    with OUTPUT_FILE.open("w", encoding="utf-8") as f:
        for row in selected:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    print(f"Wrote {OUTPUT_FILE}")
    total = 0
    for language, target in TARGETS.items():
        available = len(buckets[language])
        picked = min(target, available)
        total += picked
        print(f"{language}: available={available}, selected={picked}")
    print(f"total_selected={total}")


if __name__ == "__main__":
    main()
