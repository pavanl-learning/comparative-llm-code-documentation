#!/usr/bin/env bash
python scripts/finetune_lora_multilang.py \
  --train data/finetune/train_3000_multilang.jsonl \
  --valid data/finetune/valid_300_multilang.jsonl \
  --model-name Qwen/Qwen2.5-1.5B-Instruct \
  --output-dir outputs/finetune/qwen25_1_5b_instruct_lora_multilang
