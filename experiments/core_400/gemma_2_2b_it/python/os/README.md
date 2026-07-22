# Gemma 2 2B IT — python — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it__python__os` |
| Full model display name | Gemma 2 2B IT |
| Raw model identifier | `google/gemma-2-2b-it` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/gemma_2_2b_it/python/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/gemma-2-2b-it --input ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_one_shot_python_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_one_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/gemma_2_2b_it_P1_one_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/gemma_2_2b_it_P1_one_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/gemma_2_2b_it_P1_one_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it/python/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it/python/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it/python/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it/python/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it/python/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it/python/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it/python/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it/python/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it/python/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it/python/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
14af18e16f792dbe8346cc9ef62ede7b70aac7fc9641f87d89f5a41484199fad  experiments/core_400/gemma_2_2b_it/python/os/generation/raw_generations.jsonl
5c8545bd67d97011a1addfa29d8d6639642879a09711a0dfc0102fb617eac6b4  experiments/core_400/gemma_2_2b_it/python/os/assessment/automatic_detailed.jsonl
bbe1462d7aab6833cd39728d5b4aa707fad91fc1b28de3cbac460296d526dfd1  experiments/core_400/gemma_2_2b_it/python/os/assessment/automatic_summary.json
6100c0748c15a5c023e3fc861120d9634416f2bc3a64e1c57907affab8bff111  experiments/core_400/gemma_2_2b_it/python/os/assessment/code_grounded_detailed.jsonl
c6b013cee68a51322b7c3bd92d0fb65322142b381aaf766d007ef151d03a03eb  experiments/core_400/gemma_2_2b_it/python/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
