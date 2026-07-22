#!/usr/bin/env bash

OUT_BASE="outputs/evaluation_And_corrctness_may2026_1/saturation_experiment"
LOG_FILE="${OUT_BASE}/saturation_eval_log.txt"

mkdir -p "$OUT_BASE"
: > "$LOG_FILE"

FILES=(
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_100_v1.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_200_v1.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_300_ZS_v3.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_500_ZS_v3.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_600_v1.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_800_v1.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_1000_ZS_v3.jsonl"
  "outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_zero_shot_python_1200_v1.jsonl"
)

for input_file in "${FILES[@]}"; do

  if [ ! -f "$input_file" ]; then
    echo "MISSING raw file: $input_file" | tee -a "$LOG_FILE"
    continue
  fi

  rows=$(wc -l < "$input_file")

  rel_name=$(basename "$input_file" .jsonl)

  out_prefix="${OUT_BASE}/${rel_name}"
  code_prefix="${OUT_BASE}/${rel_name}_code_grounded"

  src="data/processed/prompted_shots/P1_zero_shot_python_400_ZS.jsonl"

  echo "========================================" | tee -a "$LOG_FILE"
  echo "Input:  $input_file" | tee -a "$LOG_FILE"
  echo "Rows:   $rows" | tee -a "$LOG_FILE"
  echo "Output: $out_prefix" | tee -a "$LOG_FILE"
  echo "========================================" | tee -a "$LOG_FILE"

  python scripts/evaluate_generations.py \
    --input "$input_file" \
    --output-prefix "$out_prefix"

  if [ $? -ne 0 ]; then
    echo "ERROR lexical failed: $input_file" | tee -a "$LOG_FILE"
    continue
  fi

  python scripts/evaluate_code_grounded_correctness.py \
    --input "$input_file" \
    --source "$src" \
    --output-prefix "$code_prefix"

  if [ $? -ne 0 ]; then
    echo "ERROR code-grounded failed: $input_file" | tee -a "$LOG_FILE"
    continue
  fi

done

echo "Done."
echo "Log file: $LOG_FILE"
