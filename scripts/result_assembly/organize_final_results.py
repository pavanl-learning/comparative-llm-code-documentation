#!/usr/bin/env python3
"""Additively organize final dissertation result files.

This script copies selected clean result artifacts into outputs/final_results
without deleting, moving, or overwriting any existing source or destination file.
"""

from __future__ import annotations

import csv
import shutil
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = REPO_ROOT / "outputs"
FINAL_RESULTS_DIR = OUTPUTS_DIR / "final_results"


@dataclass(frozen=True)
class CopySpec:
    source: Path
    destination_dir: Path
    label: str

    @property
    def destination(self) -> Path:
        return self.destination_dir / self.source.name


@dataclass(frozen=True)
class LegacySpec:
    path: Path
    reason: str


AUTOMATIC_METRICS_DIR = FINAL_RESULTS_DIR / "automatic_metrics"
CORRECTNESS_DIR = FINAL_RESULTS_DIR / "code_grounded_correctness"
THESIS_TABLES_DIR = FINAL_RESULTS_DIR / "thesis_tables"
LEGACY_INDEX_DIR = FINAL_RESULTS_DIR / "legacy_index"
LEGACY_INDEX_PATH = LEGACY_INDEX_DIR / "legacy_files_index.csv"


KNOWN_CLEAN_FILES = [
    CopySpec(
        OUTPUTS_DIR / "evaluations" / "qwen_base_zs_fs_metrics_400_clean.csv",
        AUTOMATIC_METRICS_DIR,
        "automatic metrics",
    ),
    CopySpec(
        OUTPUTS_DIR / "evaluations" / "qwen_base_zs_fs_metrics_400_clean.xlsx",
        AUTOMATIC_METRICS_DIR,
        "automatic metrics",
    ),
    CopySpec(
        OUTPUTS_DIR / "correctness" / "qwen_base_zs_fs_correctness_400_clean.csv",
        CORRECTNESS_DIR,
        "code-grounded correctness",
    ),
    CopySpec(
        OUTPUTS_DIR / "correctness" / "qwen_base_zs_fs_correctness_400_clean.xlsx",
        CORRECTNESS_DIR,
        "code-grounded correctness",
    ),
]


ADDITIONAL_CLEAN_FILES = [
    CopySpec(
        OUTPUTS_DIR / "evaluations" / "all_evaluation_summaries_clean.csv",
        AUTOMATIC_METRICS_DIR,
        "automatic metrics aggregate",
    ),
]


THESIS_TABLE_SOURCE_DIR = (
    OUTPUTS_DIR
    / "evaluation-and-correctness-may2026"
    / "final-results-tables-and-plots"
    / "tables"
)


LEGACY_FILES = [
    LegacySpec(
        OUTPUTS_DIR / "evaluations" / "all_evaluation_summaries.csv",
        "Superseded by outputs/evaluations/all_evaluation_summaries_clean.csv.",
    ),
    LegacySpec(
        OUTPUTS_DIR
        / "evaluation_And_corrctness_may2026_1"
        / "decoding_sensitivity"
        / "plots"
        / "decoding_sensitivity_metrics.csv",
        "Older May 2026 supplemental result in legacy typo-style folder.",
    ),
    LegacySpec(
        OUTPUTS_DIR
        / "evaluation_And_corrctness_may2026_1"
        / "saturation_experiment"
        / "saturation_publication_fixed_axis"
        / "saturation_metrics_fixed_axis_used.csv",
        "Older May 2026 supplemental result in legacy typo-style folder.",
    ),
]


def relpath(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def ensure_directories() -> None:
    for directory in [
        FINAL_RESULTS_DIR,
        AUTOMATIC_METRICS_DIR,
        CORRECTNESS_DIR,
        THESIS_TABLES_DIR,
        LEGACY_INDEX_DIR,
    ]:
        directory.mkdir(parents=True, exist_ok=True)


def collect_thesis_table_specs() -> tuple[list[CopySpec], list[Path]]:
    if not THESIS_TABLE_SOURCE_DIR.exists():
        return [], [THESIS_TABLE_SOURCE_DIR]

    specs = [
        CopySpec(path, THESIS_TABLES_DIR, "thesis table")
        for path in sorted(THESIS_TABLE_SOURCE_DIR.glob("*.csv"))
        if path.is_file()
    ]
    return specs, []


def copy_additive(specs: list[CopySpec]) -> tuple[list[CopySpec], list[CopySpec], list[CopySpec]]:
    copied: list[CopySpec] = []
    skipped: list[CopySpec] = []
    missing: list[CopySpec] = []

    for spec in specs:
        if not spec.source.exists():
            missing.append(spec)
            continue

        if spec.destination.exists():
            skipped.append(spec)
            continue

        spec.destination_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(spec.source, spec.destination)
        copied.append(spec)

    return copied, skipped, missing


def write_legacy_index(legacy_specs: list[LegacySpec]) -> tuple[list[LegacySpec], list[LegacySpec]]:
    indexed: list[LegacySpec] = []
    missing: list[LegacySpec] = []

    rows = []
    for spec in legacy_specs:
        if not spec.path.exists():
            missing.append(spec)
            continue

        indexed.append(spec)
        stat = spec.path.stat()
        rows.append(
            {
                "path": relpath(spec.path),
                "file_size_bytes": stat.st_size,
                "reason": spec.reason,
            }
        )

    if LEGACY_INDEX_PATH.exists():
        print(f"SKIP existing legacy index: {relpath(LEGACY_INDEX_PATH)}")
        return indexed, missing

    LEGACY_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LEGACY_INDEX_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["path", "file_size_bytes", "reason"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"WROTE legacy index: {relpath(LEGACY_INDEX_PATH)} ({len(rows)} rows)")
    return indexed, missing


def print_copy_summary(
    copied: list[CopySpec],
    skipped: list[CopySpec],
    missing: list[CopySpec],
    missing_table_dirs: list[Path],
    indexed_legacy: list[LegacySpec],
    missing_legacy: list[LegacySpec],
) -> None:
    print("\nFinal results organization summary")
    print("=" * 43)
    print(f"Copied files: {len(copied)}")
    for spec in copied:
        print(f"  COPY {relpath(spec.source)} -> {relpath(spec.destination)}")

    print(f"\nSkipped existing destinations: {len(skipped)}")
    for spec in skipped:
        print(f"  SKIP {relpath(spec.destination)}")

    print(f"\nMissing source files: {len(missing)}")
    for spec in missing:
        print(f"  MISSING {relpath(spec.source)} ({spec.label})")

    print(f"\nMissing thesis table directories: {len(missing_table_dirs)}")
    for path in missing_table_dirs:
        print(f"  MISSING {relpath(path)}")

    print(f"\nLegacy files indexed: {len(indexed_legacy)}")
    for spec in indexed_legacy:
        print(f"  LEGACY {relpath(spec.path)}")

    print(f"\nLegacy files missing: {len(missing_legacy)}")
    for spec in missing_legacy:
        print(f"  MISSING {relpath(spec.path)}")


def main() -> int:
    ensure_directories()

    thesis_table_specs, missing_table_dirs = collect_thesis_table_specs()
    all_copy_specs = KNOWN_CLEAN_FILES + ADDITIONAL_CLEAN_FILES + thesis_table_specs

    copied, skipped, missing = copy_additive(all_copy_specs)
    indexed_legacy, missing_legacy = write_legacy_index(LEGACY_FILES)

    print_copy_summary(
        copied,
        skipped,
        missing,
        missing_table_dirs,
        indexed_legacy,
        missing_legacy,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
