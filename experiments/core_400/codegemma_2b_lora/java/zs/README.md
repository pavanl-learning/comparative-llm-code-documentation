# CodeGemma 2B LoRA Multilingual — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b_lora__java__zs` |
| Full model display name | CodeGemma 2B LoRA Multilingual |
| Raw model identifier | `codegemma_2b_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | java |
| Prompt regime | ZS |
| Validation status | PASS |

## Row-count validation

| Artefact | Expected | Observed |
|---|---:|---:|
| Raw generations | 400 | 400 |
| Automatic detailed evaluation | 400 | 400 |
| Code-grounded detailed evaluation | 400 | 400 |

Sample-ID alignment: `True`.

## Inputs and execution

- Prompt input file: [prompts/core_400/java/zs/prompt_input_400.jsonl](../../../../../prompts/core_400/java/zs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/codegemma_2b_lora/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_java_400_v1.jsonl --base-model google/codegemma-2b --adapter-path ${ADAPTER_ROOT}/codegemma_2b_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/270741d35bb9_codegemma_2b_lora_multilang_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/3e1aadbf72d2_codegemma_2b_lora_multilang_P1_zero_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b_lora/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b_lora/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b_lora/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b_lora/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b_lora/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b_lora/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b_lora/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b_lora/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b_lora/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b_lora/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
08e219f66a40518c7c8ceca0c762bf7c5b5984ca2bd6831123a603c9d28f01fc  experiments/core_400/codegemma_2b_lora/java/zs/generation/raw_generations.jsonl
884cbc2eb03819afea5c04535f9bda60f957b7b8db303213f1320629856844a9  experiments/core_400/codegemma_2b_lora/java/zs/assessment/automatic_detailed.jsonl
ad6cc2fe2e66d3f59b8a99b8da87adcadb3671516d4b5236235fe8ab728e7215  experiments/core_400/codegemma_2b_lora/java/zs/assessment/automatic_summary.json
1a15a8843d07ac38f5215b0f78d8d579c095460f087295e256d7f70f1114106c  experiments/core_400/codegemma_2b_lora/java/zs/assessment/code_grounded_detailed.jsonl
a43d789e923617daf65a0f1d7eb30ff8c7637882c885ad3b288965e8a806c9d6  experiments/core_400/codegemma_2b_lora/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
