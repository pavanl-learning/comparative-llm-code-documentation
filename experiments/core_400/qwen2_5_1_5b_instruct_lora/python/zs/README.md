# Qwen2.5 1.5B Instruct LoRA Multilingual — python — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct_lora__python__zs` |
| Full model display name | Qwen2.5 1.5B Instruct LoRA Multilingual |
| Raw model identifier | `qwen25_coder_1_5b_instruct_lora_multilang` |
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
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_zero_shot_python_400_v1.jsonl --base-model Qwen/Qwen2.5-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_zero_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/cc7dab0b70c4_qwen25_1_5b_instruct_lora_multilang_P1_zero_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_zero_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_1_5b_instruct_lora_multilang_P1_zero_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
56b581db63a16bc12dbef6c910643494a6f0d8d94def336c40517b9336e299b3  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/generation/raw_generations.jsonl
5914ad0a6f6e6665725971598b10088dd085615305d3f1e6013fe10000c12ea5  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/automatic_detailed.jsonl
4fddec22e3c1d6e08825bee9c5d430ec95471ed3a7c580e7acb7a0cc80479f1b  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/automatic_summary.json
e1edac367886adbc29c9ae6c715e6aa077eef18a92197b72dc71e550f46e38e5  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/code_grounded_detailed.jsonl
8b157f7e443229340306c73c8fb2d82a66cc1b5e015947c78df510583c242187  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
