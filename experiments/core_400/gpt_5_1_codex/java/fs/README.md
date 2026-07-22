# GPT-5.1 Codex — java — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1_codex__java__fs` |
| Full model display name | GPT-5.1 Codex |
| Raw model identifier | `gpt-5.1-codex` |
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
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1_codex/java/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/gpt_5_1_codex_P1_few_shot_java_400_v1.jsonl --model gpt-5.1-codex --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/gpt_5_1_codex_P1_few_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_few_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/gpt_5_1_codex_P1_few_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_few_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1_codex/java/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1_codex/java/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1_codex/java/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1_codex/java/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1_codex/java/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1_codex/java/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1_codex/java/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1_codex/java/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1_codex/java/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1_codex/java/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
0cfc5076ec41780c00ef898585559f965949b2eb1944e46d739f0ff3415777fc  experiments/core_400/gpt_5_1_codex/java/fs/generation/raw_generations.jsonl
1fbe38962552f05800039ac7a291bbc0327a4ca4561a48c831b559443769c34c  experiments/core_400/gpt_5_1_codex/java/fs/assessment/automatic_detailed.jsonl
67231db824685d3903c1f2767b25b53fa753ed930d1226882c992e303b8cd11f  experiments/core_400/gpt_5_1_codex/java/fs/assessment/automatic_summary.json
683d1f47b3bac75c72fcadca78977cd48b2aa3e9197b276f632a839f92919585  experiments/core_400/gpt_5_1_codex/java/fs/assessment/code_grounded_detailed.jsonl
3799776499f887d94c00aed88129ca8b96b83ac1302d6977a37a537e8242c5f9  experiments/core_400/gpt_5_1_codex/java/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
