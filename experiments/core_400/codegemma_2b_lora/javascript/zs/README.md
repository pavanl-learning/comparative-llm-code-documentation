# CodeGemma 2B LoRA Multilingual — javascript — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b_lora__javascript__zs` |
| Full model display name | CodeGemma 2B LoRA Multilingual |
| Raw model identifier | `codegemma_2b_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | javascript |
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

- Prompt input file: [prompts/core_400/javascript/zs/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/zs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/codegemma_2b_lora/javascript/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_javascript_400_v1.jsonl --base-model google/codegemma-2b --adapter-path ${ADAPTER_ROOT}/codegemma_2b_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/89492be77129_codegemma_2b_lora_multilang_P1_zero_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_zero_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/2fe56860627b_codegemma_2b_lora_multilang_P1_zero_shot_javascript_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b_lora/javascript/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b_lora/javascript/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b_lora/javascript/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b_lora/javascript/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b_lora/javascript/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b_lora/javascript/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
944c01f48a20fe95a69a573a1b0a21a6a75234eb5e8144e32809d3938e32ce98  experiments/core_400/codegemma_2b_lora/javascript/zs/generation/raw_generations.jsonl
a2e8aa3da24418faf7abe0ca37d91d112fd71aa2567b3de830e4194c583c8474  experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/automatic_detailed.jsonl
cbed588d097f1fe94b0437e922e68a59f57b558a2ff70487cd33524577dc2958  experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/automatic_summary.json
232dc1c505778b90b8af433fc4d23ca927097446a3aa17a80701a59cc106b1df  experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/code_grounded_detailed.jsonl
59383e39f2377183bd07e6a16538240feb09e879a1d26bc59d34fda74e444e36  experiments/core_400/codegemma_2b_lora/javascript/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
