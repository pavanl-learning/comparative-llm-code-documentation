# Gemma 2 2B IT — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it__java__zs` |
| Full model display name | Gemma 2 2B IT |
| Raw model identifier | `google/gemma-2-2b-it` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/gemma_2_2b_it/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/gemma-2-2b-it --input ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_java_400_v2.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_java_400_v2.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_zero_shot_java_400_v2
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_java_400_v2.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_zero_shot_java_400_v2_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
6d47f2f11b1540fd256c7aba6c6f57e21b8d06a5fc28015f6310f7c0ea808279  experiments/core_400/gemma_2_2b_it/java/zs/generation/raw_generations.jsonl
368875c107ce09c8b0b212295260a88f5c77700fd6f4a51d99615d0849de9470  experiments/core_400/gemma_2_2b_it/java/zs/assessment/automatic_detailed.jsonl
2a618829e0c3a8273af71b4b6c0dfad0e2c82439bc8bc7d9f19a06f356385f3f  experiments/core_400/gemma_2_2b_it/java/zs/assessment/automatic_summary.json
1e1fd722a65622dac0cfa9ac3a3e28cd5d1a8f0dee433bf888556c4b7c28330c  experiments/core_400/gemma_2_2b_it/java/zs/assessment/code_grounded_detailed.jsonl
d8af0cbca9b4a2682b57661ac5c17c31645977c7f25573cb8e8e477cbd59a747  experiments/core_400/gemma_2_2b_it/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
