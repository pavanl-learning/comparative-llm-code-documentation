# Qwen2.5 1.5B Instruct LoRA Multilingual — python — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct_lora__python__os` |
| Full model display name | Qwen2.5 1.5B Instruct LoRA Multilingual |
| Raw model identifier | `qwen25_coder_1_5b_instruct_lora_multilang` |
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
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_one_shot_python_400_v1.jsonl --base-model Qwen/Qwen2.5-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_one_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/68ff91b210ec_qwen25_1_5b_instruct_lora_multilang_P1_one_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_one_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_1_5b_instruct_lora_multilang_P1_one_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
38ce3b40415982c3111e3bae883161b1ad95ac846f9dce8acd04088596bfb395  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/generation/raw_generations.jsonl
c793106f7987cf972bd250f077e5f3b44b6459eecac84082a560ce0bd19ff289  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/automatic_detailed.jsonl
050b2f44a8ffa6d42a421e42527d8ff9fa0e47ab08106e98fd7112a8e2d1e527  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/automatic_summary.json
e1669edd9b5b62d61d7bc9e3e41309e360dd4d06a68f61bd90512f3100e0377e  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/code_grounded_detailed.jsonl
ace8d0b18c2a8b17c4da7241cbc301aead601b4cd024360cd1c43f07d23b7a83  experiments/core_400/qwen2_5_1_5b_instruct_lora/python/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
