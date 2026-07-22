#!/usr/bin/env python3

import argparse
import json
from pathlib import Path
from typing import Dict, List, Set, Any


SOURCE_FILES = {
    "python": "data/processed/prompted_shots/P1_zero_shot_python_400_ZS.jsonl",
    "java": "data/processed/prompted_shots/P1_zero_shot_java_400_ZS.jsonl",
    "javascript": "data/processed/prompted_shots/P1_zero_shot_javascript_400_ZS.jsonl",
}

GENERATION_FILES = {
    "M1": {
        "python": "outputs/raw_generations/gemma_2_2b_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/gemma_2_2b_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/gemma_2_2b_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M2": {
        "python": "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M3": {
        "python": "outputs/raw_generations/codegemma_2b_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/codegemma_2b_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/codegemma_2b_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M4": {
        "python": "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M5": {
        "python": "outputs/raw_generations/gpt_5_1_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/gpt_5_1_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/gpt_5_1_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M6": {
        "python": "outputs/raw_generations/gpt_5_4_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/gpt_5_4_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/gpt_5_4_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M7": {
        "python": "outputs/raw_generations/gpt_5_1_codex_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/gpt_5_1_codex_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/gpt_5_1_codex_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M8": {
        "python": "outputs/raw_generations/gpt_5_3_codex_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/gpt_5_3_codex_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/gpt_5_3_codex_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M9": {
        "python": "outputs/raw_generations/gemini_3_flash_preview_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/gemini_3_flash_preview_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/gemini_3_flash_preview_P1_zero_shot_javascript_400_v1.jsonl",
    },
    "M10": {
        "python": "outputs/raw_generations/deepseek_chat_v32_P1_zero_shot_python_400_v1.jsonl",
        "java": "outputs/raw_generations/deepseek_chat_v32_P1_zero_shot_java_400_v1.jsonl",
        "javascript": "outputs/raw_generations/deepseek_chat_v32_P1_zero_shot_javascript_400_v1.jsonl",
    },
}


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def load_ids_from_jsonl(path: Path) -> Set[str]:
    return {str(r["sample_id"]) for r in load_jsonl(path) if "sample_id" in r}


def load_selected_ids(path: Path) -> List[str]:
    with path.open("r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def infer_language(sample_id: str) -> str:
    if sample_id.startswith("python_"):
        return "python"
    if sample_id.startswith("javascript_"):
        return "javascript"
    if sample_id.startswith("java_"):
        return "java"
    raise ValueError(f"Cannot infer language from sample_id: {sample_id}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project_root", default=".")
    parser.add_argument("--selected_ids", required=True)
    parser.add_argument("--report_json", required=True)
    args = parser.parse_args()

    root = Path(args.project_root).resolve()
    selected_ids_path = Path(args.selected_ids).resolve()
    report_json_path = Path(args.report_json).resolve()

    if not selected_ids_path.exists():
        raise FileNotFoundError(f"Selected IDs file not found: {selected_ids_path}")

    selected_ids = load_selected_ids(selected_ids_path)

    source_id_sets: Dict[str, Set[str]] = {}
    for lang, rel in SOURCE_FILES.items():
        path = root / rel
        if not path.exists():
            raise FileNotFoundError(f"Missing source file: {path}")
        source_id_sets[lang] = load_ids_from_jsonl(path)

    generation_id_sets: Dict[str, Dict[str, Set[str]]] = {}
    missing_files = []
    for alias, lang_map in GENERATION_FILES.items():
        generation_id_sets[alias] = {}
        for lang, rel in lang_map.items():
            path = root / rel
            if not path.exists():
                missing_files.append(str(path))
                generation_id_sets[alias][lang] = set()
            else:
                generation_id_sets[alias][lang] = load_ids_from_jsonl(path)

    report: Dict[str, Any] = {
        "num_selected_ids": len(selected_ids),
        "missing_files": missing_files,
        "missing_in_source": [],
        "missing_in_models": {},
        "all_valid": True,
    }

    for sid in selected_ids:
        lang = infer_language(sid)
        if sid not in source_id_sets[lang]:
            report["missing_in_source"].append({"sample_id": sid, "language": lang})
            report["all_valid"] = False

    for alias in sorted(GENERATION_FILES.keys()):
        missing = []
        for sid in selected_ids:
            lang = infer_language(sid)
            if sid not in generation_id_sets[alias][lang]:
                missing.append({"sample_id": sid, "language": lang})
        report["missing_in_models"][alias] = missing
        if missing:
            report["all_valid"] = False

    report_json_path.parent.mkdir(parents=True, exist_ok=True)
    with report_json_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"Wrote {report_json_path}")
    print(f"Selected IDs: {len(selected_ids)}")
    print(f"Missing source rows: {len(report['missing_in_source'])}")
    for alias in sorted(report["missing_in_models"].keys()):
        print(f"{alias} missing rows: {len(report['missing_in_models'][alias])}")
    if missing_files:
        print(f"Missing files: {len(missing_files)}")
    print(f"All valid: {report['all_valid']}")


if __name__ == "__main__":
    main()