#!/usr/bin/env bash

set -euo pipefail

run_if_missing() {
  local model="$1"
  local input="$2"
  local output="$3"

  if [ -f "$output" ]; then
    echo "Skipping existing: $output"
  else
    echo "Running: $output"
    python scripts/run_generation_hf.py \
      --model "$model" \
      --input "$input" \
      --output "$output"
  fi
}

run_if_missing "Qwen/Qwen2.5-Coder-1.5B-Instruct" \
  "data/processed/prompted_shots/P1_one_shot_python_400.jsonl" \
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_one_shot_python_400_v1.jsonl"

run_if_missing "Qwen/Qwen2.5-Coder-1.5B-Instruct" \
  "data/processed/prompted_shots/P1_one_shot_javascript_400.jsonl" \
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired.jsonl"

run_if_missing "Qwen/Qwen2.5-Coder-1.5B-Instruct" \
  "data/processed/prompted_shots/P1_one_shot_java_400.jsonl" \
  "outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_one_shot_java_400_v1.jsonl"

run_if_missing "Qwen/Qwen2.5-1.5B-Instruct" \
  "data/processed/prompted_shots/P1_one_shot_python_400.jsonl" \
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_one_shot_python_400_v1.jsonl"

run_if_missing "Qwen/Qwen2.5-1.5B-Instruct" \
  "data/processed/prompted_shots/P1_one_shot_javascript_400.jsonl" \
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_one_shot_javascript_400_v1.jsonl"

run_if_missing "Qwen/Qwen2.5-1.5B-Instruct" \
  "data/processed/prompted_shots/P1_one_shot_java_400.jsonl" \
  "outputs/raw_generations/qwen25_1_5b_instruct_P1_one_shot_java_400_v1.jsonl"

run_if_missing "google/gemma-2-2b-it" \
  "data/processed/prompted_shots/P1_one_shot_python_400.jsonl" \
  "outputs/raw_generations/gemma_2_2b_it_P1_one_shot_python_400_v1.jsonl"

run_if_missing "google/gemma-2-2b-it" \
  "data/processed/prompted_shots/P1_one_shot_javascript_400.jsonl" \
  "outputs/raw_generations/gemma_2_2b_it_P1_one_shot_javascript_400_v1.jsonl"

run_if_missing "google/gemma-2-2b-it" \
  "data/processed/prompted_shots/P1_one_shot_java_400.jsonl" \
  "outputs/raw_generations/gemma_2_2b_it_P1_one_shot_java_400_v1.jsonl"

run_if_missing "google/codegemma-2b" \
  "data/processed/prompted_shots/P1_one_shot_python_400.jsonl" \
  "outputs/raw_generations/codegemma_2b_P1_one_shot_python_400_v1.jsonl"

run_if_missing "google/codegemma-2b" \
  "data/processed/prompted_shots/P1_one_shot_javascript_400.jsonl" \
  "outputs/raw_generations/codegemma_2b_P1_one_shot_javascript_400_v1.jsonl"

run_if_missing "google/codegemma-2b" \
  "data/processed/prompted_shots/P1_one_shot_java_400.jsonl" \
  "outputs/raw_generations/codegemma_2b_P1_one_shot_java_400_v1.jsonl"

echo "All requested one-shot 400 runs checked."