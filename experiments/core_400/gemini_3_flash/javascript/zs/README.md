# Gemini 3 Flash Preview — javascript — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemini_3_flash__javascript__zs` |
| Full model display name | Gemini 3 Flash Preview |
| Raw model identifier | `gemini-3-flash-preview` |
| Model group | commercial-new |
| Model category | commercial_api |
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
- Generation script: [scripts/generation/run_generation_gemini.py](../../../../../scripts/generation/run_generation_gemini.py)
- Command file: [experiments/core_400/gemini_3_flash/javascript/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_gemini.py --input ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_zero_shot_javascript_400_v1.jsonl --model gemini-3-flash-preview --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_zero_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_zero_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_zero_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/gemini_3_flash_preview_P1_zero_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemini_3_flash/javascript/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemini_3_flash/javascript/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemini_3_flash/javascript/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemini_3_flash/javascript/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemini_3_flash/javascript/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemini_3_flash/javascript/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemini_3_flash/javascript/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemini_3_flash/javascript/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemini_3_flash/javascript/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemini_3_flash/javascript/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
bbecdb432e1786fe0ab64e1fb2a02a430c3798a888f1c6cef71788ab849c815b  experiments/core_400/gemini_3_flash/javascript/zs/generation/raw_generations.jsonl
ab840f851a8c0a99fec8f1a344c9362c39369c06e40dd7fee55be12dcc190058  experiments/core_400/gemini_3_flash/javascript/zs/assessment/automatic_detailed.jsonl
a584a09f4924154085577058321de2b1b0cf16fd8ea8225404dccbaebbb9318c  experiments/core_400/gemini_3_flash/javascript/zs/assessment/automatic_summary.json
bdb45cf6b86963f628dde39ca893bec80e057bd497fc88c9e9765dd8dfdd845a  experiments/core_400/gemini_3_flash/javascript/zs/assessment/code_grounded_detailed.jsonl
8590339755a5649b2cab45ab6fcc300b243110bcc873554e14f096f8fb7638c1  experiments/core_400/gemini_3_flash/javascript/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
