# Gemma 2 2B IT LoRA Multilingual — python — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it_lora__python__os` |
| Full model display name | Gemma 2 2B IT LoRA Multilingual |
| Raw model identifier | `gemma_2_2b_it_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | python |
| Prompt regime | OS |
| Validation status | PASS |

## Row-count validation

| Artefact | Expected | Observed |
|---|---:|---:|
| Raw generations | 400 | 400 |
| Automatic detailed evaluation | 400 | 400 |
| Code-grounded detailed evaluation | 400 | 400 |

Sample-ID alignment: `True`.

## Inputs and execution

- Prompt input file: [prompts/core_400/python/os/prompt_input_400.jsonl](../../../../../prompts/core_400/python/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/gemma_2_2b_it_lora/python/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_one_shot_python_400_v1.jsonl --base-model google/gemma-2-2b-it --adapter-path ${ADAPTER_ROOT}/gemma_2_2b_it_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_one_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/45a7659e10fa_gemma_2_2b_it_lora_multilang_P1_one_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_one_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/83406dbe4444_gemma_2_2b_it_lora_multilang_P1_one_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it_lora/python/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it_lora/python/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it_lora/python/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it_lora/python/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it_lora/python/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it_lora/python/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
77263b03ca67f6111dc19e933a88bb6e64072093c991c0e92d646f0a68b2a2ea  experiments/core_400/gemma_2_2b_it_lora/python/os/generation/raw_generations.jsonl
44559deb6d0347502627f6c6f4ea9cb508a09362d324807458a4c44808571c68  experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/automatic_detailed.jsonl
0f2b6ef4f21da2cd672e4a6dfd307ca91cf150783395a3e29a855508fa3c41a6  experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/automatic_summary.json
3bbf5765b871a814538fe29d6a8f4e89fa196d867ee6f7952eb2a6c84d2619cc  experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/code_grounded_detailed.jsonl
4a214eeec85db5911a0fdcf068564bd1b38f538117f0893b2791a27cfe50a006  experiments/core_400/gemma_2_2b_it_lora/python/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
