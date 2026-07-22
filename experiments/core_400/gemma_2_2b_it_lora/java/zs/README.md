# Gemma 2 2B IT LoRA Multilingual — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it_lora__java__zs` |
| Full model display name | Gemma 2 2B IT LoRA Multilingual |
| Raw model identifier | `gemma_2_2b_it_lora_multilang` |
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
- Command file: [experiments/core_400/gemma_2_2b_it_lora/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_zero_shot_java_400_v1.jsonl --base-model google/gemma-2-2b-it --adapter-path ${ADAPTER_ROOT}/gemma_2_2b_it_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/670bfc675768_gemma_2_2b_it_lora_multilang_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/e959266be815_gemma_2_2b_it_lora_multilang_P1_zero_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it_lora/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it_lora/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it_lora/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it_lora/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it_lora/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it_lora/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
c54cb96714c84e74671d1a5b116f6c5f7a05006770bde74daa509d97b5d38990  experiments/core_400/gemma_2_2b_it_lora/java/zs/generation/raw_generations.jsonl
5c5ea49baf9201ee46718c6c18ad42bd1009eadacf0afaa4d0f3e1bb12c4b32f  experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/automatic_detailed.jsonl
dd6b0b963844f1eaad4936f1ec628f7f3070b1a99bc25df65f21e2641160ba4b  experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/automatic_summary.json
60c52637dba5db8b7a9f7bc71d0e8d11717caa85118f262bcbce84e6c94f3b43  experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/code_grounded_detailed.jsonl
8b45712ec926ee7a555940bc0ba8b69b06f20b3bf8a4b8848460e6bebc36996d  experiments/core_400/gemma_2_2b_it_lora/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
