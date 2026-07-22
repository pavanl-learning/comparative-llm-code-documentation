# Gemini 3 Flash Preview — python — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemini_3_flash__python__os` |
| Full model display name | Gemini 3 Flash Preview |
| Raw model identifier | `gemini-3-flash-preview` |
| Model group | commercial-new |
| Model category | commercial_api |
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
- Generation script: [scripts/generation/run_generation_gemini.py](../../../../../scripts/generation/run_generation_gemini.py)
- Command file: [experiments/core_400/gemini_3_flash/python/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_gemini.py --input ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_one_shot_python_400_v1.jsonl --model gemini-3-flash-preview --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_one_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_one_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_one_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_one_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemini_3_flash/python/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemini_3_flash/python/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemini_3_flash/python/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemini_3_flash/python/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemini_3_flash/python/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemini_3_flash/python/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemini_3_flash/python/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemini_3_flash/python/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemini_3_flash/python/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemini_3_flash/python/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
d447b4c53c17fb2459d5b68e116fb373b826d7da9b26048fda1e335d28120726  experiments/core_400/gemini_3_flash/python/os/generation/raw_generations.jsonl
784a9cc5b01b43c41ba6013c3e00db1115fe2f485f2eb4fa9ae1aa2d2be10429  experiments/core_400/gemini_3_flash/python/os/assessment/automatic_detailed.jsonl
715c8feea501f63c7d67ffa0ade0b3c8d0cb0839a37cf1380a3fd00048c64e9a  experiments/core_400/gemini_3_flash/python/os/assessment/automatic_summary.json
25b2a885ddfd17415cbfc2faac43def9e730dcbc2d62ef1e7ea2e2b846c1f935  experiments/core_400/gemini_3_flash/python/os/assessment/code_grounded_detailed.jsonl
2233bde1fdcd49e93f7e2a1790b6c7c62c8a7a4b72601d0ede055cfdffc3d30a  experiments/core_400/gemini_3_flash/python/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
