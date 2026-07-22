# Qwen2.5 1.5B Instruct LoRA Multilingual — python — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct_lora__python__fs` |
| Full model display name | Qwen2.5 1.5B Instruct LoRA Multilingual |
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
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1.jsonl --base-model Qwen/Qwen2.5-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/4dc9f6a70648_qwen25_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
8be96a1a52e18102327ad17aade9042db4ebf198b42c120d00dfad33d873f28f  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/generation/raw_generations.jsonl
2b55ebb58bce0e265ba71497c01a4e06df766fd49f482ba04a76ebd71477487d  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/automatic_detailed.jsonl
f5ed90a3dd3f67709a201771b85884c898e25298e1fa8bc4e000f09ddac0cd19  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/automatic_summary.json
96f9ce5aa86f7fda1f36d77d069b6c29fb34cade4f956a9d58bbaf43d2337a08  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/code_grounded_detailed.jsonl
9fdb956cc8851a04fffc40cfbecdef8b4026ab2e8b4d2e8c2d715aa610a17e6d  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
