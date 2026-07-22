#!/usr/bin/env python3

import argparse
import json
import math
import random
from pathlib import Path
from typing import Dict, List, Any


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def safe_float(x, default=0.0):
    try:
        if x is None:
            return default
        return float(x)
    except Exception:
        return default


def compute_combined_score(row: Dict[str, Any]) -> float:
    bleu = safe_float(row.get("bleu"), 0.0)
    rouge_l = safe_float(row.get("rougeL_fmeasure"), 0.0)
    bert = safe_float(row.get("bertscore_f1"), 0.0)
    return (bleu + rouge_l + bert) / 3.0


def stratified_sample(rows: List[Dict[str, Any]], n_total: int, seed: int) -> List[Dict[str, Any]]:
    if len(rows) < n_total:
        raise ValueError(f"Not enough rows to sample {n_total}; found {len(rows)}")

    rows_sorted = sorted(rows, key=compute_combined_score, reverse=True)
    n = len(rows_sorted)

    high_end = n // 3
    med_end = 2 * n // 3

    high = rows_sorted[:high_end]
    medium = rows_sorted[high_end:med_end]
    low = rows_sorted[med_end:]

    # For n_total=20 -> 7 high, 6 medium, 7 low
    n_high = math.ceil(n_total / 3)
    n_low = math.ceil(n_total / 3)
    n_medium = n_total - n_high - n_low

    rng = random.Random(seed)

    if len(high) < n_high or len(medium) < n_medium or len(low) < n_low:
        raise ValueError(
            f"Insufficient rows in strata: high={len(high)}, medium={len(medium)}, low={len(low)}"
        )

    selected = []
    selected.extend(rng.sample(high, n_high))
    selected.extend(rng.sample(medium, n_medium))
    selected.extend(rng.sample(low, n_low))

    return sorted(selected, key=lambda r: str(r["sample_id"]))


def language_breakdown(rows: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        lang = str(row.get("language", "")).lower()
        grouped.setdefault(lang, []).append(row)
    return grouped


def write_selected_ids(path: Path, selected: Dict[str, List[Dict[str, Any]]]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for lang in ["python", "javascript", "java"]:
            for row in selected.get(lang, []):
                f.write(str(row["sample_id"]) + "\n")


def write_selection_report(path: Path, selected: Dict[str, List[Dict[str, Any]]]) -> None:
    report = {}
    total = 0
    for lang in ["python", "javascript", "java"]:
        lang_rows = selected.get(lang, [])
        total += len(lang_rows)
        report[lang] = {
            "num_selected": len(lang_rows),
            "samples": [
                {
                    "sample_id": r["sample_id"],
                    "func_name": r.get("func_name", ""),
                    "combined_score": compute_combined_score(r),
                    "bleu": r.get("bleu"),
                    "rougeL_fmeasure": r.get("rougeL_fmeasure"),
                    "bertscore_f1": r.get("bertscore_f1"),
                }
                for r in lang_rows
            ],
        }
    report["total_selected"] = total

    with path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--detailed_eval",
        required=True,
        help="Detailed evaluation JSONL file used as reference for stratification",
    )
    parser.add_argument(
        "--n_per_language",
        type=int,
        default=20,
        help="Number of selected samples per language",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducibility",
    )
    parser.add_argument(
        "--output_ids",
        required=True,
        help="Output TXT file with selected sample IDs",
    )
    parser.add_argument(
        "--output_report",
        required=True,
        help="Output JSON report with selected samples and scores",
    )
    args = parser.parse_args()

    detailed_eval_path = Path(args.detailed_eval)
    if not detailed_eval_path.exists():
        raise FileNotFoundError(f"Detailed evaluation file not found: {detailed_eval_path}")

    rows = load_jsonl(detailed_eval_path)
    grouped = language_breakdown(rows)

    required_langs = ["python", "javascript", "java"]
    for lang in required_langs:
        if lang not in grouped:
            raise ValueError(f"Language not found in evaluation file: {lang}")

    selected: Dict[str, List[Dict[str, Any]]] = {}
    for idx, lang in enumerate(required_langs):
        selected[lang] = stratified_sample(
            grouped[lang],
            n_total=args.n_per_language,
            seed=args.seed + idx,
        )

    output_ids = Path(args.output_ids)
    output_report = Path(args.output_report)
    output_ids.parent.mkdir(parents=True, exist_ok=True)
    output_report.parent.mkdir(parents=True, exist_ok=True)

    write_selected_ids(output_ids, selected)
    write_selection_report(output_report, selected)

    print(f"Wrote selected IDs: {output_ids}")
    print(f"Wrote selection report: {output_report}")
    print(f"Python: {len(selected['python'])}")
    print(f"JavaScript: {len(selected['javascript'])}")
    print(f"Java: {len(selected['java'])}")
    print(f"Total: {sum(len(v) for v in selected.values())}")


if __name__ == "__main__":
    main()