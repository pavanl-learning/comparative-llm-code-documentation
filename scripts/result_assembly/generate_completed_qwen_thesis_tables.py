#!/usr/bin/env python3
"""Build report-ready thesis tables from the verified run-details manifest."""

from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[1]
MANIFEST = REPO_ROOT / "outputs" / "segregated_results" / "index" / "final_report_run_details.csv"
OUT_DIR = REPO_ROOT / "outputs" / "final_results" / "thesis_tables_completed_qwen"

PROMPT_LABELS = {
    "zero_shot": "ZS",
    "one_shot": "OS",
    "few_shot": "FS",
}

FAMILY_LABELS = {
    "open-source-base": "open-source",
    "open-source-lora": "open-source-fine-tuned",
    "commercial-base": "commercial-new",
}

MODEL_LABELS = {
    "codegemma_2b": "google/codegemma-2b",
    "gemma_2_2b_it": "google/gemma-2-2b-it",
    "qwen25_1_5b_instruct": "Qwen/Qwen2.5-1.5B-Instruct",
    "qwen25_coder_1_5b_instruct": "Qwen/Qwen2.5-Coder-1.5B-Instruct",
    "deepseek_chat": "deepseek-chat",
    "gemini_3_flash_preview": "gemini-3-flash-preview",
    "gpt_5_1": "gpt-5.1",
    "gpt_5_1_codex": "gpt-5.1-codex",
    "codegemma_2b_lora_multilang": "codegemma_2b_lora_multilang",
    "gemma_2_2b_it_lora_multilang": "gemma_2_2b_it_lora_multilang",
    "qwen25_1_5b_instruct_lora_multilang": "qwen25_1_5b_instruct_lora_multilang",
    "qwen25_coder_1_5b_instruct_lora_multilang": "qwen25_coder_1_5b_instruct_lora_multilang",
}


def first_summary_path(paths: str) -> Path | None:
    candidates = []
    for raw_path in str(paths or "").split("|"):
        path = raw_path.strip()
        if path.endswith("_summary.json"):
            full = REPO_ROOT / path
            if full.exists():
                candidates.append(full)
    non_smoke = [
        path
        for path in candidates
        if "smoke" not in path.name.lower() and "test" not in path.name.lower()
    ]
    preferred = non_smoke or candidates
    for path in preferred:
        try:
            summary = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if summary.get("num_samples") == 400:
            return path
    return (preferred or [None])[0]


def load_json(path: Path | None) -> dict:
    if path is None:
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def build_clean_dataframe() -> pd.DataFrame:
    manifest = pd.read_csv(MANIFEST)
    manifest = manifest[
        (manifest["run_group"] == "core_400_report_run")
        & (manifest["complete_raw_metrics_correctness"] == True)
    ].copy()

    rows = []
    for _, row in manifest.iterrows():
        lexical_path = first_summary_path(row["metric_paths"])
        correctness_path = first_summary_path(row["correctness_paths"])
        lexical = load_json(lexical_path)
        correctness = load_json(correctness_path)

        rows.append(
            {
                "family": FAMILY_LABELS.get(row["category"], row["category"]),
                "model": MODEL_LABELS.get(row["model"], row["model"]),
                "language": row["language"],
                "prompt": PROMPT_LABELS.get(row["prompt_setting"], row["prompt_setting"]),
                "num_samples": lexical.get("num_samples") or correctness.get("num_samples"),
                "mean_latency_seconds": lexical.get("mean_latency_seconds"),
                "mean_generated_word_count": lexical.get("mean_generated_word_count"),
                "bleu": lexical.get("mean_bleu"),
                "rouge1": lexical.get("mean_rouge1_fmeasure"),
                "rouge2": lexical.get("mean_rouge2_fmeasure"),
                "rougeL": lexical.get("mean_rougeL_fmeasure"),
                "bertscore": lexical.get("mean_bertscore_f1"),
                "parameter_coverage": correctness.get("mean_parameter_coverage"),
                "return_coverage": correctness.get("mean_return_coverage"),
                "exception_coverage": correctness.get("mean_exception_coverage"),
                "omission_rate": correctness.get("mean_omission_rate"),
                "hallucination_sample_rate": correctness.get("hallucination_sample_rate"),
                "mean_hallucination_count": correctness.get("mean_hallucination_count"),
                "input_file": row["raw_paths"].split("|")[0].strip(),
                "lexical_summary_file": str(lexical_path.relative_to(REPO_ROOT)) if lexical_path else "",
                "code_grounded_summary_file": str(correctness_path.relative_to(REPO_ROOT)) if correctness_path else "",
            }
        )

    df = pd.DataFrame(rows)
    prompt_order = ["ZS", "OS", "FS"]
    df["prompt"] = pd.Categorical(df["prompt"], categories=prompt_order, ordered=True)
    return df.sort_values(["language", "family", "model", "prompt"]).reset_index(drop=True)


def save_tables(df: pd.DataFrame) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_DIR / "clean_full_results.csv", index=False)

    for language, sub in df.groupby("language", observed=True):
        sub.to_csv(OUT_DIR / f"{language}_full_comparison.csv", index=False)

    metric_cols = [
        "bleu",
        "rougeL",
        "bertscore",
        "parameter_coverage",
        "return_coverage",
        "exception_coverage",
        "omission_rate",
        "hallucination_sample_rate",
    ]

    df.groupby(["family", "model"], observed=True)[metric_cols].mean().reset_index().to_csv(
        OUT_DIR / "model_level_averages.csv", index=False
    )
    df.groupby("language", observed=True)[metric_cols].mean().reset_index().to_csv(
        OUT_DIR / "language_level_averages.csv", index=False
    )
    df.groupby("prompt", observed=True)[metric_cols].mean().reset_index().to_csv(
        OUT_DIR / "prompt_level_averages.csv", index=False
    )
    df.groupby(["language", "prompt"], observed=True)[metric_cols].mean().reset_index().to_csv(
        OUT_DIR / "language_prompt_averages.csv", index=False
    )
    df.groupby(["family", "language", "prompt"], observed=True)[metric_cols].mean().reset_index().to_csv(
        OUT_DIR / "family_language_prompt_averages.csv", index=False
    )

    rounded = df.copy()
    for col in metric_cols:
        rounded[col] = rounded[col].round(4)
    rounded[
        [
            "family",
            "model",
            "language",
            "prompt",
            "bleu",
            "rougeL",
            "bertscore",
            "parameter_coverage",
            "return_coverage",
            "exception_coverage",
            "omission_rate",
            "hallucination_sample_rate",
        ]
    ].to_csv(OUT_DIR / "thesis_ready_main_table.csv", index=False)

    top10 = (
        df.sort_values(["language", "parameter_coverage"], ascending=[True, False])
        .groupby("language", observed=True)
        .head(10)
    )
    top10.to_csv(OUT_DIR / "top10_models_per_language_by_coverage.csv", index=False)

    (OUT_DIR / "final_report_run_details.md").write_text(
        (REPO_ROOT / "outputs" / "segregated_results" / "index" / "final_report_run_details.md").read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )


def main() -> int:
    df = build_clean_dataframe()
    save_tables(df)
    print(f"Wrote completed Qwen thesis tables to {OUT_DIR.relative_to(REPO_ROOT)}")
    print(f"Rows: {len(df)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
