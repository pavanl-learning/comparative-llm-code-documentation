#!/usr/bin/env bash
set -euo pipefail

mkdir -p outputs/evaluations

for f in outputs/raw_generations/*.jsonl; do
  base="$(basename "$f" .jsonl)"

  if [ ! -s "$f" ]; then
    echo "Skipping empty file: $f"
    continue
  fi

  if [ "$(grep -cve '^[[:space:]]*$' "$f")" -eq 0 ]; then
    echo "Skipping file with no non-empty JSONL rows: $f"
    continue
  fi

  echo "=================================================="
  echo "Running text evaluation for: $base"
  echo "=================================================="

  python scripts/evaluate_generations.py \
    --input "$f" \
    --output-prefix "outputs/evaluations/${base}_eval.json" \
  || echo "Failed text evaluation for: $base"
done