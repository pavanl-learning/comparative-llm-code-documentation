# Qwen2.5 1.5B Instruct — javascript — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct__javascript__zs` |
| Full model display name | Qwen2.5 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_1_5b_instruct_P1_zero_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
0ee800ebf004f88429216e48aa981b3ed617e0aa54552ed551a27d717cf8bb2c  experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/generation/raw_generations.jsonl
8c741349bf2d9048c797a40c6a58c0caf647b126fbc38724bc340e2c0e443e0f  experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/automatic_detailed.jsonl
f689c852b8fe492f1c0e90b7ae849021cd81a34b0b84fa3517fa7e0f08d5371a  experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/automatic_summary.json
eb480e633fd1f3add76338136fababef911c1f2f2beaff8d19f2fcd7db186a1e  experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/code_grounded_detailed.jsonl
b50304c2afdcbfc0355de23480931802ed029d98a4d2d11a207b5fd5326651bd  experiments/core_400/qwen2_5_1_5b_instruct/javascript/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
