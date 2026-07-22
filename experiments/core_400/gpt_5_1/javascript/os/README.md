# GPT-5.1 — javascript — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1__javascript__os` |
| Full model display name | GPT-5.1 |
| Raw model identifier | `gpt-5.1` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | javascript |
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

- Prompt input file: [prompts/core_400/javascript/os/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1/javascript/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_one_shot_javascript_400_v1.jsonl --model gpt-5.1 --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_one_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_P1_one_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_P1_one_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_P1_one_shot_javascript_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1/javascript/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1/javascript/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1/javascript/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1/javascript/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1/javascript/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1/javascript/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1/javascript/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1/javascript/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1/javascript/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1/javascript/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
1570b040d4502e080ce1ca6c08c15a016f9cfcaf136dd347d6f1539f73dad420  experiments/core_400/gpt_5_1/javascript/os/generation/raw_generations.jsonl
810a97b80732522b81e4aacf9a0b55a02514250e9ba48bd83145f09664f61aa2  experiments/core_400/gpt_5_1/javascript/os/assessment/automatic_detailed.jsonl
4047274d8a7aadc618d7b9094e67982fc92a3b68c2ae9e9276e3cde949716ddc  experiments/core_400/gpt_5_1/javascript/os/assessment/automatic_summary.json
37bd745cf1ff2d94406399c822fd7f4e18000770c469b591a6ad83cd050d8500  experiments/core_400/gpt_5_1/javascript/os/assessment/code_grounded_detailed.jsonl
9c6bdbab72b652e7965e10449805e587f4d9ff279707ff505661b95e739dfe3f  experiments/core_400/gpt_5_1/javascript/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
