#!/usr/bin/env python3
"""Create a non-destructive, checksum-backed inventory of the thesis source tree."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import mimetypes
import os
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


TEXT_EXTENSIONS = {
    ".py", ".sh", ".ps1", ".bat", ".cmd", ".ipynb", ".json", ".jsonl",
    ".csv", ".tsv", ".md", ".txt", ".yaml", ".yml", ".toml", ".xml",
    ".svg", ".drawio", ".log", ".cfg", ".ini", ".env",
}
DIAGNOSTIC_MARKERS = ("smoke", "test", "debug", "diagnostic", "failed", "partial", "legacy", "superseded")
MODEL_ALIASES = [
    ("qwen2_5_coder_1_5b_instruct_lora", ("qwen2_5_coder_1_5b_instruct_lora", "qwen25_coder_1_5b_lora", "qwen_coder_lora")),
    ("qwen2_5_1_5b_instruct_lora", ("qwen2_5_1_5b_instruct_lora", "qwen25_1_5b_instruct_lora", "qwen_lora")),
    ("gemma_2_2b_it_lora", ("gemma_2_2b_it_lora", "gemma_2_2b_lora", "gemma_lora")),
    ("codegemma_2b_lora", ("codegemma_2b_lora", "codegemma_lora")),
    ("qwen2_5_coder_1_5b_instruct", ("qwen2_5_coder_1_5b_instruct", "qwen25_coder_1_5b", "qwen_coder")),
    ("qwen2_5_1_5b_instruct", ("qwen2_5_1_5b_instruct", "qwen25_1_5b_instruct", "qwen_base")),
    ("gemma_2_2b_it", ("gemma_2_2b_it", "gemma_2_2b", "gemma-2-2b-it")),
    ("codegemma_2b", ("codegemma_2b", "codegemma-2b")),
    ("deepseek_chat_v3_2", ("deepseek_chat_v3_2", "deepseek-chat-v3.2", "deepseek")),
    ("gemini_3_flash", ("gemini_3_flash", "gemini-3-flash", "gemini")),
    ("gpt_5_1_codex", ("gpt_5_1_codex", "gpt-5.1-codex", "codex")),
    ("gpt_5_1", ("gpt_5_1", "gpt-5.1")),
]


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def detect_model(value: str) -> str:
    normal = value.lower().replace("-", "_").replace(".", "_")
    for slug, aliases in MODEL_ALIASES:
        if any(alias.lower().replace("-", "_").replace(".", "_") in normal for alias in aliases):
            return slug
    return ""


def detect_language(value: str) -> str:
    normal = value.lower()
    if re.search(r"(^|[^a-z])javascript([^a-z]|$)|(^|[_\\/.-])js([_\\/.-]|$)", normal):
        return "javascript"
    if re.search(r"(^|[^a-z])python([^a-z]|$)|(^|[_\\/.-])py([_\\/.-]|$)", normal):
        return "python"
    if re.search(r"(^|[^a-z])java([^a-z]|$)", normal):
        return "java"
    return ""


def detect_prompt(value: str) -> str:
    normal = value.lower()
    if re.search(r"few[_ -]?shot|(^|[_\\/.-])fs([_\\/.-]|$)", normal):
        return "FS"
    if re.search(r"one[_ -]?shot|(^|[_\\/.-])os([_\\/.-]|$)", normal):
        return "OS"
    if re.search(r"zero[_ -]?shot|(^|[_\\/.-])zs([_\\/.-]|$)", normal):
        return "ZS"
    return ""


def detect_sample_count(value: str) -> str:
    matches = re.findall(r"(?:^|[_\\/.-])(10|50|100|200|300|400|500|1000|5000|15000)(?:[_\\/.-]|$)", value.lower())
    return matches[-1] if matches else ""


def classify(rel: str, suffix: str) -> tuple[str, str]:
    lower = rel.lower().replace("\\", "/")
    name = Path(lower).name
    if any(marker in lower for marker in DIAGNOSTIC_MARKERS):
        if "smoke" in lower:
            return "smoke_output", "diagnostics"
        if "legacy" in lower or "superseded" in lower:
            return "legacy_output", "diagnostics"
        return "diagnostic_output", "diagnostics"
    if suffix in {".safetensors", ".bin", ".pt", ".pth"} or "checkpoint-" in lower:
        return "lora_checkpoint_binary", "lora_training"
    if "trainer_state" in name:
        return "lora_trainer_state", "lora_training"
    if "adapter_config" in name:
        return "lora_adapter_metadata", "lora_training"
    if suffix == ".py":
        stage = "reporting" if any(x in name for x in ("result", "plot", "report", "organize")) else "implementation"
        return "source_code", stage
    if suffix in {".sh", ".ps1", ".bat", ".cmd"}:
        return "automation_command", "implementation"
    if suffix in {".yaml", ".yml", ".toml", ".cfg", ".ini"} or "requirements" in name:
        return "configuration", "environment_governance"
    if "human" in lower:
        if any(x in name for x in ("summary", "agreement", "kappa")):
            return "human_evaluation_summary", "human_evaluation"
        if suffix in {".xlsx", ".xls"}:
            return "human_evaluation_output", "human_evaluation"
        return "human_evaluation_input", "human_evaluation"
    if "prompt" in lower:
        return "prompt_artefact", "prompt_construction"
    if "demo" in lower:
        return "demonstration_bank", "prompt_construction"
    if "correctness" in lower or "grounded" in lower:
        return ("code_grounded_summary" if "summary" in name else "code_grounded_detailed"), "code_grounded_evaluation"
    if "eval" in lower or "bertscore" in lower or "rouge" in lower or "bleu" in lower:
        return ("automatic_evaluation_summary" if "summary" in name else "automatic_evaluation_detailed"), "automatic_evaluation"
    if "raw_generation" in lower or "generation" in name or "generations" in name:
        return "raw_generation", "model_execution"
    if "request" in lower or "batch_input" in lower:
        return "provider_request", "commercial_execution"
    if "response" in lower or "batch_output" in lower:
        return "provider_response", "commercial_execution"
    if "batch" in lower and suffix == ".json":
        return "provider_batch_state", "commercial_execution"
    if "train" in lower and suffix in {".json", ".jsonl", ".csv"}:
        return "lora_training_input", "lora_training"
    if "final_result" in lower or "thesis_table" in lower or "comparison" in lower:
        return "final_result_table", "final_result_assembly"
    if "audit" in lower or "manifest" in lower:
        return "final_result_audit", "final_result_assembly"
    if suffix in {".png", ".svg", ".drawio", ".pdf"}:
        return ("figure_chapter5" if "chapter5" in lower or "result" in lower else "figure_chapter4"), "documentation"
    if lower.startswith("data/"):
        if "cache" in lower or "codesearchnet" in lower and suffix in {".parquet", ".arrow"}:
            return "raw_dataset_cache", "dataset_preparation"
        return "processed_dataset", "dataset_preparation"
    if "log" in lower or suffix == ".log":
        return "run_log", "execution"
    if suffix in {".md", ".txt"}:
        return "thesis_document", "documentation"
    if "__pycache__" in lower or suffix in {".pyc", ".tmp"}:
        return "cache_or_environment", "environment_governance"
    return "unknown_manual_review", "unknown"


def scan_text_risks(path: Path, size: int) -> tuple[list[str], list[str]]:
    if path.suffix.lower() not in TEXT_EXTENSIONS or size > 25 * 1024 * 1024:
        return [], []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ["unreadable_text"], []
    secret_types = []
    patterns = {
        "private_key": r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        "credential_assignment": r"(?im)^\s*(?:api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*[^\s$<{][^\r\n]{5,}",
        "provider_key_shape": r"\b(?:sk-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{30,})\b",
    }
    for label, pattern in patterns.items():
        if re.search(pattern, text):
            secret_types.append(label)
    absolute_paths = sorted(set(re.findall(r"(?i)(?:[A-Z]:[\\/][^\r\n\"'<>|]{2,}|/(?:home|Users)/[^\r\n\"'<>|]{2,})", text)))
    return secret_types, absolute_paths[:100]


def publication_decision(artefact: str, rel: str, size: int, risks: list[str]) -> tuple[str, str]:
    lower = rel.lower()
    if risks:
        return "exclude", "suspected credential/private-data risk"
    if artefact in {"cache_or_environment", "raw_dataset_cache"}:
        return "manifest_only", "cache, environment state, or bulk licensed dataset"
    if artefact == "lora_checkpoint_binary":
        return "manifest_only", "model/checkpoint binary requires explicit publication approval"
    if artefact in {"smoke_output", "diagnostic_output", "legacy_output"}:
        return "diagnostics", "retain only as non-core diagnostic evidence"
    if size >= 100 * 1024 * 1024:
        return "release_or_lfs", "publication-safe candidate exceeds ordinary Git threshold"
    if artefact == "unknown_manual_review":
        return "manual_review", "unclassified artefact"
    if any(x in lower for x in (".env", "credential", "private")):
        return "manual_review", "risk-bearing filename requires review"
    return "include_git", "publication-safe candidate subject to core selection and deduplication"


def write_csv(path: Path, rows: list[dict], fields: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fields is None:
        fields = list(rows[0]) if rows else []
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source_root", type=Path)
    parser.add_argument("audit_root", type=Path)
    args = parser.parse_args()
    source = args.source_root.resolve(strict=True)
    out = args.audit_root.resolve()
    if source == out or source in out.parents:
        raise SystemExit("audit output must not be inside the read-only source")
    out.mkdir(parents=True, exist_ok=True)

    source_for_io = Path("\\\\?\\" + str(source)) if os.name == "nt" else source
    files: list[tuple[Path, Path]] = []
    for directory, _subdirectories, filenames in os.walk(source_for_io):
        directory_path = Path(directory)
        for filename in filenames:
            io_path = directory_path / filename
            relative_path = Path(os.path.relpath(io_path, source_for_io))
            files.append((io_path, relative_path))
    files.sort(key=lambda item: str(item[1]).lower())
    rows = []
    absolute_rows = []
    failures = []
    for index, (path, relative_path) in enumerate(files, 1):
        rel = relative_path.as_posix()
        display_path = source / relative_path
        stat = path.stat()
        suffix = path.suffix.lower()
        try:
            digest = sha256_file(path)
        except OSError as exc:
            digest = ""
            failures.append({"source_relative_path": rel, "error": str(exc)})
        artefact, stage = classify(rel, suffix)
        markers = [m for m in DIAGNOSTIC_MARKERS if m in rel.lower()]
        secret_types, occurrences = scan_text_risks(path, stat.st_size)
        filename_risk = [x for x in ("key", "token", "secret", "credential", ".env") if x in path.name.lower()]
        risks = sorted(set(secret_types + (["risk_bearing_filename"] if filename_risk else [])))
        action, rationale = publication_decision(artefact, rel, stat.st_size, risks)
        model = detect_model(rel)
        language = detect_language(rel)
        prompt = detect_prompt(rel)
        count = detect_sample_count(rel)
        proposed = ""
        if model and language and prompt and artefact in {"raw_generation", "automatic_evaluation_detailed", "automatic_evaluation_summary", "code_grounded_detailed", "code_grounded_summary"}:
            proposed = f"experiments/core_400/{model}/{language}/{prompt.lower()}/"
        row = {
            "absolute_source_path": str(display_path), "source_relative_path": rel, "filename": path.name,
            "extension": suffix, "size_bytes": stat.st_size,
            "modified_timestamp_utc": datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            "sha256": digest, "mime_or_logical_type": mimetypes.guess_type(path.name)[0] or "application/octet-stream",
            "implementation_stage": stage, "candidate_model_slug": model, "candidate_language": language,
            "candidate_prompt_regime": prompt, "candidate_sample_count": count,
            "candidate_artefact_type": artefact, "diagnostic_markers": ";".join(markers),
            "credential_or_private_risk": ";".join(risks), "absolute_path_count": len(occurrences),
            "proposed_destination": proposed, "publication_action": action, "rationale": rationale,
            "confidence_level": "high" if artefact != "unknown_manual_review" else "low",
            "manual_review": "YES" if action in {"manual_review", "exclude"} or failures and not digest else "NO",
        }
        rows.append(row)
        for occurrence in occurrences:
            absolute_rows.append({"source_relative_path": rel, "path_kind": "absolute_path", "matched_path_redacted": re.sub(r"(?i)([A-Z]:[\\/](?:Users|Pavan)[\\/])[^\\/]+", r"\1<redacted>", occurrence)})
        if index % 250 == 0:
            print(f"inventoried {index}/{len(files)}", flush=True)

    fields = list(rows[0]) if rows else []
    write_csv(out / "all_source_files.csv", rows, fields)
    (out / "all_source_files.json").write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")

    by_hash = defaultdict(list)
    for row in rows:
        if row["sha256"]:
            by_hash[row["sha256"]].append(row)
    duplicate_rows = []
    for group_num, (digest, members) in enumerate(sorted((x for x in by_hash.items() if len(x[1]) > 1), key=lambda x: (-len(x[1]), x[0])), 1):
        for member in members:
            duplicate_rows.append({"duplicate_group": group_num, "sha256": digest, "group_size": len(members), "size_bytes": member["size_bytes"], "source_relative_path": member["source_relative_path"]})
    write_csv(out / "sha256_duplicate_groups.csv", duplicate_rows, ["duplicate_group", "sha256", "group_size", "size_bytes", "source_relative_path"])

    logical = defaultdict(list)
    for row in rows:
        key = (row["candidate_model_slug"], row["candidate_language"], row["candidate_prompt_regime"], row["candidate_artefact_type"])
        if all(key[:3]) and key[3] not in {"unknown_manual_review", "diagnostic_output", "smoke_output", "legacy_output"}:
            logical[key].append(row)
    logical_rows = []
    for group_num, (key, members) in enumerate(sorted((x for x in logical.items() if len(x[1]) > 1), key=lambda x: x[0]), 1):
        for member in members:
            logical_rows.append({"logical_group": group_num, "model_slug": key[0], "language": key[1], "prompt_regime": key[2], "artefact_type": key[3], "candidate_sample_count": member["candidate_sample_count"], "size_bytes": member["size_bytes"], "sha256": member["sha256"], "diagnostic_markers": member["diagnostic_markers"], "source_relative_path": member["source_relative_path"]})
    write_csv(out / "logical_duplicate_groups.csv", logical_rows, ["logical_group", "model_slug", "language", "prompt_regime", "artefact_type", "candidate_sample_count", "size_bytes", "sha256", "diagnostic_markers", "source_relative_path"])

    write_csv(out / "absolute_path_occurrences.csv", absolute_rows, ["source_relative_path", "path_kind", "matched_path_redacted"])
    large = [r for r in rows if int(r["size_bytes"]) >= 50 * 1024 * 1024]
    write_csv(out / "large_file_inventory.csv", large, fields)
    unknown = [r for r in rows if r["manual_review"] == "YES" or r["candidate_artefact_type"] == "unknown_manual_review"]
    write_csv(out / "unknown_files_requiring_review.csv", unknown, fields)
    scripts = [r for r in rows if r["candidate_artefact_type"] in {"source_code", "automation_command"}]
    write_csv(out / "candidate_scripts_by_stage.csv", scripts, fields)
    core_types = {"raw_generation", "automatic_evaluation_detailed", "automatic_evaluation_summary", "code_grounded_detailed", "code_grounded_summary", "prompt_artefact", "provider_request", "provider_response", "provider_batch_state", "run_log", "run_state"}
    candidates = [r for r in rows if r["candidate_artefact_type"] in core_types and any((r["candidate_model_slug"], r["candidate_language"], r["candidate_prompt_regime"]))]
    write_csv(out / "candidate_core_run_files.csv", candidates, fields)

    risk_rows = [r for r in rows if r["credential_or_private_risk"]]
    risk_lines = ["# Secret and Private File Report", "", "No secret values are reproduced in this report.", "", f"Suspected files: {len(risk_rows)}", ""]
    for row in risk_rows:
        risk_lines.append(f"- `{row['source_relative_path']}`: {row['credential_or_private_risk']}")
    (out / "secret_and_private_file_report.md").write_text("\n".join(risk_lines) + "\n", encoding="utf-8")

    type_counts = Counter(r["candidate_artefact_type"] for r in rows)
    action_counts = Counter(r["publication_action"] for r in rows)
    summary = [
        "# Source Discovery Summary", "", f"- Source root: `{source}`", f"- Scan time (UTC): {datetime.now(timezone.utc).isoformat()}",
        f"- Files inventoried: {len(rows)}", f"- Bytes inventoried: {sum(int(r['size_bytes']) for r in rows)}",
        f"- Files that could not be hashed: {len(failures)}", f"- Physical duplicate groups: {sum(1 for members in by_hash.values() if len(members) > 1)}",
        f"- Logical duplicate groups: {sum(1 for members in logical.values() if len(members) > 1)}", f"- Suspected credential/private files: {len(risk_rows)}",
        f"- Files containing detected absolute paths: {len(set(r['source_relative_path'] for r in absolute_rows))}", f"- Large files (>= 50 MiB): {len(large)}",
        f"- Unclassified/manual-review files: {len(unknown)}", "", "## Artefact type counts", "",
    ]
    summary.extend(f"- {key}: {value}" for key, value in sorted(type_counts.items()))
    summary.extend(["", "## Publication action counts", ""])
    summary.extend(f"- {key}: {value}" for key, value in sorted(action_counts.items()))
    summary.extend(["", "## Scan completeness", "", "All filesystem entries returned by the recursive source traversal were processed." if not failures else "Some files could not be read; see scan_failures.json. Phase gate: FAIL.", ""])
    (out / "source_discovery_summary.md").write_text("\n".join(summary), encoding="utf-8")
    (out / "scan_failures.json").write_text(json.dumps(failures, indent=2), encoding="utf-8")
    print(json.dumps({"files": len(rows), "bytes": sum(int(r["size_bytes"]) for r in rows), "failures": len(failures), "risk_files": len(risk_rows), "manual_review": len(unknown), "duplicate_groups": len(duplicate_rows)}))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
