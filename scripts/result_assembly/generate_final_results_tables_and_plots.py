#!/usr/bin/env python3

import json
import re
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


BASE = Path("outputs/evaluation-and-correctness-may2026")
INPUT_FILE = BASE / "all_results_combined_full_merged.json"
OUT_DIR = BASE / "final-results-tables-and-plots"

PROMPT_ORDER = ["ZS", "OS", "FS"]


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]+", "_", str(text)).strip("_")


def extract_language(entry: dict) -> str:
    for block_name in ["lexical", "code_grounded"]:
        block = entry.get(block_name, {})
        per_lang = block.get("per_language", {})
        if per_lang:
            return list(per_lang.keys())[0]

    input_file = entry.get("input_file", "").lower()
    if "javascript" in input_file:
        return "javascript"
    if "python" in input_file:
        return "python"
    if "java" in input_file:
        return "java"
    return "unknown"


def extract_family(entry: dict) -> str:
    text = " ".join([
        entry.get("input_file", ""),
        entry.get("lexical_summary_file", ""),
        entry.get("code_grounded_summary_file", ""),
    ]).lower()

    model = str(entry.get("model_name", "")).lower()

    if "open-source-fine-tuned" in text or "lora" in model:
        return "open-source-fine-tuned"
    if "open-source" in text:
        return "open-source"
    if "commercial-new" in text:
        return "commercial-new"

    if any(x in model for x in ["gpt", "deepseek", "gemini"]):
        return "commercial-new"

    return "unknown"


def load_clean_dataframe() -> pd.DataFrame:
    with INPUT_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)

    rows = []

    for entry in data:
        input_file = entry.get("input_file", "")

        # Exclude smoke / test / partial runs
        if entry.get("num_samples") != 400:
            continue
        if "smoke" in input_file.lower():
            continue
        if "test" in input_file.lower():
            continue
        if "lexical" not in entry or "code_grounded" not in entry:
            continue

        lexical = entry["lexical"]
        code_grounded = entry["code_grounded"]

        rows.append({
            "family": extract_family(entry),
            "model": entry.get("model_name"),
            "language": extract_language(entry),
            "prompt": entry.get("prompt_template_id"),

            "num_samples": entry.get("num_samples"),

            "mean_latency_seconds": lexical.get("mean_latency_seconds"),
            "mean_generated_word_count": lexical.get("mean_generated_word_count"),

            "bleu": lexical.get("mean_bleu"),
            "rouge1": lexical.get("mean_rouge1_fmeasure"),
            "rouge2": lexical.get("mean_rouge2_fmeasure"),
            "rougeL": lexical.get("mean_rougeL_fmeasure"),
            "bertscore": lexical.get("mean_bertscore_f1"),

            "parameter_coverage": code_grounded.get("mean_parameter_coverage"),
            "return_coverage": code_grounded.get("mean_return_coverage"),
            "exception_coverage": code_grounded.get("mean_exception_coverage"),
            "omission_rate": code_grounded.get("mean_omission_rate"),
            "hallucination_sample_rate": code_grounded.get("hallucination_sample_rate"),
            "mean_hallucination_count": code_grounded.get("mean_hallucination_count"),

            "input_file": input_file,
            "lexical_summary_file": entry.get("lexical_summary_file"),
            "code_grounded_summary_file": entry.get("code_grounded_summary_file"),
        })

    df = pd.DataFrame(rows)

    if df.empty:
        raise RuntimeError("No valid 400-sample lexical + code-grounded records found.")

    df["prompt"] = pd.Categorical(df["prompt"], categories=PROMPT_ORDER, ordered=True)

    return df.sort_values(["language", "family", "model", "prompt"])


def save_tables(df: pd.DataFrame):
    tables_dir = OUT_DIR / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)

    # Full clean table
    df.to_csv(tables_dir / "clean_full_results.csv", index=False)

    # One table per language
    for language, sub in df.groupby("language", observed=True):
        sub.to_csv(tables_dir / f"{language}_full_comparison.csv", index=False)

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

    # Model-level averages
    model_avg = (
        df.groupby(["family", "model"], observed=True)[metric_cols]
        .mean()
        .reset_index()
        .sort_values(["family", "parameter_coverage"], ascending=[True, False])
    )
    model_avg.to_csv(tables_dir / "model_level_averages.csv", index=False)

    # Language-level averages
    language_avg = (
        df.groupby("language", observed=True)[metric_cols]
        .mean()
        .reset_index()
        .sort_values("parameter_coverage", ascending=False)
    )
    language_avg.to_csv(tables_dir / "language_level_averages.csv", index=False)

    # Prompt-level averages
    prompt_avg = (
        df.groupby("prompt", observed=True)[metric_cols]
        .mean()
        .reset_index()
    )
    prompt_avg.to_csv(tables_dir / "prompt_level_averages.csv", index=False)

    # Language + prompt averages
    lang_prompt_avg = (
        df.groupby(["language", "prompt"], observed=True)[metric_cols]
        .mean()
        .reset_index()
    )
    lang_prompt_avg.to_csv(tables_dir / "language_prompt_averages.csv", index=False)

    # Family + language + prompt averages
    family_lang_prompt_avg = (
        df.groupby(["family", "language", "prompt"], observed=True)[metric_cols]
        .mean()
        .reset_index()
    )
    family_lang_prompt_avg.to_csv(
        tables_dir / "family_language_prompt_averages.csv",
        index=False,
    )

    # Best models per language by parameter coverage
    best_by_language = (
        df.sort_values(["language", "parameter_coverage"], ascending=[True, False])
        .groupby("language", observed=True)
        .head(10)
    )
    best_by_language.to_csv(tables_dir / "top10_models_per_language_by_coverage.csv", index=False)

    # Thesis-ready rounded table
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
    ].to_csv(tables_dir / "thesis_ready_main_table.csv", index=False)

    return tables_dir


