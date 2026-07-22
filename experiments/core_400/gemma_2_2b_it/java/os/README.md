# Gemma 2 2B IT — java — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it__java__os` |
| Full model display name | Gemma 2 2B IT |
| Raw model identifier | `google/gemma-2-2b-it` |
| Model group | open-source |
| Model category | open_source_base |
| Language | java |
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

- Prompt input file: [prompts/core_400/java/os/prompt_input_400.jsonl](../../../../../prompts/core_400/java/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/gemma_2_2b_it/java/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/gemma-2-2b-it --input ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_one_shot_java_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_one_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_one_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_one_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/gemma_2_2b_it_P1_one_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it/java/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it/java/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it/java/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it/java/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it/java/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it/java/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it/java/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it/java/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it/java/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it/java/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
9f2a9ec525af97cf2c51c4393d3dd34a04462ce7e3f5556c69a435bbdc1f87dd  experiments/core_400/gemma_2_2b_it/java/os/generation/raw_generations.jsonl
7e920d23382ce800f152512ca79299ed34c6bc9541849095baf8b15648644fbc  experiments/core_400/gemma_2_2b_it/java/os/assessment/automatic_detailed.jsonl
0e8967b20158f1f5c3468c9b06ae608722b2e05c673465179d20f40e65fbe660  experiments/core_400/gemma_2_2b_it/java/os/assessment/automatic_summary.json
cb4212d5731045d7b00949a12b683aa400c92832752aad78e56260af0102d057  experiments/core_400/gemma_2_2b_it/java/os/assessment/code_grounded_detailed.jsonl
6eea779eec57f01076e8a7e86a5cb2d0faeb409b671c4171a8d079b835e0f6cb  experiments/core_400/gemma_2_2b_it/java/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
