# Gemma 2 2B IT — python — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it__python__zs` |
| Full model display name | Gemma 2 2B IT |
| Raw model identifier | `google/gemma-2-2b-it` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/gemma_2_2b_it/python/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/gemma-2-2b-it --input ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_python_400_v2.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_python_400_v2.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_zero_shot_python_400_v2
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_zero_shot_python_400_v2.jsonl --source ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_zero_shot_python_400_v2_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it/python/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it/python/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it/python/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it/python/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it/python/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it/python/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it/python/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it/python/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it/python/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it/python/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
fc9409051c929964cb4676a8415f63fd25c2cc83786379c65f4436aa3a5e1350  experiments/core_400/gemma_2_2b_it/python/zs/generation/raw_generations.jsonl
4fc52c629ec0edc3cc3500b0ef6aeaa04c9e554065affa2f791c92b280b0949c  experiments/core_400/gemma_2_2b_it/python/zs/assessment/automatic_detailed.jsonl
7a415b56211bc968082cd237e05081a559fb526cfe7d317911921988ee55a751  experiments/core_400/gemma_2_2b_it/python/zs/assessment/automatic_summary.json
dcf42edce09ea04dbb68c6e29a6e67a1565528f3c6d885c876054a1c070479ef  experiments/core_400/gemma_2_2b_it/python/zs/assessment/code_grounded_detailed.jsonl
3c90a02d761c17e817c1e98cce306a88173161f1e430130b4d6334cf81cdf5d5  experiments/core_400/gemma_2_2b_it/python/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
