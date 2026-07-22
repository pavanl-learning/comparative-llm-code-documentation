#!/usr/bin/env bash
python scripts/finetune_qwen_lora.py \
  --train data/finetune/smoke_24_multilang.jsonl \
  --valid data/finetune/smoke_24_multilang.jsonl \
  --output-dir outputs/finetune/qwen25_coder_1_5b_lora_smoke