#!/usr/bin/env bash
python scripts/finetune_lora_multilang.py \
  --train data/finetune/smoke_24_multilang.jsonl \
  --valid data/finetune/smoke_24_multilang.jsonl \
  --model-name google/gemma-2-2b-it \
  --output-dir outputs/finetune/gemma_2_2b_it_lora_smoke
