# Gemini 3 Flash Preview — python — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemini_3_flash__python__fs` |
| Full model display name | Gemini 3 Flash Preview |
| Raw model identifier | `gemini-3-flash-preview` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/python/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_gemini.py](../../../../../scripts/generation/run_generation_gemini.py)
- Command file: [experiments/core_400/gemini_3_flash/python/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_gemini.py --input ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_python_400_v1.jsonl --model gemini-3-flash-preview --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_few_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_few_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemini_3_flash/python/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemini_3_flash/python/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemini_3_flash/python/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemini_3_flash/python/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemini_3_flash/python/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemini_3_flash/python/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemini_3_flash/python/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemini_3_flash/python/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemini_3_flash/python/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemini_3_flash/python/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
279342f82f215c68a604ffa9a0a63c7f138a473e723cf0b8dec7b528600fb341  experiments/core_400/gemini_3_flash/python/fs/generation/raw_generations.jsonl
98bd741236941971b1bbe63b36e0dc2a0e07e96cc4fa5aa377b8dd70d870aaf4  experiments/core_400/gemini_3_flash/python/fs/assessment/automatic_detailed.jsonl
28fa066dcb0c535b03b2b2954f2aab954864054b5ab249883761479eeccd9ef8  experiments/core_400/gemini_3_flash/python/fs/assessment/automatic_summary.json
b863490c9ca2439c5280e5ca1bf2bb715f4a423f0b09b5a98c1df71aee275de4  experiments/core_400/gemini_3_flash/python/fs/assessment/code_grounded_detailed.jsonl
938adb35367c749d4f3ed8b822658f72b719e42014e846f594c49030c3d679ea  experiments/core_400/gemini_3_flash/python/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
