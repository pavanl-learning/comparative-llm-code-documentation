# GPT-5.1 — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1__java__zs` |
| Full model display name | GPT-5.1 |
| Raw model identifier | `gpt-5.1` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | java |
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

- Prompt input file: [prompts/core_400/java/zs/prompt_input_400.jsonl](../../../../../prompts/core_400/java/zs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_zero_shot_java_400_v1.jsonl --model gpt-5.1 --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/gpt_5_1_P1_zero_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
0e6569a8026eef7ef53a9cda51657ce03c4e7b7093c639b07b5dffb1d0d9b013  experiments/core_400/gpt_5_1/java/zs/generation/raw_generations.jsonl
1ad9dd098021b11360ada858f3da2888a1146f249a3017b55f351f61a6a731df  experiments/core_400/gpt_5_1/java/zs/assessment/automatic_detailed.jsonl
590bf83df1939748984c1646240905e475f40cf439f8dff3dba6ae260983f808  experiments/core_400/gpt_5_1/java/zs/assessment/automatic_summary.json
c2d1478ccfbc620a149059292a82d7648781ccf5800fdc9abda976de068628e8  experiments/core_400/gpt_5_1/java/zs/assessment/code_grounded_detailed.jsonl
4997e67f502c32411cab2450633daf132e2470bf061cfc2b80d8561ab2ab4e67  experiments/core_400/gpt_5_1/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
