# Qwen2.5 Coder 1.5B Instruct LoRA Multilingual — python — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_coder_1_5b_instruct_lora__python__fs` |
| Full model display name | Qwen2.5 Coder 1.5B Instruct LoRA Multilingual |
| Raw model identifier | `qwen25_coder_1_5b_instruct_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/python/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_coder_1_5b_lora_multilang/qwen25_coder_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1.jsonl --base-model Qwen/Qwen2.5-Coder-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_coder_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_coder_1_5b_lora_multilang/qwen25_coder_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/4bf3ff8b1b15_qwen25_coder_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_coder_1_5b_lora_multilang/qwen25_coder_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_coder_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
cb4e3f1b734f234ac9505df87f87b642506042fdf0f0617af206622ea0886b8b  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/generation/raw_generations.jsonl
22415a58b1ff17aaa2a038f0542d0bcd89861d5d8c058de04e202b80bd8be065  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/automatic_detailed.jsonl
6fabe27b685091b77e6dd6e6921ab625ea9f5551184124f91f10ca658745e3f6  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/automatic_summary.json
d7d371ece32714a349d52b46feafaa57be1f21a5f2492e323d308174537b4351  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/code_grounded_detailed.jsonl
4ceb393b71866e60915e3775383fa028a28c965b94397f52c51ab881653c87fd  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/python/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
