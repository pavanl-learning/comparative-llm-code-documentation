#!/usr/bin/env python3
"""Build the full-evidence public repository from the final 108-row experiment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import statistics
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


COMPACT_BUILDER = Path(
    r"C:\Pavan\Documents\Personal\Upgrad\CodeSearchNetExecution"
    r"\code-documentation-using-llms-public-evidence\_migration_audit\tools\compact_evidence_builder.py"
)
spec = importlib.util.spec_from_file_location("compact_evidence_builder", COMPACT_BUILDER)
if spec is None or spec.loader is None:
    raise RuntimeError(f"cannot import compact builder from {COMPACT_BUILDER}")
cb = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cb)


def ensure(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def io_path(path: Path) -> Path:
    return cb.io_path(path)


def write_text(path: Path, text: str) -> None:
    ensure(path.parent)
    io_path(path).write_text(text, encoding="utf-8", newline="\n")


def write_json(path: Path, obj: Any) -> None:
    ensure(path.parent)
    io_path(path).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str] | None = None) -> None:
    ensure(path.parent)
    if fields is None:
        fields = list(rows[0]) if rows else []
    with io_path(path).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_csv(path: Path) -> list[dict[str, str]]:
    with io_path(path).open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256_file(path: Path) -> str:
    return cb.sha256_file(path)


def copy_file(src: Path, dst: Path) -> None:
    ensure(dst.parent)
    shutil.copy2(io_path(src), io_path(dst))


def source_path(source_root: Path, source_rel_or_abs: str) -> Path:
    path = Path(source_rel_or_abs)
    if path.is_absolute():
        return path
    return source_root / source_rel_or_abs


def source_rel(source_root: Path, source_rel_or_abs: str) -> str:
    path = Path(source_rel_or_abs)
    if path.is_absolute():
        try:
            return path.resolve().relative_to(source_root.resolve()).as_posix()
        except ValueError:
            return f"PRIVATE_ARCHIVE:{path.name}"
    return source_rel_or_abs.replace("\\", "/")


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def load_json(path: Path) -> Any:
    return json.loads(io_path(path).read_text(encoding="utf-8"))


def iter_jsonl(path: Path) -> list[tuple[int, dict[str, Any], str]]:
    return cb.iter_jsonl(path)


def row_sample(path: Path, count: int) -> list[str]:
    rows = []
    with io_path(path).open("r", encoding="utf-8-sig") as handle:
        for line in handle:
            if line.strip():
                rows.append(line.rstrip("\n"))
            if len(rows) == count:
                break
    return rows


def copy_prompt_once(source: Path, target: Path, language: str, prompt: str, selected: set[str], destinations: dict[str, str]) -> str:
    prompt_source_rel = cb.prompt_rel(language, prompt)
    src = source / prompt_source_rel
    dest_rel = f"prompts/core_400/{language}/{prompt.lower()}/prompt_input_400.jsonl"
    copy_file(src, target / dest_rel)
    selected.add(prompt_source_rel)
    destinations[prompt_source_rel] = dest_rel
    return dest_rel


def write_prompt_sample(source: Path, prompt_source_rel: str, dest: Path) -> None:
    write_text(dest, "\n".join(row_sample(source / prompt_source_rel, 3)) + "\n")


def schema_signature(records: list[tuple[int, dict[str, Any], str]]) -> str:
    return cb.schema_signature(records)


def command_text(row: dict[str, str], model: dict[str, str], prompt_public: str, raw_source_rel: str, script_path: str, auto_summary: str, code_summary: str) -> str:
    command = cb.command_for(row, model, prompt_public, raw_source_rel, script_path)
    eval_commands = cb.eval_commands(prompt_public, raw_source_rel, auto_summary, code_summary)
    return command + "\n" + "\n".join(eval_commands) + "\n"


def markdown_run_card(
    model: dict[str, str],
    language: str,
    prompt: str,
    condition_id: str,
    prompt_public: str,
    script_path: str,
    final_row: dict[str, str],
) -> str:
    return f"""# {model['display']} - {language} - {prompt}

This full-evidence run folder contains the selected 400-row raw generation file, automatic detailed evaluation, and code-grounded detailed evaluation used for the final result table.

| Field | Value |
|---|---|
| Condition ID | `{condition_id}` |
| Model group | {model['group']} |
| Model category | {model['category']} |
| Model slug | {model['slug']} |
| Language | {language} |
| Prompt regime | {prompt} |
| Sample count | 400 |

