#!/usr/bin/env bash
set -euo pipefail

mkdir -p outputs/evaluations

# Evaluate Qwen2.5-1.5B-Instruct and Qwen2.5-Coder-1.5B-Instruct
# for zero-shot and few-shot 400-sample outputs across python, javascript, and java.

FILES=(
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_python_400_v1.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_java_400_v1.jsonl"

  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_python_400_v1.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1.jsonl"
)

for input_file in "${FILES[@]}"; do
  if [[ ! -f "$input_file" ]]; then
    echo "Missing generation file, skipping: $input_file"
    continue
  fi

  rows="$(wc -l < "$input_file" | tr -d ' ')"
  if [[ "$rows" != "400" ]]; then
    echo "Incomplete generation file, skipping: $input_file"
    echo "Rows found: $rows, expected: 400"
    continue
  fi

  base="$(basename "$input_file" .jsonl)"
  output_prefix="outputs/evaluations/${base}_eval.json"
  summary_file="${output_prefix}_summary.json"
  detailed_file="${output_prefix}_detailed.jsonl"

  if [[ -f "$summary_file" && -f "$detailed_file" ]]; then
    echo "Evaluation already exists, skipping: $summary_file"
    continue
  fi

  echo "============================================================"
  echo "Evaluating: $input_file"
  echo "Output prefix: $output_prefix"
  echo "============================================================"

  python scripts/evaluate_generations.py \
    --input "$input_file" \
    --output-prefix "$output_prefix"

  echo "Completed evaluation: $summary_file"
  echo
done

echo "All Qwen base zero-shot/few-shot 400-sample evaluations checked."
