#!/usr/bin/env bash
set -euo pipefail

mkdir -p outputs/raw_generations
mkdir -p outputs/evaluations

# Base models only. No LoRA / no fine-tuning.
MODELS=(
  "Qwen/Qwen2.5-1.5B-Instruct|qwen25_1_5b_instruct"
  "Qwen/Qwen2.5-Coder-1.5B-Instruct|qwen25_coder_1_5b_instruct"
)

LANGUAGES=(
  "python"
  "javascript"
  "java"
)

SHOTS=(
  "zero_shot|ZS"
  "few_shot|FS"
)

find_input_file() {
  local shot_name="$1"
  local shot_code="$2"
  local lang="$3"

  local candidates=(
    "data/processed/prompted_shots/P1_${shot_name}_${lang}_400_${shot_code}.jsonl"
    "data/processed/prompted_shots/P1_${shot_name}_${lang}_400.jsonl"
    "data/processed/prompted/P1_${shot_name}_${lang}_400_${shot_code}.jsonl"
    "data/processed/prompted/P1_${shot_name}_${lang}_400.jsonl"
  )

  for f in "${candidates[@]}"; do
    if [[ -f "$f" ]]; then
      echo "$f"
      return 0
    fi
  done

  echo ""
  return 1
}

for model_entry in "${MODELS[@]}"; do
  IFS="|" read -r MODEL MODEL_SLUG <<< "$model_entry"

  for shot_entry in "${SHOTS[@]}"; do
    IFS="|" read -r SHOT_NAME SHOT_CODE <<< "$shot_entry"

    for LANG in "${LANGUAGES[@]}"; do
      INPUT_FILE="$(find_input_file "$SHOT_NAME" "$SHOT_CODE" "$LANG" || true)"

      if [[ -z "$INPUT_FILE" ]]; then
        echo "Missing input for ${MODEL_SLUG} ${SHOT_NAME} ${LANG}. Skipping."
        echo "Expected one of:"
        echo "  data/processed/prompted_shots/P1_${SHOT_NAME}_${LANG}_400_${SHOT_CODE}.jsonl"
        echo "  data/processed/prompted_shots/P1_${SHOT_NAME}_${LANG}_400.jsonl"
        echo "  data/processed/prompted/P1_${SHOT_NAME}_${LANG}_400_${SHOT_CODE}.jsonl"
        echo "  data/processed/prompted/P1_${SHOT_NAME}_${LANG}_400.jsonl"
        echo
        continue
      fi

      OUTPUT_FILE="outputs/raw_generations/${MODEL_SLUG}_P1_${SHOT_NAME}_${LANG}_400_v1.jsonl"

      if [[ -f "$OUTPUT_FILE" ]]; then
        echo "Skipping existing output: $OUTPUT_FILE"
        continue
      fi

      echo "============================================================"
      echo "Model: $MODEL"
      echo "Shot:  $SHOT_NAME"
      echo "Lang:  $LANG"
      echo "Input: $INPUT_FILE"
      echo "Out:   $OUTPUT_FILE"
      echo "============================================================"

      python scripts/run_generation_hf.py \
        --model "$MODEL" \
        --input "$INPUT_FILE" \
        --output "$OUTPUT_FILE"

      echo "Completed: $OUTPUT_FILE"
      echo
    done
  done
done

echo "All requested Qwen base-model zero-shot/few-shot generations checked."