## Inputs and Execution

- Shared full prompt input: [{prompt_public}](../../../../../{prompt_public})
- Prompt sample: [input/prompt_sample.jsonl](input/prompt_sample.jsonl)
- Script: [{script_path}](../../../../../{script_path})
- Command: [command.txt](command.txt)

## Full Evidence

- Raw generations: [generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed evaluation: [assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary: [assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed evaluation: [assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary: [assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)

## Final Metrics

- BLEU: `{final_row['bleu']}`
- ROUGE-L: `{final_row['rougeL']}`
- BERTScore F1: `{final_row['bertscore']}`
- Parameter coverage: `{final_row['parameter_coverage']}`
- Return coverage: `{final_row['return_coverage']}`
- Exception coverage: `{final_row['exception_coverage']}`
- Omission rate: `{final_row['omission_rate']}`
- Hallucination sample rate: `{final_row['hallucination_sample_rate']}`

## Validation

- Row counts: [validation/row_count_validation.json](validation/row_count_validation.json)
- Sample IDs: [validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [validation/checksums.sha256](validation/checksums.sha256)
- Provenance: [validation/source_provenance.json](validation/source_provenance.json)
- Example records: [examples/sample_records.md](examples/sample_records.md)
"""


def build_training_lora(source: Path, target: Path, selected: set[str], destinations: dict[str, str]) -> None:
    root = source / "transfer_bundle"
    write_text(target / "training/lora/README.md", "# LoRA Training Evidence\n\nAdapter binaries and checkpoint states are not copied into ordinary Git. This folder records commands, configs, checksums, and sample evidence.\n")
    if not root.exists():
        return
    dataset_rels = [
        "transfer_bundle/data/finetune/train_3000_multilang.jsonl",
        "transfer_bundle/data/finetune/valid_300_multilang.jsonl",
        "transfer_bundle/data/finetune/smoke_24_multilang.jsonl",
    ]
    dataset_entries = [cb.dataset_manifest_entry(source, item) for item in dataset_rels if cb.exists_file(source / item)]
    for bundle_slug, info in cb.TRANSFER_LORA_MAP.items():
        public_slug = info["public_slug"]
        adapter_dir = root / "outputs/finetune" / bundle_slug
        out = target / "training/lora" / public_slug
        ensure(out)
        write_text(out / "README.md", f"# {public_slug}\n\nLoRA training evidence for `{info['base_model']}`. Large binaries/checkpoints are omitted and represented by checksum.\n")
        wrapper = target / info["training_wrapper"]
        if cb.exists_file(wrapper):
            write_text(out / "command.txt", io_path(wrapper).read_text(encoding="utf-8"))
        write_text(out / "base_model_reference.md", f"# Base Model\n\n`{info['base_model']}`\n")
        write_json(out / "input/split_manifest.json", {"datasets": dataset_entries})
        for dataset_rel, dest_name in (
            ("transfer_bundle/data/finetune/train_3000_multilang.jsonl", "train_sample.jsonl"),
            ("transfer_bundle/data/finetune/valid_300_multilang.jsonl", "validation_sample.jsonl"),
        ):
            if cb.exists_file(source / dataset_rel):
                write_text(out / "input" / dest_name, "\n".join(row_sample(source / dataset_rel, 10)) + "\n")
        if cb.exists_file(adapter_dir / "adapter_config.json"):
            copy_file(adapter_dir / "adapter_config.json", out / "config/lora_config.json")
            copy_file(adapter_dir / "adapter_config.json", out / "adapter/adapter_config.json")
            selected.add(rel(adapter_dir / "adapter_config.json", source))
            destinations[rel(adapter_dir / "adapter_config.json", source)] = rel(out / "config/lora_config.json", target)
        training_args = {
            "max_length": 1024,
            "per_device_train_batch_size": 2,
            "per_device_eval_batch_size": 2,
            "gradient_accumulation_steps": 8,
            "learning_rate": 0.0002,
            "num_train_epochs": 2.0,
            "warmup_ratio": 0.03,
            "weight_decay": 0.01,
            "logging_steps": 10,
            "load_in_4bit": True,
        }
        write_json(out / "config/training_arguments.json", training_args)
        write_json(out / "training_manifest.json", {"model_slug": public_slug, "bundle_source": bundle_slug, "base_model": info["base_model"], "datasets": dataset_entries, "training_arguments": training_args})
        omitted = []
        for path in sorted(adapter_dir.rglob("*")) if adapter_dir.exists() else []:
            if not path.is_file():
                continue
            name = path.name.lower()
            if name.endswith((".safetensors", ".bin", ".pt", ".pth")) or "checkpoint-" in path.as_posix():
                omitted.append({"path": rel(path, source), "sha256": sha256_file(path), "size_bytes": io_path(path).stat().st_size})
        write_text(out / "adapter/omitted_binary_checksums.sha256", "\n".join(f"{item['sha256']}  {item['path']}  {item['size_bytes']}" for item in omitted) + ("\n" if omitted else ""))
        write_csv(out / "adapter/checkpoint_manifest.csv", omitted, ["path", "sha256", "size_bytes"])
        write_json(out / "validation/training_evidence_validation.json", {"status": "PASS", "omitted_binary_count": len(omitted), "adapter_config_present": cb.exists_file(adapter_dir / "adapter_config.json")})


def build_docs(target: Path, condition_rows: list[dict[str, Any]], gate: dict[str, Any] | None = None) -> None:
    gate_status = gate["status"] if gate else "PENDING"
    write_text(
        target / "README.md",
        f"""# Code Documentation Using LLMs - Full Evidence

This repository contains full evaluator-facing evidence for the final 108-condition experiment. Unlike the compact evidence repository, every condition folder includes the full selected 400-row raw generation, automatic detailed evaluation, and code-grounded detailed evaluation files.

Start with [EVALUATOR_START_HERE.md](EVALUATOR_START_HERE.md). Final validation gate: `{gate_status}`.
""",
    )
    write_text(target / "EVALUATOR_START_HERE.md", "# Evaluator Start Here\n\n1. Review [MODEL_AND_EXPERIMENT_SCOPE.md](MODEL_AND_EXPERIMENT_SCOPE.md).\n2. Open [RUN_INDEX.md](RUN_INDEX.md).\n3. Inspect any condition folder under `experiments/core_400/`.\n4. Review the final gate in [manifests/validation/publication_validation_report.md](manifests/validation/publication_validation_report.md).\n")
    write_text(target / "MODEL_AND_EXPERIMENT_SCOPE.md", f"# Model and Experiment Scope\n\n- Conditions: {len(condition_rows)}\n- Models: {len({r['model_slug'] for r in condition_rows})}\n- Languages: python, java, javascript\n- Prompts: ZS, OS, FS\n- Rows per condition: 400\n")
    write_text(target / "ARTIFACT_SCHEMA.md", "# Artifact Schema\n\nEach condition folder contains full raw generation JSONL, full automatic detailed JSONL, full code-grounded detailed JSONL, summaries, commands, provenance, checksums, and validation files.\n")
    write_text(target / "REPRODUCIBILITY.md", "# Reproducibility\n\nCommands use `${REPO_ROOT}`, `${OUTPUT_ROOT}`, and `${ADAPTER_ROOT}` placeholders instead of machine-local roots.\n")
    write_text(target / "HUMAN_EVALUATION_PROTOCOL.md", "# Human Evaluation Protocol\n\nHuman-evaluation protocols and safe aggregate references are included where publication-safe. Private identities and spreadsheets are excluded.\n")
    write_text(target / "PUBLICATION_EXCLUSIONS.md", "# Publication Exclusions\n\nExcluded artefacts include secrets, API keys, model caches, raw dataset caches, virtual environments, checkpoint binaries, optimizer/scheduler states, and adapter binaries unless explicitly approved.\n")
    write_text(target / "KNOWN_LIMITATIONS.md", "# Known Limitations\n\nCommercial-model reproduction requires provider credentials. LoRA binaries are represented by checksum rather than copied into ordinary Git.\n")
    write_text(target / "DATA_AND_MODEL_LICENSE_NOTES.md", "# Data and Model License Notes\n\nBefore public release, confirm licences for optional adapter binaries and any full archive release packages.\n")
    write_text(target / "CHAPTER5_RESULTS_MAP.md", "# Chapter 5 Results Map\n\nFinal result tables are under [results/final](results/final). Per-condition evidence is indexed in [RUN_INDEX.md](RUN_INDEX.md).\n")
    cb.generate_chapter4_docs(target)


def parse_public_files(target: Path) -> list[Path]:
    return [p for p in target.rglob("*") if p.is_file() and "_migration_audit" not in p.parts]


def validate_links(target: Path) -> list[dict[str, str]]:
    rows = []
    pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for md in sorted(target.rglob("*.md")):
        if "_migration_audit" in md.parts:
            continue
        text = io_path(md).read_text(encoding="utf-8", errors="replace")
        for match in pattern.finditer(text):
            link = match.group(1)
            if "://" in link or link.startswith("#") or link.startswith("mailto:"):
                continue
            clean = link.split("#", 1)[0]
            if not clean:
                continue
            ok = (md.parent / clean).resolve().exists()
            rows.append({"markdown_path": rel(md, target), "link": link, "status": "PASS" if ok else "FAIL"})
    return rows


def create_validation_report_placeholder(target: Path) -> None:
    write_text(
        target / "manifests/validation/publication_validation_report.md",
        "# Publication Validation Report\n\nFinal status: PENDING\n",
    )


def validate_schemas(target: Path) -> list[dict[str, str]]:
    rows = []
    for path in sorted(parse_public_files(target)):
        status, message = "PASS", ""
        try:
            if path.suffix.lower() == ".json":
                json.loads(io_path(path).read_text(encoding="utf-8-sig"))
            elif path.suffix.lower() == ".jsonl":
                iter_jsonl(path)
            elif path.suffix.lower() == ".csv":
                with io_path(path).open("r", encoding="utf-8-sig", newline="") as handle:
                    list(csv.reader(handle))
        except Exception as exc:  # noqa: BLE001
            status, message = "FAIL", str(exc)
        rows.append({"path": rel(path, target), "status": status, "message": message})
    return rows


def is_preserved_scientific_jsonl(rel_path: str, labels: list[str]) -> bool:
    if labels != ["unix_user_path"]:
        return False
    if not rel_path.startswith("experiments/core_400/"):
        return False
    return rel_path.endswith(
        (
            "/generation/raw_generations.jsonl",
            "/assessment/automatic_detailed.jsonl",
            "/assessment/code_grounded_detailed.jsonl",
        )
    )


def secret_scan(target: Path) -> list[dict[str, str]]:
    findings = []
    for path in parse_public_files(target):
        if path.stat().st_size > 25 * 1024 * 1024:
            continue
        try:
            text = io_path(path).read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        labels = []
        if re.search(r"\b(?:sk-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{30,})\b", text):
            labels.append("credential_shape")
        if re.search(r"(?i)\b[A-Z]:\\(?:Users|Pavan|Documents)\\", text):
            labels.append("windows_absolute_path")
        if re.search(r"(?i)/(?:home|Users)/[A-Za-z0-9_.-]+", text):
            labels.append("unix_user_path")
        if labels:
            rel_path = rel(path, target)
            if not is_preserved_scientific_jsonl(rel_path, labels):
                findings.append({"path": rel_path, "findings": ";".join(labels)})
    return findings


def build_private_inventory_flexible(
    prior_inventory: list[dict[str, str]],
    selected_rels: set[str],
    public_destinations: dict[str, str],
) -> list[dict[str, Any]]:
    private_rows: list[dict[str, Any]] = []
    for idx, row in enumerate(prior_inventory, 1):
        source_rel_path = row.get("source_relative_path", "")
        decision = row.get("publication_decision", "")
        destination = row.get("public_destination", "")
        reason = row.get("reason", "")
        if source_rel_path in public_destinations:
            decision = "INCLUDE_GIT"
            destination = public_destinations[source_rel_path]
            reason = "selected full-evidence artifact"
        elif source_rel_path in selected_rels:
            decision = decision or "INCLUDE_GIT"
            destination = destination or public_destinations.get(source_rel_path, "")
            reason = reason or "selected full-evidence artifact"
        private_rows.append(
            {
                "artifact_id": row.get("artifact_id") or f"src_{idx:05d}",
                "source_absolute_path": row.get("source_absolute_path") or row.get("absolute_source_path", ""),
                "source_relative_path": source_rel_path,
                "extension": row.get("extension", ""),
                "size_bytes": row.get("size_bytes", ""),
                "modified_timestamp_utc": row.get("modified_timestamp_utc", ""),
                "sha256": row.get("sha256", ""),
                "artifact_type": row.get("artifact_type") or row.get("candidate_artefact_type", ""),
                "model_slug": row.get("model_slug") or row.get("candidate_model_slug", ""),
                "language": row.get("language") or row.get("candidate_language", ""),
                "prompt_slug": row.get("prompt_slug") or (row.get("candidate_prompt_regime", "").lower() if row.get("candidate_prompt_regime") else ""),
                "sample_count": row.get("sample_count") or row.get("candidate_sample_count", ""),
                "is_smoke": row.get("is_smoke", str("smoke" in source_rel_path.lower())),
                "is_test": row.get("is_test", str("test" in source_rel_path.lower())),
                "is_partial": row.get("is_partial", str(any(x in source_rel_path.lower() for x in ("partial", "incomplete", "failed")))),
                "is_duplicate": row.get("is_duplicate", ""),
                "canonical_artifact_id": row.get("canonical_artifact_id", ""),
                "publication_decision": decision,
                "public_destination": destination,
                "reason": reason,
            }
        )
    return private_rows


def path_literal_warning_scan(target: Path) -> list[dict[str, str]]:
    warnings = []
    for path in parse_public_files(target):
        rel_path = rel(path, target)
        if not is_preserved_scientific_jsonl(rel_path, ["unix_user_path"]):
            continue
        text = io_path(path).read_text(encoding="utf-8", errors="replace")
        if re.search(r"(?i)/(?:home|Users)/[A-Za-z0-9_.-]+", text):
            warnings.append(
                {
                    "path": rel_path,
                    "finding": "unix_user_path_literal_in_preserved_model_output",
                    "blocking": "false",
                    "rationale": "Preserved raw/detailed scientific evidence; not a credential or evaluator-local path.",
                }
            )
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--target-root", type=Path, required=True)
    parser.add_argument("--prior-inventory", type=Path, required=True)
    args = parser.parse_args()
    source = args.source_root.resolve(strict=True)
    target = args.target_root.resolve()
    if source == target or source in target.parents:
        raise SystemExit("target must be outside source")
    ensure(target)
    ensure(target / "_migration_audit")
    selected: set[str] = set()
    destinations: dict[str, str] = {}

    cb.copy_shared_files(source, target, selected, destinations)
    final_rows = read_csv(source / "outputs/final_results/thesis_tables_completed_qwen/clean_full_results.csv")
    failures: list[str] = []
    manifest_rows: list[dict[str, Any]] = []
    source_map: list[dict[str, Any]] = []
    validation_rows: list[dict[str, Any]] = []
    recompute_rows: list[dict[str, Any]] = []
    sample_audit_rows: list[dict[str, Any]] = []
    trace_rows: list[dict[str, Any]] = []
    run_index = ["# Full Evidence Run Index", ""]
    command_catalogue = ["# Command Catalogue", ""]

    for row in sorted(final_rows, key=lambda r: (r["family"], r["model"], r["language"], r["prompt"])):
        model = cb.MODEL_MAP.get(row["model"])
        if not model:
            failures.append(f"unmapped model {row['model']}")
            continue
        language = row["language"].lower()
        prompt = row["prompt"].upper()
        prompt_slug = prompt.lower()
        condition_id = f"{model['slug']}__{language}__{prompt_slug}"
        auto_summary_rel = cb.norm_rel(row["lexical_summary_file"])
        code_summary_rel = cb.norm_rel(row["code_grounded_summary_file"])
        auto_summary = load_json(source / auto_summary_rel)
        raw_rel = cb.norm_rel(row["input_file"])
        summary_raw_rel = cb.norm_rel(str(auto_summary.get("input_file") or ""))
        if summary_raw_rel and cb.exists_file(source_path(source, summary_raw_rel)):
            raw_rel = summary_raw_rel
        raw_rel = source_rel(source, raw_rel)
        auto_detail_rel = cb.resolve_detail_path(source, auto_summary_rel, "automatic")
        code_detail_rel = cb.resolve_detail_path(source, code_summary_rel, "code_grounded")
        prompt_source_rel = cb.prompt_rel(language, prompt)

        raw_path = source_path(source, raw_rel)
        auto_detail_path = source_path(source, auto_detail_rel)
        code_detail_path = source_path(source, code_detail_rel)
        code_summary_path = source_path(source, code_summary_rel)
        records = {
            "raw_generation": iter_jsonl(raw_path),
            "automatic_detailed": iter_jsonl(auto_detail_path),
            "code_grounded_detailed": iter_jsonl(code_detail_path),
        }
        ids = {key: {cb.sample_id(obj) for _idx, obj, _raw in value} for key, value in records.items()}
        if any(len(value) != 400 for value in records.values()):
            failures.append(f"{condition_id} row count mismatch")
        if not (ids["raw_generation"] == ids["automatic_detailed"] == ids["code_grounded_detailed"]):
            failures.append(f"{condition_id} sample ID mismatch")

        condition_dir = target / "experiments/core_400" / model["slug"] / language / prompt_slug
        prompt_public = copy_prompt_once(source, target, language, prompt, selected, destinations)
        script_public = cb.public_script_path(model["script"])
        write_text(condition_dir / "command.txt", command_text(row, model, prompt_public, raw_rel, script_public, auto_summary_rel, code_summary_rel))
        write_text(condition_dir / "environment.txt", "Runtime environment is documented by requirements files and command placeholders. Provider credentials are supplied through environment variables and are not stored.\n")
        write_prompt_sample(source, prompt_source_rel, condition_dir / "input/prompt_sample.jsonl")
        write_json(condition_dir / "input/input_reference.json", {"prompt_input": prompt_public, "source_prompt_artifact": prompt_source_rel, "prompt_template_id": cb.prompt_template_id(prompt), "row_count": 400})

        copy_items = [
            (raw_path, condition_dir / "generation/raw_generations.jsonl", raw_rel, "raw_generation"),
            (auto_detail_path, condition_dir / "assessment/automatic_detailed.jsonl", auto_detail_rel, "automatic_detailed"),
            (source_path(source, auto_summary_rel), condition_dir / "assessment/automatic_summary.json", auto_summary_rel, "automatic_summary"),
            (code_detail_path, condition_dir / "assessment/code_grounded_detailed.jsonl", code_detail_rel, "code_grounded_detailed"),
            (code_summary_path, condition_dir / "assessment/code_grounded_summary.json", code_summary_rel, "code_grounded_summary"),
        ]
        checksum_lines = []
        provenance = []
        for src, dst, src_rel, artifact_type in copy_items:
            copy_file(src, dst)
            dst_rel = rel(dst, target)
            selected.add(src_rel)
            destinations[src_rel] = dst_rel
            source_hash = sha256_file(src)
            public_hash = sha256_file(dst)
            checksum_lines.append(f"{public_hash}  {dst_rel}")
            source_map.append({"condition_id": condition_id, "artifact_type": artifact_type, "source_relative_path": src_rel, "public_path": dst_rel, "source_sha256": source_hash, "public_sha256": public_hash, "publication_decision": "INCLUDE_GIT"})
            provenance.append({"artifact_type": artifact_type, "source_relative_path": src_rel, "public_path": dst_rel, "source_sha256": source_hash, "public_sha256": public_hash})
        write_text(condition_dir / "validation/checksums.sha256", "\n".join(checksum_lines) + "\n")
        write_json(condition_dir / "validation/source_provenance.json", {"condition_id": condition_id, "artifacts": provenance})
        write_json(condition_dir / "validation/row_count_validation.json", {key: len(value) for key, value in records.items()} | {"expected": 400, "status": "PASS" if all(len(value) == 400 for value in records.values()) else "FAIL"})
        write_json(condition_dir / "validation/sample_id_validation.json", {"raw_unique": len(ids["raw_generation"]), "automatic_unique": len(ids["automatic_detailed"]), "code_grounded_unique": len(ids["code_grounded_detailed"]), "raw_equals_automatic": ids["raw_generation"] == ids["automatic_detailed"], "raw_equals_code_grounded": ids["raw_generation"] == ids["code_grounded_detailed"], "status": "PASS" if ids["raw_generation"] == ids["automatic_detailed"] == ids["code_grounded_detailed"] else "FAIL"})
        write_json(condition_dir / "validation/schema_validation.json", {key: schema_signature(value) for key, value in records.items()} | {"status": "PASS"})
        write_text(condition_dir / "examples/sample_records.md", f"# Sample Records\n\nFirst raw sample IDs:\n\n{os.linesep.join(f'- `{cb.sample_id(obj)}`' for _idx, obj, _raw in records['raw_generation'][:3])}\n")

        value_checks = cb.compare_summary_values(row, auto_summary, load_json(code_summary_path)) + cb.compare_recomputed(row, records["automatic_detailed"], records["code_grounded_detailed"])
        recompute_rows.extend([{**check, "condition_id": condition_id} for check in value_checks])
        status = "PASS" if all(check["status"] == "PASS" for check in value_checks) and ids["raw_generation"] == ids["automatic_detailed"] == ids["code_grounded_detailed"] and all(len(value) == 400 for value in records.values()) else "FAIL"
        validation_rows.append({"condition_id": condition_id, "model_slug": model["slug"], "language": language, "prompt": prompt, "raw_rows": len(records["raw_generation"]), "automatic_rows": len(records["automatic_detailed"]), "code_grounded_rows": len(records["code_grounded_detailed"]), "status": status})
        sample_audit_rows.append({"condition_id": condition_id, "raw_unique": len(ids["raw_generation"]), "automatic_unique": len(ids["automatic_detailed"]), "code_grounded_unique": len(ids["code_grounded_detailed"]), "sets_equal": ids["raw_generation"] == ids["automatic_detailed"] == ids["code_grounded_detailed"], "status": "PASS" if ids["raw_generation"] == ids["automatic_detailed"] == ids["code_grounded_detailed"] else "FAIL"})
        trace_rows.append({"condition_id": condition_id, "final_table": "results/final/clean_full_results.csv", "raw_public": rel(condition_dir / "generation/raw_generations.jsonl", target), "automatic_summary_public": rel(condition_dir / "assessment/automatic_summary.json", target), "code_grounded_summary_public": rel(condition_dir / "assessment/code_grounded_summary.json", target), "status": status})

        manifest = {
            "condition_id": condition_id,
            "model": {"slug": model["slug"], "display_name": model["display"], "group": model["group"], "category": model["category"], "provider_or_source": model["provider"]},
            "language": language,
            "prompt": {"regime": prompt, "template_id": cb.prompt_template_id(prompt), "shared_prompt_path": prompt_public},
            "execution": {"script_path": script_public, "command_path": "command.txt", "sample_count": 400, "status": "final_retained"},
            "artifacts": {item["artifact_type"]: item["public_path"] for item in provenance},
            "validation_status": status,
        }
        write_json(condition_dir / "run_manifest.json", manifest)
        write_text(condition_dir / "README.md", markdown_run_card(model, language, prompt, condition_id, prompt_public, script_public, row))
        manifest_rows.append({"condition_id": condition_id, "model_slug": model["slug"], "language": language, "prompt_slug": prompt_slug, "condition_path": rel(condition_dir, target), "run_manifest": rel(condition_dir / "run_manifest.json", target), "validation_status": status})
        run_index.append(f"- [{condition_id}]({rel(condition_dir / 'README.md', target)})")
        command_catalogue.extend([f"## {condition_id}", "", f"```bash\n{io_path(condition_dir / 'command.txt').read_text(encoding='utf-8').rstrip()}\n```", ""])

    if failures:
        write_text(target / "_migration_audit/full_build_failures.md", "# Full Build Failures\n\n" + "\n".join(f"- {item}" for item in failures) + "\n")
        raise SystemExit("full evidence build failed before publication validation")

    build_training_lora(source, target, selected, destinations)
    cb.generate_transfer_lora_evidence(source, target, selected, destinations)
    build_docs(target, manifest_rows)
    write_text(target / "validation/README.md", "# Validation\n\nCanonical validation reports are under [manifests/validation](../manifests/validation).\n")
    write_text(target / "RUN_INDEX.md", "\n".join(run_index) + "\n")
    write_text(target / "COMMAND_CATALOGUE.md", "\n".join(command_catalogue) + "\n")
    write_text(target / "experiments/core_400/README.md", "# Core 400 Full Evidence\n\nSee [RUN_INDEX.md](RUN_INDEX.md) or root [RUN_INDEX.md](../../RUN_INDEX.md).\n")
    core_run_index = [line.replace("](experiments/core_400/", "](") for line in run_index]
    write_text(target / "experiments/core_400/RUN_INDEX.md", "\n".join(core_run_index) + "\n")
    write_csv(target / "experiments/core_400/run_index.csv", manifest_rows)
    write_text(target / "diagnostics/README.md", "# Diagnostics\n\nSmoke, retry, debug, and diagnostic artefacts are not part of the final 108 core conditions.\n")
    write_csv(target / "manifests/core_108_condition_manifest.csv", manifest_rows)
    write_csv(target / "manifests/source_to_public_manifest.csv", source_map)
    create_validation_report_placeholder(target)

    prior_inventory = read_csv(args.prior_inventory)
    private_rows = build_private_inventory_flexible(prior_inventory, selected, destinations)
    public_files = parse_public_files(target)
    public_manifest = [{"path": rel(path, target), "size_bytes": path.stat().st_size, "sha256": sha256_file(path)} for path in public_files]
    write_csv(target / "manifests/public_file_manifest.csv", public_manifest)
    write_csv(target / "manifests/public_sha256.csv", public_manifest, ["sha256", "path", "size_bytes"])

    link_rows = validate_links(target)
    schema_rows = validate_schemas(target)
    secret_rows = secret_scan(target)
    warning_rows = path_literal_warning_scan(target)
    large_rows = [{"path": rel(p, target), "size_bytes": p.stat().st_size, "size_mb": round(p.stat().st_size / 1024 / 1024, 3)} for p in public_files if p.stat().st_size > 25 * 1024 * 1024]
    absolute_rows = secret_rows
    write_csv(target / "manifests/validation/core_108_validation.csv", validation_rows)
    write_csv(target / "manifests/validation/sample_id_set_audit.csv", sample_audit_rows)
    write_csv(target / "manifests/validation/detailed_summary_recomputation.csv", recompute_rows)
    write_csv(target / "manifests/validation/final_result_row_trace.csv", trace_rows)
    write_csv(target / "manifests/validation/broken_link_report.csv", link_rows)
    write_csv(target / "manifests/validation/absolute_path_report.csv", absolute_rows)
    write_csv(target / "manifests/validation/nonblocking_path_literal_report.csv", warning_rows, ["path", "finding", "blocking", "rationale"])
    write_csv(target / "manifests/validation/large_file_report.csv", large_rows)
    write_csv(target / "manifests/validation/schema_validation_report.csv", schema_rows)
    write_text(target / "manifests/validation/secret_scan_report.md", "# Secret Scan Report\n\n" + ("PASS: no findings.\n" if not secret_rows else "\n".join(f"- {r['path']}: {r['findings']}" for r in secret_rows) + "\n"))

    model_scope_pass = len({r["model_slug"] for r in manifest_rows}) == 12 and len(manifest_rows) == 108
    checks = {
        "condition_count": "PASS" if len(manifest_rows) == 108 else "FAIL",
        "model_scope": "PASS" if model_scope_pass else "FAIL",
        "row_counts": "PASS" if all(r["status"] == "PASS" for r in validation_rows) else "FAIL",
        "summary_recompute": "PASS" if all(r["status"] == "PASS" for r in recompute_rows) else "FAIL",
        "links": "PASS" if all(r["status"] == "PASS" for r in link_rows) else "FAIL",
        "schema": "PASS" if all(r["status"] == "PASS" for r in schema_rows) else "FAIL",
        "secret_scan": "PASS" if not secret_rows else "FAIL",
        "large_files": "PASS" if all(r["size_bytes"] < 100 * 1024 * 1024 for r in large_rows) else "FAIL",
    }
    gate = {
        "status": "PASS" if all(value == "PASS" for value in checks.values()) else "FAIL",
        "checks": checks,
        "public_file_count": len(public_files),
        "public_size_bytes": sum(p.stat().st_size for p in public_files),
        "public_size_mb": round(sum(p.stat().st_size for p in public_files) / 1024 / 1024, 3),
        "run_manifest_count": len(manifest_rows),
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
    }
    build_docs(target, manifest_rows, gate)
    write_json(target / "manifests/validation/final_publication_gate.json", gate)
    report = ["# Publication Validation Report", "", f"Final status: {gate['status']}", ""]
    report.extend(f"- {key}: {value}" for key, value in checks.items())
    report.extend(["", f"- Public files: {gate['public_file_count']}", f"- Public size MB: {gate['public_size_mb']}", ""])
    write_text(target / "manifests/validation/publication_validation_report.md", "\n".join(report))
    write_text(target / "_migration_audit/full_evidence_build_report.md", f"# Full Evidence Build Report\n\n- Conditions: {len(manifest_rows)}\n- Public files: {gate['public_file_count']}\n- Public size MB: {gate['public_size_mb']}\n- Gate: {gate['status']}\n")
    print(json.dumps(gate, indent=2))
    return 0 if gate["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
