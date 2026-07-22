#!/usr/bin/env bash
python scripts/finetune_lora_multilang.py \
  --train data/finetune/smoke_24_multilang.jsonl \
  --valid data/finetune/smoke_24_multilang.jsonl \
  --model-name google/codegemma-2b \
  --output-dir outputs/finetune/codegemma_2b_lora_smoke
