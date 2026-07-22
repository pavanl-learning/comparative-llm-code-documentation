# Gemma 2 2B IT — javascript — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it__javascript__zs` |
| Full model display name | Gemma 2 2B IT |
| Raw model identifier | `google/gemma-2-2b-it` |
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
- Command file: [experiments/core_400/gemma_2_2b_it/javascript/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/gemma-2-2b-it --input ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_javascript_400_v2.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_javascript_400_v2.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_zero_shot_javascript_400_v2
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_javascript_400_v2.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_zero_shot_javascript_400_v2_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it/javascript/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it/javascript/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it/javascript/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it/javascript/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it/javascript/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it/javascript/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
0a63fd7edee9d7b250ae7a0f272bdaba6b220d7a48b5b75cfdeae529d8406e7c  experiments/core_400/gemma_2_2b_it/javascript/zs/generation/raw_generations.jsonl
52f6fee3120f75409036a8fc5a384fbb0bbaf8f763eb1ec077861f1bb0644d9e  experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/automatic_detailed.jsonl
0dd4dc0084fbf5bed711ecf2a8d94c5111e3b804ab806d118e35d1c7743ed1d6  experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/automatic_summary.json
aa4cd873eb47def950ab4b850e373fff332e8941e15162ad076b25f8fc0c5515  experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/code_grounded_detailed.jsonl
7a8a3f20d2a4f866fd1296af91f3405ae6ec4aac3543bd33578dc3c0dcff34ca  experiments/core_400/gemma_2_2b_it/javascript/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
