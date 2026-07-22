# DeepSeek Chat — python — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `deepseek_chat_v3_2__python__fs` |
| Full model display name | DeepSeek Chat |
| Raw model identifier | `deepseek-chat` |
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
- Generation script: [scripts/generation/run_generation_deepseek.py](../../../../../scripts/generation/run_generation_deepseek.py)
- Command file: [experiments/core_400/deepseek_chat_v3_2/python/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_deepseek.py --input ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_few_shot_python_400_v1.jsonl --model deepseek-chat --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_few_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_few_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_few_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_few_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/deepseek_chat_v3_2/python/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/deepseek_chat_v3_2/python/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/deepseek_chat_v3_2/python/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/deepseek_chat_v3_2/python/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/deepseek_chat_v3_2/python/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/deepseek_chat_v3_2/python/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
68e360e20c94c400c1174321b944a11d81a3c4e74ef010640b065fb99413aab2  experiments/core_400/deepseek_chat_v3_2/python/fs/generation/raw_generations.jsonl
cf2d8f0dc41b965f27b60effc764d56d7c991040441cb45ec3a745404930aeb5  experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/automatic_detailed.jsonl
32adacaa4ad707b844c29de0baa4cf3f7f8acc7e87dcb6fbdb48d48ba27259fd  experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/automatic_summary.json
efd5114ed8f77178e782c6266456089a2fc0e44f65f193fa5c382fc64b69b2e7  experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/code_grounded_detailed.jsonl
3afd3eac18fd629f5f319eb95bafe6f30603254f3d462a9a9281d83d90d29f44  experiments/core_400/deepseek_chat_v3_2/python/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
