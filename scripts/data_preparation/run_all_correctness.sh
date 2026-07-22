#!/usr/bin/env bash
set -euo pipefail

mkdir -p outputs/correctness

for f in outputs/raw_generations/*.jsonl; do
  base="$(basename "$f" .jsonl)"
  src=""

  case "$base" in
    *_P1_zero_shot_python_*)
      src="data/processed/prompted_shots/P1_zero_shot_python_400_ZS.jsonl"
      ;;
    *_P1_zero_shot_java_*)
      src="data/processed/prompted_shots/P1_zero_shot_java_400_ZS.jsonl"
      ;;
    *_P1_zero_shot_javascript_*)
      src="data/processed/prompted_shots/P1_zero_shot_javascript_400_ZS.jsonl"
      ;;
    *_P1_one_shot_python_*)
      src="data/processed/prompted_shots/P1_one_shot_python_400.jsonl"
      ;;
    *_P1_one_shot_java_*)
      src="data/processed/prompted_shots/P1_one_shot_java_400.jsonl"
      ;;
    *_P1_one_shot_javascript_*)
      src="data/processed/prompted_shots/P1_one_shot_javascript_400.jsonl"
      ;;
    *_P1_few_shot_python_*)
      src="data/processed/prompted_shots/P1_few_shot_python_400.jsonl"
      ;;
    *_P1_few_shot_java_*)
      src="data/processed/prompted_shots/P1_few_shot_java_400.jsonl"
      ;;
    *_P1_few_shot_javascript_*)
      src="data/processed/prompted_shots/P1_few_shot_javascript_400.jsonl"
      ;;
    *)
      echo "Skipping unmatched file: $base"
      continue
      ;;
  esac

  if [ ! -f "$src" ]; then
    echo "Missing source file for $base -> $src"
    continue
  fi

  if [ ! -s "$f" ]; then
    echo "Skipping empty file: $f"
    continue
  fi

  if [ "$(grep -cve '^[[:space:]]*$' "$f")" -eq 0 ]; then
    echo "Skipping file with no non-empty JSONL rows: $f"
    continue
  fi

  echo "=================================================="
  echo "Running correctness evaluation for: $base"
  echo "Source: $src"
  echo "=================================================="

  python scripts/evaluate_code_grounded_correctness.py \
    --input "$f" \
    --source "$src" \
    --output-prefix "outputs/correctness/${base}_correctness.json" \
  || echo "Failed correctness evaluation for: $base"
done