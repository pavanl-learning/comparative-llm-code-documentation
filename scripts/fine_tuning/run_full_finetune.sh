#!/usr/bin/env bash
python scripts/finetune_qwen_lora.py \
  --train data/finetune/train_3000_multilang.jsonl \
  --valid data/finetune/valid_300_multilang.jsonl \
  --output-dir outputs/finetune/qwen25_coder_1_5b_lora_multilang