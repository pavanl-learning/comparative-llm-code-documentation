# CodeGemma 2B — javascript — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b__javascript__fs` |
| Full model display name | CodeGemma 2B |
| Raw model identifier | `google/codegemma-2b` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/codegemma_2b/javascript/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/codegemma-2b --input ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_few_shot_javascript_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_few_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/codegemma_2b_P1_few_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_few_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/codegemma_2b_P1_few_shot_javascript_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b/javascript/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b/javascript/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b/javascript/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b/javascript/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b/javascript/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b/javascript/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b/javascript/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b/javascript/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b/javascript/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b/javascript/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
73e82d9068f1af0acefc5462fb3fb0bb53e80829f9b8a91bcd482582ab811859  experiments/core_400/codegemma_2b/javascript/fs/generation/raw_generations.jsonl
36559f6ad4e3a6ce12b6bc25b5f53e8b06ec458ec295de285743c99e587ad5b4  experiments/core_400/codegemma_2b/javascript/fs/assessment/automatic_detailed.jsonl
2b668f13e67a2529a0a2b52276b684dc5a9ec8410d6b5a8ad52b30bcd3522aca  experiments/core_400/codegemma_2b/javascript/fs/assessment/automatic_summary.json
ef5885cd9f1741edca418ec8cd9f7b22c47041f176d1d2dbbf31c04d0787f8aa  experiments/core_400/codegemma_2b/javascript/fs/assessment/code_grounded_detailed.jsonl
fab874f281d2e0192aee7fa46b49667d70edce287234d3434e66f6d0a36d15f0  experiments/core_400/codegemma_2b/javascript/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
