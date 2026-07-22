#!/usr/bin/env python3
"""Additively organize dissertation runs by model/run family.

The script copies source result artifacts into outputs/segregated_results while
preserving their original path below outputs/. It never deletes, moves, or
overwrites source files or existing destination files.
"""

from __future__ import annotations

import csv
import hashlib
import re
import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS_DIR = REPO_ROOT / "outputs"
DEST_ROOT = OUTPUTS_DIR / "segregated_results"
INDEX_DIR = DEST_ROOT / "index"

SOURCE_DIRS = [
    "raw_generations",
    "evaluations",
    "correctness",
    "batches",
    "responses",
    "human_eval",
    "evaluation-and-correctness-may2026",
    "evaluation_And_corrctness_may2026_1",
]

SOURCE_DIR_ALIASES = {
    "raw_generations": "raw",
    "evaluations": "eval",
    "correctness": "correctness",
    "batches": "batches",
    "responses": "responses",
    "human_eval": "human_eval",
    "evaluation-and-correctness-may2026": "may2026",
    "evaluation_And_corrctness_may2026_1": "may2026_legacy",
}

EXCLUDED_OUTPUT_DIRS = {
    "final_results",
    "segregated_results",
}

CATEGORY_DIRS = {
    "open-source-base": "open-source-base",
    "open-source-lora": "open-source-lora",
    "commercial-base": "commercial-base",
    "shared-aggregate": "shared-aggregate",
}

COMMERCIAL_TOKENS = (
    "gpt",
    "gpt54",
    "codex",
    "codex_cli",
    "gemini",
    "deepseek",
)

OPEN_SOURCE_TOKENS = (
    "qwen",
    "gemma",
    "codegemma",
)

LANGUAGES = ("python", "java", "javascript")
PROMPTS = ("zero_shot", "one_shot", "few_shot")


@dataclass(frozen=True)
class IndexedFile:
    source: Path
    destination: Path
    category: str
    reason: str


@dataclass(frozen=True)
class CopyError:
    item: IndexedFile
    error: str


def relpath(path: Path) -> str:
    return path.resolve().relative_to(REPO_ROOT).as_posix()


def classify(path: Path) -> tuple[str, str]:
    relative = relpath(path).lower()

    if "lora" in relative or "fine-tuned" in relative or "finetune" in relative:
        return "open-source-lora", "Path indicates LoRA/fine-tuned open-source run."

    if any(token in relative for token in COMMERCIAL_TOKENS):
        return "commercial-base", "Path indicates commercial/base model run."

    if any(token in relative for token in OPEN_SOURCE_TOKENS):
        return "open-source-base", "Path indicates open-source base model run."

    return "shared-aggregate", "Shared aggregate, human-eval, table, or mixed-family result."


def destination_for(source: Path, category: str) -> Path:
    outputs_relative = source.resolve().relative_to(OUTPUTS_DIR)
    parts = list(outputs_relative.parts)
    if parts:
        parts[0] = SOURCE_DIR_ALIASES.get(parts[0], parts[0])
    destination = DEST_ROOT / CATEGORY_DIRS[category] / Path(*parts)

    # Keep full Windows paths below the legacy MAX_PATH boundary. The source
    # path is still preserved in the index, so long-path copies remain traceable.
    if len(str(destination.resolve())) > 240:
        digest = hashlib.sha1(outputs_relative.as_posix().encode("utf-8")).hexdigest()[:12]
        filename = source.name
        if len(filename) > 90:
            suffix = "".join(source.suffixes)
            stem = source.name[: 90 - len(suffix)]
            filename = f"{stem}{suffix}"
        destination = (
            DEST_ROOT
            / CATEGORY_DIRS[category]
            / "_long_paths"
            / f"{digest}_{filename}"
        )

    return destination


def iter_source_files() -> list[Path]:
    files: list[Path] = []
    for name in SOURCE_DIRS:
        source_dir = OUTPUTS_DIR / name
        if not source_dir.exists():
            continue

        for path in source_dir.rglob("*"):
            if not path.is_file():
                continue
            parts = path.resolve().relative_to(OUTPUTS_DIR).parts
            if parts and parts[0] in EXCLUDED_OUTPUT_DIRS:
                continue
            files.append(path)

    return sorted(set(files), key=lambda p: relpath(p))


def collect_indexed_files() -> list[IndexedFile]:
    indexed: list[IndexedFile] = []
    for source in iter_source_files():
        category, reason = classify(source)
        indexed.append(
            IndexedFile(
                source=source,
                destination=destination_for(source, category),
                category=category,
                reason=reason,
            )
        )
    return indexed


def copy_files(
    indexed_files: list[IndexedFile],
) -> tuple[list[IndexedFile], list[IndexedFile], list[CopyError]]:
    copied: list[IndexedFile] = []
    skipped: list[IndexedFile] = []
    errors: list[CopyError] = []

    for item in indexed_files:
        if item.destination.exists():
            skipped.append(item)
            continue

        try:
            item.destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item.source, item.destination)
            copied.append(item)
        except OSError as exc:
            errors.append(CopyError(item=item, error=str(exc)))

    return copied, skipped, errors


def write_index(indexed_files: list[IndexedFile]) -> Path:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    path = INDEX_DIR / "segregated_results_index.csv"
    rows = []

    for item in indexed_files:
        stat = item.source.stat()
        rows.append(
            {
                "category": item.category,
                "source_path": relpath(item.source),
                "destination_path": relpath(item.destination),
                "file_size_bytes": stat.st_size,
                "last_write_time": stat.st_mtime,
                "classification_reason": item.reason,
            }
        )

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "category",
                "source_path",
                "destination_path",
                "file_size_bytes",
                "last_write_time",
                "classification_reason",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    return path


