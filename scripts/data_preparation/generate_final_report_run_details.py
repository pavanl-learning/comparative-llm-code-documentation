#!/usr/bin/env python3
"""Generate report-ready run details from segregated result indexes."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_DIR = REPO_ROOT / "outputs" / "segregated_results" / "index"
SEGREGATED_INDEX = INDEX_DIR / "segregated_results_index.csv"
OUTPUT_MD = INDEX_DIR / "final_report_run_details.md"
OUTPUT_CSV = INDEX_DIR / "final_report_run_details.csv"

LANGUAGES = ("python", "java", "javascript")
PROMPTS = ("zero_shot", "one_shot", "few_shot")

CORE_MODELS = {
    "open-source-base": [
        "codegemma_2b",
        "gemma_2_2b_it",
        "qwen25_1_5b_instruct",
        "qwen25_coder_1_5b_instruct",
    ],
    "open-source-lora": [
        "codegemma_2b_lora_multilang",
        "gemma_2_2b_it_lora_multilang",
        "qwen25_1_5b_instruct_lora_multilang",
        "qwen25_coder_1_5b_instruct_lora_multilang",
    ],
    "commercial-base": [
        "deepseek_chat",
        "gemini_3_flash_preview",
        "gpt_5_1",
        "gpt_5_1_codex",
    ],
}

PRESERVED_PARTIAL_MODELS = {
    "commercial-base": [
        "deepseek_reasoner",
        "gpt_5_3_codex",
        "gpt_5_4",
    ],
}


def load_index() -> list[dict[str, str]]:
    with SEGREGATED_INDEX.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    return [
        row
        for row in rows
        if (REPO_ROOT / row["destination_path"]).exists()
    ]


def language_matches(path: str, language: str) -> bool:
    filename = Path(path).name.lower()
    return re.search(rf"(^|_){re.escape(language)}(_|\.|$)", filename) is not None


def artifact_type(source_path: str) -> str:
    source = source_path.lower()
    filename = Path(source).name

    if "/raw_generations/" in source:
        return "raw_generation"
    if "/correctness/" in source or "code_grounded" in source or "correctness" in filename:
        return "correctness"
    if "/evaluations/" in source or "/evaluation-and-correctness-may2026/" in source:
        return "automatic_metrics"
    return "other"


def matches_combo(
    row: dict[str, str],
    category: str,
    model: str,
    prompt: str,
    language: str,
) -> bool:
    source = row["source_path"].lower()
    filename = Path(source).name.lower()
    if "smoke" in filename or "test" in filename:
        return False
    return (
        row["category"] == category
        and model.lower() in source
        and prompt in source
        and "400" in source
        and language_matches(source, language)
    )


def build_combo_rows(index_rows: list[dict[str, str]]) -> list[dict[str, str | int | bool]]:
    rows: list[dict[str, str | int | bool]] = []

    for category, models in CORE_MODELS.items():
        for model in models:
            for prompt in PROMPTS:
                for language in LANGUAGES:
                    matches = [
                        row
                        for row in index_rows
                        if matches_combo(row, category, model, prompt, language)
                    ]
                    by_type: dict[str, list[dict[str, str]]] = defaultdict(list)
                    for row in matches:
                        by_type[artifact_type(row["source_path"])].append(row)

                    raw_files = by_type["raw_generation"]
                    metric_files = by_type["automatic_metrics"]
                    correctness_files = by_type["correctness"]

                    rows.append(
                        {
                            "run_group": "core_400_report_run",
                            "category": category,
                            "model": model,
                            "prompt_setting": prompt,
                            "language": language,
                            "raw_generation_files": len(raw_files),
                            "automatic_metric_files": len(metric_files),
                            "correctness_files": len(correctness_files),
                            "raw_present": bool(raw_files),
                            "metrics_present": bool(metric_files),
                            "correctness_present": bool(correctness_files),
                            "complete_raw_metrics_correctness": bool(
                                raw_files and metric_files and correctness_files
                            ),
                            "raw_paths": " | ".join(row["destination_path"] for row in raw_files),
                            "metric_paths": " | ".join(row["destination_path"] for row in metric_files),
                            "correctness_paths": " | ".join(
                                row["destination_path"] for row in correctness_files
                            ),
                        }
                    )

    for category, models in PRESERVED_PARTIAL_MODELS.items():
        for model in models:
            for prompt in PROMPTS:
                for language in LANGUAGES:
                    matches = [
                        row
                        for row in index_rows
                        if matches_combo(row, category, model, prompt, language)
                    ]
                    if not matches:
                        continue
                    by_type: dict[str, list[dict[str, str]]] = defaultdict(list)
                    for row in matches:
                        by_type[artifact_type(row["source_path"])].append(row)

                    rows.append(
                        {
                            "run_group": "preserved_partial_or_legacy_400_run",
                            "category": category,
                            "model": model,
                            "prompt_setting": prompt,
                            "language": language,
                            "raw_generation_files": len(by_type["raw_generation"]),
                            "automatic_metric_files": len(by_type["automatic_metrics"]),
                            "correctness_files": len(by_type["correctness"]),
                            "raw_present": bool(by_type["raw_generation"]),
                            "metrics_present": bool(by_type["automatic_metrics"]),
                            "correctness_present": bool(by_type["correctness"]),
                            "complete_raw_metrics_correctness": bool(
                                by_type["raw_generation"]
                                and by_type["automatic_metrics"]
                                and by_type["correctness"]
                            ),
                            "raw_paths": " | ".join(
                                row["destination_path"] for row in by_type["raw_generation"]
                            ),
                            "metric_paths": " | ".join(
                                row["destination_path"] for row in by_type["automatic_metrics"]
                            ),
                            "correctness_paths": " | ".join(
                                row["destination_path"] for row in by_type["correctness"]
                            ),
                        }
                    )

    return rows


def write_csv(rows: list[dict[str, str | int | bool]]) -> None:
    fieldnames = [
        "run_group",
        "category",
        "model",
        "prompt_setting",
        "language",
        "raw_generation_files",
        "automatic_metric_files",
        "correctness_files",
        "raw_present",
        "metrics_present",
        "correctness_present",
        "complete_raw_metrics_correctness",
        "raw_paths",
        "metric_paths",
        "correctness_paths",
    ]
    with OUTPUT_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def model_summary(rows: list[dict[str, str | int | bool]]) -> list[dict[str, str | int]]:
    grouped: dict[tuple[str, str, str], list[dict[str, str | int | bool]]] = defaultdict(list)
    for row in rows:
        grouped[
            (
                str(row["run_group"]),
                str(row["category"]),
                str(row["model"]),
            )
        ].append(row)

    summary_rows: list[dict[str, str | int]] = []
    for (run_group, category, model), model_rows in sorted(grouped.items()):
        summary_rows.append(
            {
                "run_group": run_group,
                "category": category,
                "model": model,
                "combinations_listed": len(model_rows),
                "raw_present": sum(bool(row["raw_present"]) for row in model_rows),
                "metrics_present": sum(bool(row["metrics_present"]) for row in model_rows),
                "correctness_present": sum(
                    bool(row["correctness_present"]) for row in model_rows
                ),
                "complete_raw_metrics_correctness": sum(
                    bool(row["complete_raw_metrics_correctness"])
                    for row in model_rows
                ),
            }
        )

    return summary_rows


def write_markdown(
    index_rows: list[dict[str, str]],
    rows: list[dict[str, str | int | bool]],
) -> None:
    category_counts = Counter(row["category"] for row in index_rows)
    summaries = model_summary(rows)
    gaps = [
        row
        for row in rows
        if row["run_group"] == "core_400_report_run"
        and not row["complete_raw_metrics_correctness"]
    ]

    lines: list[str] = []
    lines.append("# Final Report Run Details Manifest")
    lines.append("")
    lines.append("This manifest is generated from `outputs/segregated_results/index/segregated_results_index.csv` and only counts files whose copied destination exists.")
    lines.append("")
    lines.append("## Organized Result Folders")
    lines.append("")
    lines.append("- `outputs/segregated_results/open-source-base/`: open-source pretrained/base model runs")
    lines.append("- `outputs/segregated_results/open-source-lora/`: open-source LoRA/fine-tuned model runs")
    lines.append("- `outputs/segregated_results/commercial-base/`: commercial model runs")
    lines.append("- `outputs/segregated_results/shared-aggregate/`: shared tables, plots, human-eval, and mixed-family aggregate files")
    lines.append("- `outputs/segregated_results/index/`: file indexes and verification reports")
    lines.append("")
    lines.append("## File Counts")
    lines.append("")
    lines.append("| Category | Files |")
    lines.append("|---|---:|")
    for category in sorted(category_counts):
        lines.append(f"| {category} | {category_counts[category]} |")
    lines.append(f"| **Total** | **{len(index_rows)}** |")
    lines.append("")
    lines.append("## Core 400-Sample Run Coverage")
    lines.append("")
    lines.append("Each core model should have 9 combinations: 3 languages (`python`, `java`, `javascript`) x 3 prompt settings (`zero_shot`, `one_shot`, `few_shot`).")
    lines.append("")
    lines.append("| Category | Model | Listed combos | Raw present | Metrics present | Correctness present | Complete raw+metrics+correctness |")
    lines.append("|---|---|---:|---:|---:|---:|---:|")
    for summary in summaries:
        if summary["run_group"] != "core_400_report_run":
            continue
        lines.append(
            "| {category} | {model} | {combinations_listed} | {raw_present} | {metrics_present} | {correctness_present} | {complete_raw_metrics_correctness} |".format(
                **summary
            )
        )
    lines.append("")
    lines.append("## Core 400-Sample Downstream Gaps")
    lines.append("")
    if gaps:
        lines.append("The raw generation files exist for all core 400-sample runs. The following rows identify downstream metric/correctness artifacts that were not present in the source outputs and therefore could not be copied.")
        lines.append("")
        lines.append("| Category | Model | Prompt | Language | Raw files | Metric files | Correctness files |")
        lines.append("|---|---|---|---|---:|---:|---:|")
        for row in gaps:
            lines.append(
                f"| {row['category']} | {row['model']} | {row['prompt_setting']} | {row['language']} | {row['raw_generation_files']} | {row['automatic_metric_files']} | {row['correctness_files']} |"
            )
    else:
        lines.append("No downstream gaps found for core 400-sample runs.")
    lines.append("")
    lines.append("## Preserved Partial Or Legacy Commercial 400-Sample Runs")
    lines.append("")
    partial = [
        summary
        for summary in summaries
        if summary["run_group"] == "preserved_partial_or_legacy_400_run"
    ]
    if partial:
        lines.append("| Category | Model | Listed combos | Raw present | Metrics present | Correctness present | Complete raw+metrics+correctness |")
        lines.append("|---|---|---:|---:|---:|---:|---:|")
        for summary in partial:
            lines.append(
                "| {category} | {model} | {combinations_listed} | {raw_present} | {metrics_present} | {correctness_present} | {complete_raw_metrics_correctness} |".format(
                    **summary
                )
            )
    else:
        lines.append("No partial legacy commercial 400-sample runs were listed.")
    lines.append("")
    lines.append("## Companion Files")
    lines.append("")
    lines.append("- `final_report_run_details.csv`: per-combination file counts and copied destination paths")
    lines.append("- `segregated_results_index.csv`: complete file-level source-to-destination index")
    lines.append("- `main_400_core_run_presence.csv`: compact core 400-sample presence report")
    lines.append("- `main_400_artifact_verification_from_index.csv`: detailed artifact verification from copied destination index")
    lines.append("")

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    index_rows = load_index()
    combo_rows = build_combo_rows(index_rows)
    write_csv(combo_rows)
    write_markdown(index_rows, combo_rows)
    print(f"Wrote {OUTPUT_MD.relative_to(REPO_ROOT).as_posix()}")
    print(f"Wrote {OUTPUT_CSV.relative_to(REPO_ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
