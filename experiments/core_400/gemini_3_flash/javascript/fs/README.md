# Gemini 3 Flash Preview — javascript — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemini_3_flash__javascript__fs` |
| Full model display name | Gemini 3 Flash Preview |
| Raw model identifier | `gemini-3-flash-preview` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | javascript |
| Prompt regime | FS |
| Validation status | PASS |

## Row-count validation

| Artefact | Expected | Observed |
|---|---:|---:|
| Raw generations | 400 | 400 |
| Automatic detailed evaluation | 400 | 400 |
| Code-grounded detailed evaluation | 400 | 400 |

Sample-ID alignment: `True`.

## Inputs and execution

- Prompt input file: [prompts/core_400/javascript/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_gemini.py](../../../../../scripts/generation/run_generation_gemini.py)
- Command file: [experiments/core_400/gemini_3_flash/javascript/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_gemini.py --input ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_javascript_400_v1.jsonl --model gemini-3-flash-preview --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_few_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_few_shot_javascript_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemini_3_flash/javascript/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemini_3_flash/javascript/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemini_3_flash/javascript/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemini_3_flash/javascript/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemini_3_flash/javascript/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemini_3_flash/javascript/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemini_3_flash/javascript/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemini_3_flash/javascript/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemini_3_flash/javascript/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemini_3_flash/javascript/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
99d87a3ef4651af389d4be529c33bb24c80fa5853c0b0c06e859e224f11668f5  experiments/core_400/gemini_3_flash/javascript/fs/generation/raw_generations.jsonl
11cfcdf7019b0baded89b90ceeeda5f4495a82409d0b1d5942c1a87d8e02521e  experiments/core_400/gemini_3_flash/javascript/fs/assessment/automatic_detailed.jsonl
d8012faf5bcea41c5ccf601e61dbaed5f283c967f4fff3b2c9c03ce3e845d716  experiments/core_400/gemini_3_flash/javascript/fs/assessment/automatic_summary.json
6edc679fa522eaebd03605be4ddddbf7bc4628c756996c450de7f43be7f2434a  experiments/core_400/gemini_3_flash/javascript/fs/assessment/code_grounded_detailed.jsonl
a3d7c7f142a30a03e337fc7aae0bdac5292b3624212acc3595ed9b99a76e7e0c  experiments/core_400/gemini_3_flash/javascript/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