def write_summary(
    indexed_files: list[IndexedFile],
    copied: list[IndexedFile],
    skipped: list[IndexedFile],
    errors: list[CopyError],
) -> Path:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    path = INDEX_DIR / "segregated_results_summary.csv"

    total_by_category = Counter(item.category for item in indexed_files)
    copied_by_category = Counter(item.category for item in copied)
    skipped_by_category = Counter(item.category for item in skipped)
    errors_by_category = Counter(error.item.category for error in errors)

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "category",
                "total_files",
                "copied_files",
                "skipped_existing_files",
                "copy_errors",
            ],
        )
        writer.writeheader()
        for category in CATEGORY_DIRS:
            writer.writerow(
                {
                    "category": category,
                    "total_files": total_by_category[category],
                    "copied_files": copied_by_category[category],
                    "skipped_existing_files": skipped_by_category[category],
                    "copy_errors": errors_by_category[category],
                }
            )

    return path


def write_copy_errors(errors: list[CopyError]) -> Path:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    path = INDEX_DIR / "copy_errors.csv"

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["category", "source_path", "destination_path", "error"],
        )
        writer.writeheader()
        for error in errors:
            writer.writerow(
                {
                    "category": error.item.category,
                    "source_path": relpath(error.item.source),
                    "destination_path": relpath(error.item.destination),
                    "error": error.error,
                }
            )

    return path


def model_key(path: Path) -> str:
    name = path.name
    match = re.match(r"(.+?)_P[12]_(zero_shot|one_shot|few_shot)", name, re.IGNORECASE)
    if match:
        return match.group(1)

    for part in path.parts:
        lower = part.lower()
        tokens = OPEN_SOURCE_TOKENS + COMMERCIAL_TOKENS
        if any(token in lower for token in tokens) and "may2026" not in lower:
            return part

    return "unknown"


def language_for(path: Path) -> str | None:
    filename = path.name.lower()
    for language in LANGUAGES:
        if re.search(rf"(^|_){re.escape(language)}(_|\.|$)", filename):
            return language
    return None


def prompt_for(path: Path) -> str | None:
    lower = relpath(path).lower()
    for prompt in PROMPTS:
        if prompt in lower:
            return prompt
    return None


def write_main_400_matrix(indexed_files: list[IndexedFile]) -> Path:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    path = INDEX_DIR / "main_400_run_matrix.csv"

    matrix: dict[tuple[str, str], dict[str, set[str]]] = defaultdict(
        lambda: defaultdict(set)
    )

    for item in indexed_files:
        if item.category == "shared-aggregate":
            continue

        relative = relpath(item.source).lower()
        if "400" not in relative:
            continue

        prompt = prompt_for(item.source)
        language = language_for(item.source)
        if prompt is None or language is None:
            continue

        matrix[(item.category, model_key(item.source))][prompt].add(language)

    rows = []
    for (category, model), by_prompt in sorted(matrix.items()):
        complete = all(set(LANGUAGES).issubset(by_prompt[prompt]) for prompt in PROMPTS)
        for prompt in PROMPTS:
            present = sorted(by_prompt[prompt])
            missing = [language for language in LANGUAGES if language not in by_prompt[prompt]]
            rows.append(
                {
                    "category": category,
                    "model": model,
                    "prompt_setting": prompt,
                    "present_languages": ";".join(present),
                    "missing_languages": ";".join(missing),
                    "complete_3_languages_for_prompt": not missing,
                    "complete_3_languages_x_3_prompts_for_model": complete,
                }
            )

    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "category",
                "model",
                "prompt_setting",
                "present_languages",
                "missing_languages",
                "complete_3_languages_for_prompt",
                "complete_3_languages_x_3_prompts_for_model",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    return path


def print_summary(
    indexed_files: list[IndexedFile],
    copied: list[IndexedFile],
    skipped: list[IndexedFile],
    errors: list[CopyError],
    index_path: Path,
    summary_path: Path,
    matrix_path: Path,
    errors_path: Path,
) -> None:
    total_by_category = Counter(item.category for item in indexed_files)
    copied_by_category = Counter(item.category for item in copied)
    skipped_by_category = Counter(item.category for item in skipped)
    errors_by_category = Counter(error.item.category for error in errors)

    print("Segregated results organization summary")
    print("=" * 42)
    print(f"Indexed source files: {len(indexed_files)}")
    print(f"Copied files: {len(copied)}")
    print(f"Skipped existing destination files: {len(skipped)}")
    print(f"Copy errors: {len(errors)}")
    print()

    for category in CATEGORY_DIRS:
        print(
            f"{category}: total={total_by_category[category]}, "
            f"copied={copied_by_category[category]}, "
            f"skipped={skipped_by_category[category]}, "
            f"errors={errors_by_category[category]}"
        )

    print()
    print(f"Wrote index: {relpath(index_path)}")
    print(f"Wrote summary: {relpath(summary_path)}")
    print(f"Wrote main 400 matrix: {relpath(matrix_path)}")
    print(f"Wrote copy errors: {relpath(errors_path)}")


def main() -> int:
    indexed_files = collect_indexed_files()
    copied, skipped, errors = copy_files(indexed_files)

    index_path = write_index(indexed_files)
    summary_path = write_summary(indexed_files, copied, skipped, errors)
    matrix_path = write_main_400_matrix(indexed_files)
    errors_path = write_copy_errors(errors)

    print_summary(
        indexed_files,
        copied,
        skipped,
        errors,
        index_path,
        summary_path,
        matrix_path,
        errors_path,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
