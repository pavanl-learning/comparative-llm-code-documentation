# Gemini 3 Flash Preview — java — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemini_3_flash__java__fs` |
| Full model display name | Gemini 3 Flash Preview |
| Raw model identifier | `gemini-3-flash-preview` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | java |
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

- Prompt input file: [prompts/core_400/java/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/java/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_gemini.py](../../../../../scripts/generation/run_generation_gemini.py)
- Command file: [experiments/core_400/gemini_3_flash/java/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_gemini.py --input ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_java_400_v1.jsonl --model gemini-3-flash-preview --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_few_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gemini_3_flash_preview_P1_few_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gemini_3_flash_preview_P1_few_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemini_3_flash/java/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemini_3_flash/java/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemini_3_flash/java/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemini_3_flash/java/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemini_3_flash/java/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemini_3_flash/java/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemini_3_flash/java/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemini_3_flash/java/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemini_3_flash/java/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemini_3_flash/java/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
5e1010598a14a0eaa2e7b4be67dcb3dc1127ddcfe61cd966f54ce08340e0c5a0  experiments/core_400/gemini_3_flash/java/fs/generation/raw_generations.jsonl
9ade424a3cb9a0a174b9f0b2afc338cd3cfdbfa11cb123a1c80d47881ad0ad02  experiments/core_400/gemini_3_flash/java/fs/assessment/automatic_detailed.jsonl
2fe05009bb8268a0876b9d1f49cf94f56fe3df6234997c8b2f31f7ba8a3956b4  experiments/core_400/gemini_3_flash/java/fs/assessment/automatic_summary.json
fd38873fe9ff775c2f2953d5779206caa22b60c740e5e7e4c7caeb79b34242c9  experiments/core_400/gemini_3_flash/java/fs/assessment/code_grounded_detailed.jsonl
27ebde568f3ae19058a509e904361d07134afc79538777027958f149bf7e60e6  experiments/core_400/gemini_3_flash/java/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
