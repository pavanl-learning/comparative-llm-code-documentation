#!/usr/bin/env bash
set -euo pipefail

mkdir -p outputs/correctness

JOBS=(
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl|data/processed/prompted_shots/P1_zero_shot_python_400_ZS.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl|data/processed/prompted_shots/P1_zero_shot_javascript_400_ZS.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl|data/processed/prompted_shots/P1_zero_shot_java_400_ZS.jsonl"

  "outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_python_400_v1.jsonl|data/processed/prompted_shots/P1_few_shot_python_400_FS.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl|data/processed/prompted_shots/P1_few_shot_javascript_400_FS.jsonl"
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_java_400_v1.jsonl|data/processed/prompted_shots/P1_few_shot_java_400_FS.jsonl"

  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl|data/processed/prompted_shots/P1_zero_shot_python_400_ZS.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl|data/processed/prompted_shots/P1_zero_shot_javascript_400_ZS.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl|data/processed/prompted_shots/P1_zero_shot_java_400_ZS.jsonl"

  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_python_400_v1.jsonl|data/processed/prompted_shots/P1_few_shot_python_400_FS.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl|data/processed/prompted_shots/P1_few_shot_javascript_400_FS.jsonl"
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1.jsonl|data/processed/prompted_shots/P1_few_shot_java_400_FS.jsonl"
)

for job in "${JOBS[@]}"; do
  IFS="|" read -r input_file source_file <<< "$job"

  if [[ ! -f "$input_file" ]]; then
    echo "Missing generation file, skipping: $input_file"
    continue
  fi

  if [[ ! -f "$source_file" ]]; then
    echo "Missing source file, skipping: $source_file"
    continue
  fi

  rows="$(wc -l < "$input_file" | tr -d ' ')"
  if [[ "$rows" != "400" ]]; then
    echo "Incomplete generation file, skipping: $input_file"
    echo "Rows found: $rows, expected: 400"
    continue
  fi

  base="$(basename "$input_file" .jsonl)"
  output_prefix="outputs/correctness/${base}_correctness"

  summary_file="${output_prefix}_summary.json"
  detailed_file="${output_prefix}_detailed.jsonl"

  if [[ -f "$summary_file" && -f "$detailed_file" ]]; then
    echo "Correctness already exists, skipping: $base"
    continue
  fi

  echo "============================================================"
  echo "Running code-grounded correctness"
  echo "Input:  $input_file"
  echo "Source: $source_file"
  echo "Prefix: $output_prefix"
  echo "============================================================"

  python scripts/evaluate_code_grounded_correctness.py \
    --input "$input_file" \
    --source "$source_file" \
    --output-prefix "$output_prefix"

  echo "Completed: $summary_file"
  echo
done

echo "All Qwen base ZS/FS 400 correctness evaluations checked."
