# CodeGemma 2B — java — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b__java__os` |
| Full model display name | CodeGemma 2B |
| Raw model identifier | `google/codegemma-2b` |
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
- Command file: [experiments/core_400/codegemma_2b/java/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/codegemma-2b --input ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_one_shot_java_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_one_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/codegemma_2b_P1_one_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_one_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/codegemma_2b_P1_one_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b/java/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b/java/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b/java/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b/java/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b/java/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b/java/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b/java/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b/java/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b/java/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b/java/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
c2d4b1096244186cfe66786ee4149d46c273e7168d85b027bab8c8dfa84d488d  experiments/core_400/codegemma_2b/java/os/generation/raw_generations.jsonl
208e55ca4ead8302c9fba0b414671e70fad7418fb079cd165202a5a85323eaf0  experiments/core_400/codegemma_2b/java/os/assessment/automatic_detailed.jsonl
fb93da3e1707406a8bb40fc7812d2d4a9d3500ae2d9eff88f7fe55d244e257b5  experiments/core_400/codegemma_2b/java/os/assessment/automatic_summary.json
713ced3f94f6b680d53c5c1ce42ef32b8fdb005bd6b5aa5bc141cd52a93e7433  experiments/core_400/codegemma_2b/java/os/assessment/code_grounded_detailed.jsonl
05b1b8fa2c8b968254f9c3a5712f5fe31b67d7279f6bf779879245ff90489472  experiments/core_400/codegemma_2b/java/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
