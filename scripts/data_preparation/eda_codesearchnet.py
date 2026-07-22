#!/usr/bin/env python
"""
Exploratory Data Analysis for CodeSearchNet-style code documentation records.

This script performs implementation-focused EDA for a thesis pipeline on
function-level code documentation generation.

It supports JSONL and CSV input files with flexible column names.

Expected logical fields:
- language
- code / function / func_code
- reference_doc / docstring / documentation / doc
- split

Outputs:
- EDA summary CSV files
- EDA figures
- Markdown EDA report

Example:
python scripts/eda_codesearchnet.py ^
  --input data/processed/codesearchnet_cleaned.jsonl ^
  --output-dir results/eda ^
  --figures-dir figures/eda
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

import pandas as pd
import matplotlib.pyplot as plt


LANGUAGE_COL_CANDIDATES = ["language", "lang", "programming_language"]
CODE_COL_CANDIDATES = ["code", "function", "func_code", "source_code", "code_tokens"]
DOC_COL_CANDIDATES = [
    "reference_documentation",
    "reference_doc",
    "docstring",
    "documentation",
    "doc",
    "docstring_summary",
    "target",
    "summary",
]
SPLIT_COL_CANDIDATES = [
    "split_name",
    "split",
    "partition",
    "dataset_split",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run EDA on CodeSearchNet-style code documentation records."
    )
    parser.add_argument(
        "--input",
        required=True,
        help="Input JSONL or CSV file containing CodeSearchNet-style records.",
    )
    parser.add_argument(
        "--output-dir",
        default="results/eda",
        help="Directory for EDA CSV and Markdown outputs.",
    )
    parser.add_argument(
        "--figures-dir",
        default="figures/eda",
        help="Directory for EDA plots.",
    )
    parser.add_argument(
        "--languages",
        nargs="*",
        default=["python", "javascript", "java"],
        help="Languages to include in the EDA. Default: python javascript java.",
    )
    parser.add_argument(
        "--max-code-chars",
        type=int,
        default=6000,
        help="Diagnostic threshold for long source-code records.",
    )
    parser.add_argument(
        "--min-doc-words",
        type=int,
        default=3,
        help="Diagnostic threshold for very short documentation.",
    )
    parser.add_argument(
        "--sample-sizes",
        nargs="*",
        type=int,
        default=[100, 200, 400, 800, 1000, 1200],
        help="Candidate balanced sample sizes to check per language.",
    )
    return parser.parse_args()


def load_records(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    suffix = path.suffix.lower()

    if suffix == ".jsonl":
        rows: List[dict] = []
        with path.open("r", encoding="utf-8") as f:
            for line_no, line in enumerate(f, start=1):
                line = line.strip()
                if not line:
                    continue
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError as exc:
                    raise ValueError(
                        f"Invalid JSON on line {line_no} in {path}: {exc}"
                    ) from exc
        return pd.DataFrame(rows)

    if suffix == ".csv":
        return pd.read_csv(path)

    raise ValueError("Input must be a .jsonl or .csv file")


def first_existing_column(df: pd.DataFrame, candidates: List[str]) -> Optional[str]:
    lower_to_original = {col.lower(): col for col in df.columns}
    for candidate in candidates:
        if candidate.lower() in lower_to_original:
            return lower_to_original[candidate.lower()]
    return None


def normalise_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        value = " ".join(str(v) for v in value)
    text = str(value)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def stable_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def count_words(text: str) -> int:
    if not text:
        return 0
    return len(re.findall(r"\S+", text))


def count_lines(text: str) -> int:
    if not text:
        return 0
    return len(text.splitlines())


def count_parameters(code: str, language: str) -> int:
    """
    Lightweight parameter-count heuristic.
    This is not a full parser, but it is sufficient for EDA diagnostics.
    Full correctness evaluation can use stronger language-specific logic.
    """
    if not code:
        return 0

    language = (language or "").lower()
    compact = re.sub(r"\s+", " ", code)

    patterns = []

    if language == "python":
        patterns = [
            r"def\s+\w+\s*\((.*?)\)\s*:",
            r"async\s+def\s+\w+\s*\((.*?)\)\s*:",
        ]
    elif language in {"javascript", "js"}:
        patterns = [
            r"function\s+\w+\s*\((.*?)\)",
            r"\w+\s*=\s*function\s*\((.*?)\)",
            r"\((.*?)\)\s*=>",
            r"([A-Za-z_$][\w$]*)\s*=>",
        ]
    elif language == "java":
        patterns = [
            r"(?:public|private|protected|static|final|synchronized|\s)+[\w<>\[\], ?]+\s+\w+\s*\((.*?)\)",
        ]
    else:
        patterns = [r"\w+\s*\((.*?)\)"]

    for pattern in patterns:
        match = re.search(pattern, compact)
        if not match:
            continue

        params = match.group(1).strip()

        if not params:
            return 0

        if language in {"javascript", "js"} and re.match(r"^[A-Za-z_$][\w$]*$", params):
            return 1

        parts = [p.strip() for p in params.split(",") if p.strip()]
        cleaned = [
            p
            for p in parts
            if p not in {"self", "cls"}
            and not p.startswith("*")
            and p.lower() not in {"void"}
        ]
        return len(cleaned)

    return 0


def has_return_statement(code: str, language: str) -> bool:
    if not code:
        return False
    return bool(re.search(r"\breturn\b", code))


def ensure_columns(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, str]]:
    language_col = first_existing_column(df, LANGUAGE_COL_CANDIDATES)
    code_col = first_existing_column(df, CODE_COL_CANDIDATES)
    doc_col = first_existing_column(df, DOC_COL_CANDIDATES)
    split_col = first_existing_column(df, SPLIT_COL_CANDIDATES)

    missing = []
    if language_col is None:
        missing.append("language")
    if code_col is None:
        missing.append("code")
    if doc_col is None:
        missing.append("reference documentation")

    if missing:
        raise ValueError(
            "Required logical columns missing: "
            + ", ".join(missing)
            + f". Available columns: {list(df.columns)}"
        )

    mapped = pd.DataFrame()
    mapped["language"] = df[language_col].apply(normalise_text).str.lower()
    mapped["code"] = df[code_col].apply(normalise_text)
    mapped["reference_doc"] = df[doc_col].apply(normalise_text)

    if split_col is not None:
        mapped["split"] = df[split_col].apply(normalise_text).str.lower()
    else:
        mapped["split"] = "unknown"

    if "sample_id" in df.columns:
        mapped["sample_id"] = df["sample_id"].apply(normalise_text)
    else:
        mapped["sample_id"] = [
            f"sample_{idx:08d}" for idx in range(1, len(mapped) + 1)
        ]

    column_map = {
        "language": language_col,
        "code": code_col,
        "reference_doc": doc_col,
        "split": split_col or "<not available>",
    }

    return mapped, column_map


def add_diagnostic_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    out["code_chars"] = out["code"].str.len()
    out["doc_chars"] = out["reference_doc"].str.len()
    out["code_words"] = out["code"].apply(count_words)
    out["doc_words"] = out["reference_doc"].apply(count_words)
    out["code_lines"] = out["code"].apply(count_lines)
    out["doc_lines"] = out["reference_doc"].apply(count_lines)

    out["code_hash"] = out["code"].apply(stable_hash)
    out["doc_hash"] = out["reference_doc"].apply(stable_hash)
    out["code_doc_hash"] = (out["code"] + " ||| " + out["reference_doc"]).apply(stable_hash)

    out["is_missing_code"] = out["code"].eq("")
    out["is_missing_doc"] = out["reference_doc"].eq("")
    out["parameter_count"] = out.apply(
        lambda row: count_parameters(row["code"], row["language"]), axis=1
    )
    out["has_return_statement"] = out.apply(
        lambda row: has_return_statement(row["code"], row["language"]), axis=1
    )

    return out


def save_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def plot_bar(df: pd.DataFrame, x: str, y: str, path: Path, xlabel: str, ylabel: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df[x].astype(str), df[y])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=30)
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=300)
    plt.close(fig)


def plot_hist_by_language(
    df: pd.DataFrame,
    value_col: str,
    path: Path,
    xlabel: str,
    ylabel: str,
    max_value: Optional[int] = None,
) -> None:
    fig, ax = plt.subplots(figsize=(8, 5))

    for language, group in df.groupby("language"):
        values = group[value_col].dropna()
        if max_value is not None:
            values = values[values <= max_value]
        if len(values) == 0:
            continue
        ax.hist(values, bins=40, alpha=0.45, label=language)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.legend()
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=300)
    plt.close(fig)


def compute_language_split_counts(df: pd.DataFrame) -> pd.DataFrame:
    counts = (
        df.groupby(["language", "split"])
        .size()
        .reset_index(name="record_count")
        .sort_values(["language", "split"])
    )
    return counts


def compute_length_statistics(df: pd.DataFrame) -> pd.DataFrame:
    stats = (
        df.groupby("language")
        .agg(
            records=("sample_id", "count"),
            code_chars_mean=("code_chars", "mean"),
            code_chars_median=("code_chars", "median"),
            code_chars_p95=("code_chars", lambda x: x.quantile(0.95)),
            code_words_mean=("code_words", "mean"),
            code_lines_mean=("code_lines", "mean"),
            doc_words_mean=("doc_words", "mean"),
            doc_words_median=("doc_words", "median"),
            doc_words_p95=("doc_words", lambda x: x.quantile(0.95)),
            doc_lines_mean=("doc_lines", "mean"),
        )
        .reset_index()
    )

    numeric_cols = [col for col in stats.columns if col != "language"]
    stats[numeric_cols] = stats[numeric_cols].round(3)
    return stats


def compute_missing_duplicate_summary(df: pd.DataFrame, min_doc_words: int) -> pd.DataFrame:
    rows = []

    for language, group in df.groupby("language"):
        duplicate_code = group["code_hash"].duplicated().sum()
        duplicate_doc = group["doc_hash"].duplicated().sum()
        duplicate_pair = group["code_doc_hash"].duplicated().sum()

        rows.append(
            {
                "language": language,
                "records": len(group),
                "missing_code": int(group["is_missing_code"].sum()),
                "missing_doc": int(group["is_missing_doc"].sum()),
                "very_short_doc": int((group["doc_words"] < min_doc_words).sum()),
                "duplicate_code": int(duplicate_code),
                "duplicate_doc": int(duplicate_doc),
                "duplicate_code_doc_pair": int(duplicate_pair),
            }
        )

    return pd.DataFrame(rows)


def compute_structure_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("language")
        .agg(
            records=("sample_id", "count"),
            avg_parameter_count=("parameter_count", "mean"),
            median_parameter_count=("parameter_count", "median"),
            records_with_parameters=("parameter_count", lambda x: int((x > 0).sum())),
            records_with_return=("has_return_statement", lambda x: int(x.sum())),
        )
        .reset_index()
    )

    summary["parameter_record_rate"] = (
        summary["records_with_parameters"] / summary["records"]
    ).round(4)
    summary["return_record_rate"] = (
        summary["records_with_return"] / summary["records"]
    ).round(4)

    numeric_cols = [
        "avg_parameter_count",
        "median_parameter_count",
    ]
    summary[numeric_cols] = summary[numeric_cols].round(3)

    return summary


def compute_filtering_summary(
    df: pd.DataFrame, min_doc_words: int, max_code_chars: int
) -> pd.DataFrame:
    rows = []

    for language, group in df.groupby("language"):
        invalid_missing = group["is_missing_code"] | group["is_missing_doc"]
        invalid_short_doc = group["doc_words"] < min_doc_words
        invalid_long_code = group["code_chars"] > max_code_chars
        invalid_duplicate_pair = group["code_doc_hash"].duplicated()

        invalid_any = (
            invalid_missing
            | invalid_short_doc
            | invalid_long_code
            | invalid_duplicate_pair
        )

        rows.append(
            {
                "language": language,
                "raw_records": len(group),
                "missing_code_or_doc": int(invalid_missing.sum()),
                "short_documentation": int(invalid_short_doc.sum()),
                "long_code_records": int(invalid_long_code.sum()),
                "duplicate_code_doc_pairs": int(invalid_duplicate_pair.sum()),
                "diagnostically_retained_records": int((~invalid_any).sum()),
            }
        )

    return pd.DataFrame(rows)


def compute_sample_size_feasibility(
    df: pd.DataFrame, sample_sizes: List[int], min_doc_words: int, max_code_chars: int
) -> pd.DataFrame:
    valid = df[
        (~df["is_missing_code"])
        & (~df["is_missing_doc"])
        & (df["doc_words"] >= min_doc_words)
        & (df["code_chars"] <= max_code_chars)
        & (~df["code_doc_hash"].duplicated())
    ].copy()

    rows = []
    lang_counts = valid.groupby("language").size().to_dict()

    for n in sample_sizes:
        feasible = all(lang_counts.get(lang, 0) >= n for lang in sorted(df["language"].unique()))
        rows.append(
            {
                "candidate_sample_size_per_language": n,
                "feasible_for_all_languages": feasible,
                **{f"{lang}_available_valid_records": lang_counts.get(lang, 0) for lang in sorted(df["language"].unique())},
            }
        )

    return pd.DataFrame(rows)


def write_markdown_report(
    output_path: Path,
    input_path: Path,
    column_map: Dict[str, str],
    row_count_before: int,
    row_count_after_language_filter: int,
    languages: List[str],
    language_split_counts: pd.DataFrame,
    length_stats: pd.DataFrame,
    missing_summary: pd.DataFrame,
    structure_summary: pd.DataFrame,
    filtering_summary: pd.DataFrame,
    feasibility: pd.DataFrame,
    min_doc_words: int,
    max_code_chars: int,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    report = []
    report.append("# Exploratory Data Analysis Summary\n")
    report.append("## Purpose\n")
    report.append(
        "This report summarises the exploratory dataset diagnostics performed before "
        "prompt construction and model execution. The EDA verifies whether the extracted "
        "CodeSearchNet-style records are suitable for controlled function-level code "
        "documentation generation.\n"
    )

    report.append("## Input\n")
    report.append(f"- Input file: `{input_path}`\n")
    report.append(f"- Original record count: `{row_count_before}`\n")
    report.append(f"- Record count after language filtering: `{row_count_after_language_filter}`\n")
    report.append(f"- Languages retained: `{', '.join(languages)}`\n")
    report.append("\n## Column Mapping\n")
    for logical, actual in column_map.items():
        report.append(f"- {logical}: `{actual}`\n")

    report.append("\n## Diagnostic Thresholds\n")
    report.append(f"- Minimum documentation length: `{min_doc_words}` words\n")
    report.append(f"- Long-code diagnostic threshold: `{max_code_chars}` characters\n")

    report.append("\n## Language and Split Distribution\n")
    report.append(language_split_counts.to_markdown(index=False))
    report.append("\n\n## Length Statistics\n")
    report.append(length_stats.to_markdown(index=False))
    report.append("\n\n## Missing and Duplicate Summary\n")
    report.append(missing_summary.to_markdown(index=False))
    report.append("\n\n## Code-Structure Summary\n")
    report.append(structure_summary.to_markdown(index=False))
    report.append("\n\n## Filtering Diagnostics\n")
    report.append(filtering_summary.to_markdown(index=False))
    report.append("\n\n## Sample-Size Feasibility\n")
    report.append(feasibility.to_markdown(index=False))

    report.append("\n\n## Interpretation\n")
    report.append(
        "The EDA confirms whether language balancing, documentation filtering, duplicate "
        "removal, and prompt-length control are required before constructing the final "
        "benchmark. The structure diagnostics also support later code-grounded evaluation "
        "because parameter availability and return-statement presence determine whether "
        "parameter coverage and return coverage can be meaningfully assessed.\n"
    )

    output_path.write_text("\n".join(report), encoding="utf-8")


def main() -> None:
    args = parse_args()

    input_path = Path(args.input)
    output_dir = Path(args.output_dir)
    figures_dir = Path(args.figures_dir)

    output_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    raw_df = load_records(input_path)
    row_count_before = len(raw_df)

    df, column_map = ensure_columns(raw_df)
    selected_languages = [lang.lower() for lang in args.languages]
    df = df[df["language"].isin(selected_languages)].copy()
    row_count_after_language_filter = len(df)

    if df.empty:
        raise ValueError(
            f"No records left after filtering for languages: {selected_languages}"
        )

    df = add_diagnostic_columns(df)

    language_split_counts = compute_language_split_counts(df)
    length_stats = compute_length_statistics(df)
    missing_summary = compute_missing_duplicate_summary(df, args.min_doc_words)
    structure_summary = compute_structure_summary(df)
    filtering_summary = compute_filtering_summary(
        df, args.min_doc_words, args.max_code_chars
    )
    feasibility = compute_sample_size_feasibility(
        df, args.sample_sizes, args.min_doc_words, args.max_code_chars
    )

    save_csv(language_split_counts, output_dir / "eda_language_split_counts.csv")
    save_csv(length_stats, output_dir / "eda_length_statistics.csv")
    save_csv(missing_summary, output_dir / "eda_missing_duplicate_summary.csv")
    save_csv(structure_summary, output_dir / "eda_structure_summary.csv")
    save_csv(filtering_summary, output_dir / "eda_filtering_summary.csv")
    save_csv(feasibility, output_dir / "eda_sample_size_feasibility.csv")

    records_by_language = (
        df.groupby("language").size().reset_index(name="record_count")
    )
    plot_bar(
        records_by_language,
        x="language",
        y="record_count",
        path=figures_dir / "eda_records_by_language.png",
        xlabel="Programming language",
        ylabel="Number of records",
    )

    plot_hist_by_language(
        df,
        value_col="code_words",
        path=figures_dir / "eda_code_length_distribution.png",
        xlabel="Source-code length in words",
        ylabel="Record count",
        max_value=int(df["code_words"].quantile(0.99)),
    )

    plot_hist_by_language(
        df,
        value_col="doc_words",
        path=figures_dir / "eda_doc_length_distribution.png",
        xlabel="Reference-documentation length in words",
        ylabel="Record count",
        max_value=int(df["doc_words"].quantile(0.99)),
    )

    param_distribution = (
        df.groupby(["language", "parameter_count"])
        .size()
        .reset_index(name="record_count")
    )
    fig, ax = plt.subplots(figsize=(8, 5))
    for language, group in param_distribution.groupby("language"):
        group = group[group["parameter_count"] <= 10]
        ax.plot(group["parameter_count"], group["record_count"], marker="o", label=language)
    ax.set_xlabel("Parameter count")
    ax.set_ylabel("Record count")
    ax.legend()
    fig.tight_layout()
    fig.savefig(figures_dir / "eda_parameter_count_distribution.png", dpi=300)
    plt.close(fig)

    return_presence = (
        df.groupby("language")["has_return_statement"]
        .mean()
        .reset_index(name="return_presence_rate")
    )
    plot_bar(
        return_presence,
        x="language",
        y="return_presence_rate",
        path=figures_dir / "eda_return_presence_by_language.png",
        xlabel="Programming language",
        ylabel="Return-statement presence rate",
    )

    write_markdown_report(
        output_path=output_dir / "eda_summary_report.md",
        input_path=input_path,
        column_map=column_map,
        row_count_before=row_count_before,
        row_count_after_language_filter=row_count_after_language_filter,
        languages=selected_languages,
        language_split_counts=language_split_counts,
        length_stats=length_stats,
        missing_summary=missing_summary,
        structure_summary=structure_summary,
        filtering_summary=filtering_summary,
        feasibility=feasibility,
        min_doc_words=args.min_doc_words,
        max_code_chars=args.max_code_chars,
    )

    print("EDA completed successfully.")
    print(f"CSV outputs written to: {output_dir}")
    print(f"Figures written to: {figures_dir}")
    print(f"Markdown report written to: {output_dir / 'eda_summary_report.md'}")


if __name__ == "__main__":
    main()