def plot_metric_by_prompt_per_language(df: pd.DataFrame, metric: str, ylabel: str):
    plots_dir = OUT_DIR / "plots" / "per_language_prompt_trends" / metric
    plots_dir.mkdir(parents=True, exist_ok=True)

    for language, lang_df in df.groupby("language", observed=True):
        plt.figure(figsize=(12, 7))

        for model, sub in lang_df.groupby("model", observed=True):
            sub = sub.sort_values("prompt")
            plt.plot(
                sub["prompt"].astype(str),
                sub[metric],
                marker="o",
                label=model,
            )

        plt.ylim(0, 1 if metric not in ["bleu", "rougeL"] else None)
        plt.xlabel("Prompt setting")
        plt.ylabel(ylabel)
        plt.title(f"{language.capitalize()} - {ylabel} across ZS / OS / FS")
        plt.grid(True, axis="y", alpha=0.3)
        plt.legend(fontsize=8, bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.tight_layout()

        plt.savefig(plots_dir / f"{language}_{metric}_prompt_trend.png", dpi=300)
        plt.close()


def plot_family_by_language_prompt(df: pd.DataFrame):
    plots_dir = OUT_DIR / "plots" / "family_language_prompt"
    plots_dir.mkdir(parents=True, exist_ok=True)

    metrics = [
        ("parameter_coverage", "Parameter Coverage"),
        ("return_coverage", "Return Coverage"),
        ("omission_rate", "Omission Rate"),
        ("bertscore", "BERTScore F1"),
        ("rougeL", "ROUGE-L"),
        ("bleu", "BLEU"),
    ]

    grouped = (
        df.groupby(["language", "family", "prompt"], observed=True)
        [[m[0] for m in metrics]]
        .mean()
        .reset_index()
    )

    for language, lang_df in grouped.groupby("language", observed=True):
        for metric, ylabel in metrics:
            plt.figure(figsize=(9, 6))

            for family, sub in lang_df.groupby("family", observed=True):
                sub = sub.sort_values("prompt")
                plt.plot(
                    sub["prompt"].astype(str),
                    sub[metric],
                    marker="o",
                    label=family,
                )

            plt.ylim(0, 1 if metric not in ["bleu", "rougeL"] else None)
            plt.xlabel("Prompt setting")
            plt.ylabel(ylabel)
            plt.title(f"{language.capitalize()} - {ylabel} by Model Family")
            plt.grid(True, axis="y", alpha=0.3)
            plt.legend()
            plt.tight_layout()

            plt.savefig(
                plots_dir / f"{language}_{metric}_by_family_prompt.png",
                dpi=300,
            )
            plt.close()


def plot_model_language_structural(df: pd.DataFrame):
    plots_dir = OUT_DIR / "plots" / "model_language_structural"
    plots_dir.mkdir(parents=True, exist_ok=True)

    for (model, language), sub in df.groupby(["model", "language"], observed=True):
        sub = sub.sort_values("prompt")

        plt.figure(figsize=(8, 5.5))
        plt.plot(
            sub["prompt"].astype(str),
            sub["parameter_coverage"],
            marker="o",
            label="Parameter coverage",
        )
        plt.plot(
            sub["prompt"].astype(str),
            sub["return_coverage"],
            marker="s",
            label="Return coverage",
        )
        plt.plot(
            sub["prompt"].astype(str),
            sub["omission_rate"],
            marker="^",
            linestyle="--",
            label="Omission rate",
        )

        plt.ylim(0, 1)
        plt.xlabel("Prompt setting")
        plt.ylabel("Metric value")
        plt.title(f"{model} - {language}: ZS / OS / FS structural comparison")
        plt.grid(True, axis="y", alpha=0.3)
        plt.legend()
        plt.tight_layout()

        plt.savefig(
            plots_dir / f"{safe_name(model)}_{language}_structural.png",
            dpi=300,
        )
        plt.close()


def plot_tradeoff_per_language(df: pd.DataFrame):
    plots_dir = OUT_DIR / "plots" / "tradeoff_plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    marker_map = {
        "ZS": "o",
        "OS": "s",
        "FS": "^",
    }

    for language, lang_df in df.groupby("language", observed=True):
        # Coverage vs BERTScore
        plt.figure(figsize=(10, 7))

        for family, family_df in lang_df.groupby("family", observed=True):
            for prompt in PROMPT_ORDER:
                sub = family_df[family_df["prompt"] == prompt]
                if sub.empty:
                    continue

                plt.scatter(
                    sub["parameter_coverage"],
                    sub["bertscore"],
                    marker=marker_map[prompt],
                    label=f"{family} - {prompt}",
                    alpha=0.8,
                )

                for _, row in sub.iterrows():
                    plt.annotate(
                        safe_name(row["model"])[:18],
                        (row["parameter_coverage"], row["bertscore"]),
                        fontsize=7,
                        alpha=0.75,
                    )

        plt.xlabel("Parameter Coverage")
        plt.ylabel("BERTScore F1")
        plt.title(f"{language.capitalize()} - Coverage vs Semantic Similarity")
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=8, bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.tight_layout()
        plt.savefig(plots_dir / f"{language}_coverage_vs_bertscore.png", dpi=300)
        plt.close()

        # Coverage vs Omission
        plt.figure(figsize=(10, 7))

        for family, family_df in lang_df.groupby("family", observed=True):
            for prompt in PROMPT_ORDER:
                sub = family_df[family_df["prompt"] == prompt]
                if sub.empty:
                    continue

                plt.scatter(
                    sub["parameter_coverage"],
                    sub["omission_rate"],
                    marker=marker_map[prompt],
                    label=f"{family} - {prompt}",
                    alpha=0.8,
                )

                for _, row in sub.iterrows():
                    plt.annotate(
                        safe_name(row["model"])[:18],
                        (row["parameter_coverage"], row["omission_rate"]),
                        fontsize=7,
                        alpha=0.75,
                    )

        plt.xlabel("Parameter Coverage")
        plt.ylabel("Omission Rate")
        plt.title(f"{language.capitalize()} - Coverage vs Omission")
        plt.grid(True, alpha=0.3)
        plt.legend(fontsize=8, bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.tight_layout()
        plt.savefig(plots_dir / f"{language}_coverage_vs_omission.png", dpi=300)
        plt.close()


def plot_model_level_rankings(df: pd.DataFrame):
    plots_dir = OUT_DIR / "plots" / "rankings"
    plots_dir.mkdir(parents=True, exist_ok=True)

    avg = (
        df.groupby(["family", "model"], observed=True)
        [
            [
                "bertscore",
                "parameter_coverage",
                "return_coverage",
                "omission_rate",
                "hallucination_sample_rate",
            ]
        ]
        .mean()
        .reset_index()
    )

    avg["model_label"] = avg["family"] + " / " + avg["model"]

    for metric, ylabel, ascending in [
        ("parameter_coverage", "Mean Parameter Coverage", False),
        ("return_coverage", "Mean Return Coverage", False),
        ("omission_rate", "Mean Omission Rate", True),
        ("hallucination_sample_rate", "Mean Hallucination Sample Rate", True),
        ("bertscore", "Mean BERTScore F1", False),
    ]:
        sub = avg.sort_values(metric, ascending=ascending)

        plt.figure(figsize=(11, 7))
        plt.barh(sub["model_label"], sub[metric])
        plt.xlabel(ylabel)
        plt.title(ylabel + " by Model")
        plt.grid(True, axis="x", alpha=0.3)
        plt.tight_layout()
        plt.savefig(plots_dir / f"ranking_{metric}.png", dpi=300)
        plt.close()


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_clean_dataframe()
    tables_dir = save_tables(df)

    plot_metric_by_prompt_per_language(df, "bleu", "BLEU")
    plot_metric_by_prompt_per_language(df, "rougeL", "ROUGE-L")
    plot_metric_by_prompt_per_language(df, "bertscore", "BERTScore F1")
    plot_metric_by_prompt_per_language(df, "parameter_coverage", "Parameter Coverage")
    plot_metric_by_prompt_per_language(df, "return_coverage", "Return Coverage")
    plot_metric_by_prompt_per_language(df, "omission_rate", "Omission Rate")

    plot_family_by_language_prompt(df)
    plot_model_language_structural(df)
    plot_tradeoff_per_language(df)
    plot_model_level_rankings(df)

    print("Done.")
    print(f"Input: {INPUT_FILE}")
    print(f"Output folder: {OUT_DIR}")
    print(f"Tables: {tables_dir}")
    print(f"Clean records used: {len(df)}")


if __name__ == "__main__":
    main()