#!/usr/bin/env python3
"""Run missing downstream metrics/correctness for 400-sample LoRA outputs."""

from __future__ import annotations

import csv
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUN_PRESENCE_CSV = REPO_ROOT / "outputs" / "segregated_results" / "index" / "main_400_core_run_presence.csv"
SEGREGATED_INDEX_CSV = REPO_ROOT / "outputs" / "segregated_results" / "index" / "segregated_results_index.csv"
EVALUATE_GENERATIONS = REPO_ROOT / "scripts" / "evaluate_generations.py"
EVALUATE_CORRECTNESS = REPO_ROOT / "scripts" / "evaluate_code_grounded_correctness.py"


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def truthy(value: str) -> bool:
    return str(value).strip().lower() == "true"


def source_file_for(prompt: str, language: str) -> Path:
    if prompt == "zero_shot":
        name = f"P1_zero_shot_{language}_400_ZS.jsonl"
    elif prompt == "one_shot":
        name = f"P1_one_shot_{language}_400.jsonl"
    elif prompt == "few_shot":
        name = f"P1_few_shot_{language}_400.jsonl"
    else:
        raise ValueError(f"Unsupported prompt setting: {prompt}")

    return REPO_ROOT / "data" / "processed" / "prompted_shots" / name


def find_raw_file(index_rows: list[dict[str, str]], model: str, prompt: str, language: str) -> Path | None:
    candidates = []
    for row in index_rows:
        source = row["source_path"]
        source_lower = source.lower()
        filename = Path(source).name.lower()

        if row["category"] != "open-source-lora":
            continue
        if "/raw_generations/" not in source_lower:
            continue
        if model.lower() not in source_lower:
            continue
        if prompt not in source_lower:
            continue
        if f"_{language}_" not in filename:
            continue
        if "400" not in filename:
            continue

        path = REPO_ROOT / source
        if path.exists():
            candidates.append(path)

    return sorted(candidates, key=lambda p: str(p))[0] if candidates else None


def output_base(raw_file: Path) -> str:
    return raw_file.stem


def outputs_exist(prefix: Path) -> bool:
    return Path(str(prefix) + "_summary.json").exists() and Path(str(prefix) + "_detailed.jsonl").exists()


def run_command(args: list[str]) -> int:
    print("RUN " + " ".join(args))
    completed = subprocess.run(args, cwd=REPO_ROOT)
    return completed.returncode


def main() -> int:
    presence_rows = load_csv(RUN_PRESENCE_CSV)
    index_rows = load_csv(SEGREGATED_INDEX_CSV)

    metric_jobs = []
    correctness_jobs = []
    missing_raw = []
    missing_source = []

    for row in presence_rows:
        if row["category"] != "open-source-lora":
            continue
        if truthy(row["metrics_present"]) and truthy(row["correctness_present"]):
            continue

        raw_file = find_raw_file(
            index_rows,
            row["model"],
            row["prompt_setting"],
            row["language"],
        )
        if raw_file is None:
            missing_raw.append(row)
            continue

        base = output_base(raw_file)
        if not truthy(row["metrics_present"]):
            metric_prefix = REPO_ROOT / "outputs" / "evaluations" / f"{base}_eval.json"
            if not outputs_exist(metric_prefix):
                metric_jobs.append((raw_file, metric_prefix))

        if not truthy(row["correctness_present"]):
            source_file = source_file_for(row["prompt_setting"], row["language"])
            if not source_file.exists():
                missing_source.append((row, source_file))
                continue

            correctness_prefix = REPO_ROOT / "outputs" / "correctness" / f"{base}_correctness"
            if not outputs_exist(correctness_prefix):
                correctness_jobs.append((raw_file, source_file, correctness_prefix))

    print("Missing LoRA downstream job plan")
    print("=" * 36)
    print(f"Metric jobs to run: {len(metric_jobs)}")
    print(f"Correctness jobs to run: {len(correctness_jobs)}")
    print(f"Missing raw files: {len(missing_raw)}")
    print(f"Missing source prompt files: {len(missing_source)}")

    for raw_file, prefix in metric_jobs:
        rc = run_command(
            [
                sys.executable,
                str(EVALUATE_GENERATIONS),
                "--input",
                str(raw_file),
                "--output-prefix",
                str(prefix),
            ]
        )
        if rc != 0:
            return rc

    for raw_file, source_file, prefix in correctness_jobs:
        rc = run_command(
            [
                sys.executable,
                str(EVALUATE_CORRECTNESS),
                "--input",
                str(raw_file),
                "--source",
                str(source_file),
                "--output-prefix",
                str(prefix),
            ]
        )
        if rc != 0:
            return rc

    print("Completed missing LoRA downstream job run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
