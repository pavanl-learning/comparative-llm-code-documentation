# CodeGemma 2B — javascript — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b__javascript__os` |
| Full model display name | CodeGemma 2B |
| Raw model identifier | `google/codegemma-2b` |
| Model group | open-source |
| Model category | open_source_base |
| Language | javascript |
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

- Prompt input file: [prompts/core_400/javascript/os/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/codegemma_2b/javascript/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/codegemma-2b --input ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_one_shot_javascript_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_one_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/codegemma_2b_P1_one_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_one_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/codegemma_2b_P1_one_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b/javascript/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b/javascript/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b/javascript/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b/javascript/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b/javascript/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b/javascript/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b/javascript/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b/javascript/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b/javascript/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b/javascript/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
591e88ed44d9d9ead90b331a459e50cb1dee4e825610cd554a11d546a27cb8b1  experiments/core_400/codegemma_2b/javascript/os/generation/raw_generations.jsonl
f6e8bb4526627706d7897c0bdad20e7700d8c3169ad0e00f1555357250954f80  experiments/core_400/codegemma_2b/javascript/os/assessment/automatic_detailed.jsonl
7db8ffaf0fff4563c549925108807f975caa13a99fc737a27bc8bbd19f9d51db  experiments/core_400/codegemma_2b/javascript/os/assessment/automatic_summary.json
20681fdb5af6f185e7e7b32551f09b45b20bf62fb0ca40d141cff40bda6a0d01  experiments/core_400/codegemma_2b/javascript/os/assessment/code_grounded_detailed.jsonl
35cc11353143fa5d6d048fce9338be686c14b46ef3df1a2def8a6478d1bb847c  experiments/core_400/codegemma_2b/javascript/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
