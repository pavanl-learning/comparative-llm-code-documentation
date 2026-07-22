#!/usr/bin/env bash

set -euo pipefail

evaluate_if_missing() {
  local input="$1"
  local output_prefix="$2"

  if [ -f "${output_prefix}_summary.json" ]; then
    echo "Skipping existing: ${output_prefix}_summary.json"
  else
    echo "Evaluating: $input"
    python scripts/evaluate_generations.py \
      --input "$input" \
      --output "$output_prefix"
  fi
}

evaluate_if_missing \
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_one_shot_python_400_v1.jsonl" \
  "outputs/evaluations/qwen25_coder_1_5b_instruct_P1_one_shot_python_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired.jsonl" \
  "outputs/evaluations/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_one_shot_java_400_v2_rerun.jsonl" \
  "outputs/evaluations/qwen25_coder_1_5b_instruct_P1_one_shot_java_400_v2_rerun_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_one_shot_python_400_v1.jsonl" \
  "outputs/evaluations/qwen25_1_5b_instruct_P1_one_shot_python_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_one_shot_javascript_400_v1.jsonl" \
  "outputs/evaluations/qwen25_1_5b_instruct_P1_one_shot_javascript_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_one_shot_java_400_v1.jsonl" \
  "outputs/evaluations/qwen25_1_5b_instruct_P1_one_shot_java_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/gemma_2_2b_it_P1_one_shot_python_400_v1.jsonl" \
  "outputs/evaluations/gemma_2_2b_it_P1_one_shot_python_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/gemma_2_2b_it_P1_one_shot_javascript_400_v1.jsonl" \
  "outputs/evaluations/gemma_2_2b_it_P1_one_shot_javascript_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/gemma_2_2b_it_P1_one_shot_java_400_v1.jsonl" \
  "outputs/evaluations/gemma_2_2b_it_P1_one_shot_java_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/codegemma_2b_P1_one_shot_python_400_v1.jsonl" \
  "outputs/evaluations/codegemma_2b_P1_one_shot_python_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/codegemma_2b_P1_one_shot_javascript_400_v1.jsonl" \
  "outputs/evaluations/codegemma_2b_P1_one_shot_javascript_400_v1_eval.json"

evaluate_if_missing \
  "outputs/raw_generations/codegemma_2b_P1_one_shot_java_400_v1.jsonl" \
  "outputs/evaluations/codegemma_2b_P1_one_shot_java_400_v1_eval.json"

echo "All requested one-shot 400 evaluations checked."