#!/usr/bin/env bash
python scripts/finetune_lora_multilang.py \
  --train data/finetune/train_3000_multilang.jsonl \
  --valid data/finetune/valid_300_multilang.jsonl \
  --model-name google/gemma-2-2b-it \
  --output-dir outputs/finetune/gemma_2_2b_it_lora_multilang
