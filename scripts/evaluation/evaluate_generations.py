#!/usr/bin/env python3

import argparse
import json
import statistics
from collections import defaultdict
from pathlib import Path

from rouge_score import rouge_scorer
from bert_score import score as bertscore_score
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def safe_text(x):
    if x is None:
        return ""
    return " ".join(str(x).split()).strip()


def normalized_text(x):
    if x is None:
        return ""
    return " ".join(str(x).strip().lower().split())


def compute_bleu(reference: str, prediction: str) -> float:
    reference = safe_text(reference)
    prediction = safe_text(prediction)

    if not reference or not prediction:
        return 0.0

    ref_tokens = reference.split()
    pred_tokens = prediction.split()

    if not ref_tokens or not pred_tokens:
        return 0.0

    smoothie = SmoothingFunction().method1
    return float(
        sentence_bleu(
            [ref_tokens],
            pred_tokens,
            smoothing_function=smoothie,
        )
    )


def summarize_rows(rows):
    valid_berts = [r["bertscore_f1"] for r in rows if r["bertscore_f1"] is not None]
    valid_latencies = [r["latency_seconds"] for r in rows if r["latency_seconds"] is not None]

    return {
        "num_samples": len(rows),
        "mean_latency_seconds": statistics.mean(valid_latencies) if valid_latencies else None,
        "mean_generated_word_count": statistics.mean(r["generated_word_count"] for r in rows) if rows else None,
        "exact_match_accuracy": statistics.mean(r["exact_match"] for r in rows) if rows else None,
        "normalized_exact_match_accuracy": statistics.mean(r["normalized_exact_match"] for r in rows) if rows else None,
        "mean_bleu": statistics.mean(r["bleu"] for r in rows) if rows else None,
        "mean_rouge1_fmeasure": statistics.mean(r["rouge1_fmeasure"] for r in rows) if rows else None,
        "mean_rouge2_fmeasure": statistics.mean(r["rouge2_fmeasure"] for r in rows) if rows else None,
        "mean_rougeL_fmeasure": statistics.mean(r["rougeL_fmeasure"] for r in rows) if rows else None,
        "mean_bertscore_f1": statistics.mean(valid_berts) if valid_berts else None,
        "num_bertscore_skipped": sum(1 for r in rows if r["bertscore_skipped"]),
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate generated documentation.")
    parser.add_argument("--input", required=True, help="Input generations JSONL")
    parser.add_argument("--output-prefix", required=True, help="Prefix for detailed and summary outputs")
    return parser.parse_args()


def main():
    args = parse_args()

    input_file = Path(args.input)
    output_prefix = Path(args.output_prefix)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    detailed_out = Path(str(output_prefix) + "_detailed.jsonl")
    summary_out = Path(str(output_prefix) + "_summary.json")

    detailed_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.parent.mkdir(parents=True, exist_ok=True)

    rows = load_jsonl(input_file)
    if not rows:
        raise ValueError(f"No rows found in {input_file}")

    scorer = rouge_scorer.RougeScorer(
        ["rouge1", "rouge2", "rougeL"],
        use_stemmer=True
    )

    detailed_rows = []
    bert_predictions = []
    bert_references = []
    bert_row_indices = []

    for i, row in enumerate(rows):
        ref = safe_text(row.get("reference_documentation", ""))
        pred = safe_text(row.get("generated_documentation", ""))

        exact_match = 1 if pred == ref else 0
        normalized_exact_match = 1 if normalized_text(pred) == normalized_text(ref) else 0
        bleu = compute_bleu(ref, pred)

        rouge = scorer.score(ref, pred)

        out_row = {
            "sample_id": row["sample_id"],
            "language": row["language"],
            "model_name": row["model_name"],
            "prompt_template_id": row["prompt_template_id"],
            "latency_seconds": row.get("latency_seconds"),
            "reference_documentation": ref,
            "generated_documentation": pred,
            "generated_char_length": len(pred),
            "generated_word_count": len(pred.split()),
            "exact_match": exact_match,
            "normalized_exact_match": normalized_exact_match,
            "bleu": bleu,
            "rouge1_fmeasure": rouge["rouge1"].fmeasure,
            "rouge2_fmeasure": rouge["rouge2"].fmeasure,
            "rougeL_fmeasure": rouge["rougeL"].fmeasure,
            "bertscore_precision": None,
            "bertscore_recall": None,
            "bertscore_f1": None,
            "bertscore_skipped": False,
        }

        if pred and ref:
            bert_predictions.append(pred)
            bert_references.append(ref)
            bert_row_indices.append(i)
        else:
            out_row["bertscore_skipped"] = True

        detailed_rows.append(out_row)

    if bert_predictions:
        print("Computing BERTScore...")
        P, R, F1 = bertscore_score(
            bert_predictions,
            bert_references,
            lang="en",
            verbose=True
        )

        for pos, row_idx in enumerate(bert_row_indices):
            detailed_rows[row_idx]["bertscore_precision"] = float(P[pos])
            detailed_rows[row_idx]["bertscore_recall"] = float(R[pos])
            detailed_rows[row_idx]["bertscore_f1"] = float(F1[pos])

    overall_summary = summarize_rows(detailed_rows)

    grouped = defaultdict(list)
    for row in detailed_rows:
        grouped[row["language"]].append(row)

    per_language = {
        lang: summarize_rows(lang_rows)
        for lang, lang_rows in sorted(grouped.items())
    }

    summary = {
        "input_file": str(input_file),
        "num_samples": len(detailed_rows),
        "model_name": detailed_rows[0]["model_name"],
        "prompt_template_id": detailed_rows[0]["prompt_template_id"],
        **overall_summary,
        "per_language": per_language,
    }

    # Always overwrite on rerun
    with detailed_out.open("w", encoding="utf-8") as f:
        for row in detailed_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    with summary_out.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Wrote {detailed_out}")
    print(f"Wrote {summary_out}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()