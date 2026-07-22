import json
import random
from pathlib import Path

from datasets import load_dataset
from tqdm import tqdm

SEED = 42
LANGUAGES = ["python", "java", "javascript"]
SAMPLES_PER_LANGUAGE = 5000

MIN_CODE_LINES = 3
MAX_CODE_LINES = 80
MIN_DOC_CHARS = 20
MAX_DOC_CHARS = 400

OUTPUT_DIR = Path("data/processed")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

RAW_CACHE_DIR = Path("data/raw/hf_cache")
RAW_CACHE_DIR.mkdir(parents=True, exist_ok=True)


def clean_text(text: str) -> str:
    if text is None:
        return ""
    return " ".join(text.strip().split())


def line_count(text: str) -> int:
    if not text:
        return 0
    return len([ln for ln in text.splitlines() if ln.strip()])


def is_valid_example(example: dict) -> bool:
    code = clean_text(example.get("func_code_string", ""))
    doc = clean_text(example.get("func_documentation_string", ""))
    func_name = clean_text(example.get("func_name", ""))

    if not code or not doc:
        return False

    if len(doc) < MIN_DOC_CHARS or len(doc) > MAX_DOC_CHARS:
        return False

    code_lines = line_count(example.get("func_code_string", ""))
    if code_lines < MIN_CODE_LINES or code_lines > MAX_CODE_LINES:
        return False

    lowered_doc = doc.lower()
    bad_docs = {
        "todo",
        "test",
        "none",
        "n/a",
        "deprecated",
    }
    if lowered_doc in bad_docs:
        return False

    if func_name and doc.lower() == func_name.lower():
        return False

    return True


def normalize_example(example: dict, language: str, idx: int) -> dict:
    code = example.get("func_code_string", "").rstrip()
    doc = clean_text(example.get("func_documentation_string", ""))
    func_name = clean_text(example.get("func_name", ""))

    sample_id = f"{language}_{idx:06d}"

    return {
        "sample_id": sample_id,
        "language": language,
        "repository_name": example.get("repository_name", ""),
        "func_path_in_repository": example.get("func_path_in_repository", ""),
        "func_name": func_name,
        "code": code,
        "reference_documentation": doc,
        "code_line_count": line_count(code),
        "split_name": example.get("split_name", "train"),
        "source_dataset": "code_search_net",
    }


def main():
    random.seed(SEED)

    all_selected = []
    summary = {}

    for language in LANGUAGES:
        print(f"\nLoading language: {language}")
        ds = load_dataset(
            "code_search_net",
            language,
            split="train",
            cache_dir=str(RAW_CACHE_DIR),
        )

        print(f"Loaded {len(ds)} raw train rows for {language}")

        filtered = []
        seen_keys = set()

        for ex in tqdm(ds, desc=f"Filtering {language}"):
            if not is_valid_example(ex):
                continue

            code = ex.get("func_code_string", "").strip()
            doc = clean_text(ex.get("func_documentation_string", ""))
            dedup_key = (code, doc)

            if dedup_key in seen_keys:
                continue
            seen_keys.add(dedup_key)

            filtered.append(ex)

        print(f"Kept {len(filtered)} filtered rows for {language}")

        random.shuffle(filtered)
        chosen = filtered[:SAMPLES_PER_LANGUAGE]

        if len(chosen) < SAMPLES_PER_LANGUAGE:
            raise ValueError(
                f"Not enough filtered examples for {language}: "
                f"needed {SAMPLES_PER_LANGUAGE}, got {len(chosen)}"
            )

        normalized = [
            normalize_example(ex, language, i + 1)
            for i, ex in enumerate(chosen)
        ]

        all_selected.extend(normalized)
        summary[language] = {
            "raw_train_rows": len(ds),
            "filtered_rows": len(filtered),
            "selected_rows": len(normalized),
        }

    random.shuffle(all_selected)

    out_jsonl = OUTPUT_DIR / "codesearchnet_balanced_15000.jsonl"
    with out_jsonl.open("w", encoding="utf-8") as f:
        for row in all_selected:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    out_summary = OUTPUT_DIR / "codesearchnet_balanced_15000_summary.json"
    with out_summary.open("w", encoding="utf-8") as f:
        json.dump(
            {
                "seed": SEED,
                "languages": LANGUAGES,
                "samples_per_language": SAMPLES_PER_LANGUAGE,
                "min_code_lines": MIN_CODE_LINES,
                "max_code_lines": MAX_CODE_LINES,
                "min_doc_chars": MIN_DOC_CHARS,
                "max_doc_chars": MAX_DOC_CHARS,
                "summary": summary,
                "total_selected": len(all_selected),
            },
            f,
            indent=2,
        )

    print("\nDone.")
    print(f"Wrote: {out_jsonl}")
    print(f"Wrote: {out_summary}")
    print(f"Total selected samples: {len(all_selected)}")


if __name__ == "__main__":
    main()
