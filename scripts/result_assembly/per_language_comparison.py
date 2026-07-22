import json
from pathlib import Path
from collections import defaultdict

FILES = {
    "Qwen2.5-1.5B-Instruct": Path("outputs/evaluations/qwen25_1_5b_instruct_P1_zero_shot_balanced_300_detailed.jsonl"),
    "Qwen2.5-Coder-1.5B-Instruct": Path("outputs/evaluations/qwen25_coder_1_5b_instruct_P1_zero_shot_balanced_300_detailed.jsonl"),
}

OUTPUT_DIR = Path("outputs/evaluations")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def mean(values):
    values = [v for v in values if v is not None]
    return sum(values) / len(values) if values else None


def summarize_by_language(rows):
    buckets = defaultdict(list)
    for row in rows:
        buckets[row["language"]].append(row)

    summary = {}
    for language, items in buckets.items():
        summary[language] = {
            "num_samples": len(items),
            "mean_latency_seconds": mean([r.get("latency_seconds") for r in items]),
            "mean_generated_word_count": mean([r.get("generated_word_count") for r in items]),
            "mean_rouge1_fmeasure": mean([r.get("rouge1_fmeasure") for r in items]),
            "mean_rouge2_fmeasure": mean([r.get("rouge2_fmeasure") for r in items]),
            "mean_rougeL_fmeasure": mean([r.get("rougeL_fmeasure") for r in items]),
            "mean_bertscore_f1": mean([r.get("bertscore_f1") for r in items]),
        }
    return summary


def main():
    all_results = {}

    for model_name, path in FILES.items():
        rows = load_jsonl(path)
        all_results[model_name] = summarize_by_language(rows)

    out_path = OUTPUT_DIR / "per_language_comparison_balanced_300.json"
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2)

    print(f"Wrote {out_path}\n")

    for model_name, summary in all_results.items():
        print(f"=== {model_name} ===")
        for language, metrics in summary.items():
            print(f"\n{language}")
            for k, v in metrics.items():
                print(f"  {k}: {v}")
        print()


if __name__ == "__main__":
    main()
