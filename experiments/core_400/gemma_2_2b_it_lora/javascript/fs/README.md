# Gemma 2 2B IT LoRA Multilingual — javascript — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it_lora__javascript__fs` |
| Full model display name | Gemma 2 2B IT LoRA Multilingual |
| Raw model identifier | `gemma_2_2b_it_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | javascript |
| Prompt regime | FS |
| Validation status | PASS |

## Row-count validation

| Artefact | Expected | Observed |
|---|---:|---:|
| Raw generations | 400 | 400 |
| Automatic detailed evaluation | 400 | 400 |
| Code-grounded detailed evaluation | 400 | 400 |

Sample-ID alignment: `True`.

## Inputs and execution

- Prompt input file: [prompts/core_400/javascript/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_few_shot_javascript_400_v1.jsonl --base-model google/gemma-2-2b-it --adapter-path ${ADAPTER_ROOT}/gemma_2_2b_it_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_few_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/6e9d63f16b22_gemma_2_2b_it_lora_multilang_P1_few_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_few_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/gemma_2_2b_it_lora_multilang_P1_few_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it_lora/javascript/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
3b644908aeb7391178fba8fa9e695143cc7a9356a6990382b2a13c256e460e9f  experiments/core_400/gemma_2_2b_it_lora/javascript/fs/generation/raw_generations.jsonl
31cbeac95efc286f3fec6810bc55d1e1bdab1eb5c377c6afb9e0e27d665b5b35  experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/automatic_detailed.jsonl
29de19dd1ed6a057959b5a84f8659b556ce920e78413082d2422e655298d9171  experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/automatic_summary.json
ded2f2efb0005ad608ba51c168935b20a38e36a42b21cd1308f7337580e575fe  experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/code_grounded_detailed.jsonl
7974e224b564076570cf614e02fa84e7f173880157ccdd32525a3d95c42ff5f4  experiments/core_400/gemma_2_2b_it_lora/javascript/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
