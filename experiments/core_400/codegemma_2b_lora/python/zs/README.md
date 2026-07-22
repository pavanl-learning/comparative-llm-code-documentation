# CodeGemma 2B LoRA Multilingual — python — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b_lora__python__zs` |
| Full model display name | CodeGemma 2B LoRA Multilingual |
| Raw model identifier | `codegemma_2b_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/zs/prompt_input_400.jsonl](../../../../../prompts/core_400/python/zs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/codegemma_2b_lora/python/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_python_400_v1.jsonl --base-model google/codegemma-2b --adapter-path ${ADAPTER_ROOT}/codegemma_2b_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/2a91692c4753_codegemma_2b_lora_multilang_P1_zero_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/e11cabe07d49_codegemma_2b_lora_multilang_P1_zero_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b_lora/python/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b_lora/python/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b_lora/python/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b_lora/python/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b_lora/python/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b_lora/python/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b_lora/python/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b_lora/python/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b_lora/python/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b_lora/python/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
396dc77da7df4e48cb52fe87c908b9a4b52174670072eef1918c3ac9f2d6bfee  experiments/core_400/codegemma_2b_lora/python/zs/generation/raw_generations.jsonl
1b6335161d29f6a45f1e73575aae28b76df11210c8968bf048239c5cc5bb85b5  experiments/core_400/codegemma_2b_lora/python/zs/assessment/automatic_detailed.jsonl
e78c0600b89e4ab4a657adcf9b3bd5856e2b0d7afb7a67f9b2e8dde4edc282c4  experiments/core_400/codegemma_2b_lora/python/zs/assessment/automatic_summary.json
a268c4ec0687644ba83ceed059c239e342acb9df816f9483f09fccfdeb0bc4f7  experiments/core_400/codegemma_2b_lora/python/zs/assessment/code_grounded_detailed.jsonl
97fc0371e8bb23fe7b5e426c4cf140aaa37320a3e7dac388f75a32fac6849c69  experiments/core_400/codegemma_2b_lora/python/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
