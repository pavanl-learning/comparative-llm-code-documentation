# DeepSeek Chat — python — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `deepseek_chat_v3_2__python__os` |
| Full model display name | DeepSeek Chat |
| Raw model identifier | `deepseek-chat` |
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
- Generation script: [scripts/generation/run_generation_deepseek.py](../../../../../scripts/generation/run_generation_deepseek.py)
- Command file: [experiments/core_400/deepseek_chat_v3_2/python/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_deepseek.py --input ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_python_400_v1.jsonl --model deepseek-chat --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_one_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/deepseek_chat_P1_one_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/deepseek_chat_v3_2/python/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/deepseek_chat_v3_2/python/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/deepseek_chat_v3_2/python/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/deepseek_chat_v3_2/python/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/deepseek_chat_v3_2/python/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/deepseek_chat_v3_2/python/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/deepseek_chat_v3_2/python/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/deepseek_chat_v3_2/python/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/deepseek_chat_v3_2/python/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/deepseek_chat_v3_2/python/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
c0ca545e48b93963dfdacf71c237ddd0a53d82c28177b21fd15bbed430a86447  experiments/core_400/deepseek_chat_v3_2/python/os/generation/raw_generations.jsonl
46f85e1d87cc4ffec8fe3e1d4d1fe44c867fb4019823a10d5788f07d7511f564  experiments/core_400/deepseek_chat_v3_2/python/os/assessment/automatic_detailed.jsonl
9c2944409bff8e4afca914527de9d4562726fd53b1f3f96603cd0f8962bec77d  experiments/core_400/deepseek_chat_v3_2/python/os/assessment/automatic_summary.json
212932c3fba5d61a842bfba666903e1dede42a5408a49dae0faa71757c5422b0  experiments/core_400/deepseek_chat_v3_2/python/os/assessment/code_grounded_detailed.jsonl
d12026df828ab0bfd5b2513d31cdf9d0178585cf6d5ba316489d289a420521b5  experiments/core_400/deepseek_chat_v3_2/python/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
