# GPT-5.1 — python — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1__python__zs` |
| Full model display name | GPT-5.1 |
| Raw model identifier | `gpt-5.1` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/zs/prompt_input_400.jsonl](../../../../../prompts/core_400/python/zs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1/python/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_zero_shot_python_400_v2.jsonl --model gpt-5.1 --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_zero_shot_python_400_v2.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_P1_zero_shot_python_400_v2
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_zero_shot_python_400_v2.jsonl --source ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/gpt_5_1_P1_zero_shot_python_400_v2_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1/python/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1/python/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1/python/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1/python/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1/python/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1/python/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1/python/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1/python/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1/python/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1/python/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
f4971c24cdbf9aa35ceae07cedc9d2e83d5ac035ee7ea4fa112f830c136b7ffa  experiments/core_400/gpt_5_1/python/zs/generation/raw_generations.jsonl
521d32e6b8cce6a521e3ab2149ff2f93b9649845c17151c7cdad74fb5c966e7b  experiments/core_400/gpt_5_1/python/zs/assessment/automatic_detailed.jsonl
357070ece98dd2b0dfa348df9c2286a9cb44c184f5f4bbf3f17791e3c86729a6  experiments/core_400/gpt_5_1/python/zs/assessment/automatic_summary.json
941fc2f44d7661940a0eb8840d11a6594d24e5e8bea4412c7e586176b4eaff9e  experiments/core_400/gpt_5_1/python/zs/assessment/code_grounded_detailed.jsonl
6d8c858c86e8bced64da6fc65ab5f92c8600d05032f484cc20819f815ff1bbb2  experiments/core_400/gpt_5_1/python/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
