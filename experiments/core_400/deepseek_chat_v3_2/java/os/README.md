# DeepSeek Chat — java — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `deepseek_chat_v3_2__java__os` |
| Full model display name | DeepSeek Chat |
| Raw model identifier | `deepseek-chat` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | java |
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

- Prompt input file: [prompts/core_400/java/os/prompt_input_400.jsonl](../../../../../prompts/core_400/java/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_deepseek.py](../../../../../scripts/generation/run_generation_deepseek.py)
- Command file: [experiments/core_400/deepseek_chat_v3_2/java/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_deepseek.py --input ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_java_400_v1.jsonl --model deepseek-chat --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_one_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/deepseek_chat_P1_one_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/deepseek_chat_v3_2/java/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/deepseek_chat_v3_2/java/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/deepseek_chat_v3_2/java/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/deepseek_chat_v3_2/java/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/deepseek_chat_v3_2/java/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/deepseek_chat_v3_2/java/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/deepseek_chat_v3_2/java/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/deepseek_chat_v3_2/java/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/deepseek_chat_v3_2/java/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/deepseek_chat_v3_2/java/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
ca6fcecd17345049142443e42e3aa8121d2b41d20f91cb864b859a2b10fc4318  experiments/core_400/deepseek_chat_v3_2/java/os/generation/raw_generations.jsonl
194ad90feca61636cc49d3bc085b16297bcd9c951648a4f65d6e7837fd4f39b7  experiments/core_400/deepseek_chat_v3_2/java/os/assessment/automatic_detailed.jsonl
429a45c902ce080efdb893560fcb0ff6eb54a03829c33c4ad4b15b09521178e1  experiments/core_400/deepseek_chat_v3_2/java/os/assessment/automatic_summary.json
65c4aa9b816c67779af5adae13d4746500fa19a978a7e97c0d27822c4b67e73e  experiments/core_400/deepseek_chat_v3_2/java/os/assessment/code_grounded_detailed.jsonl
2d109e258deaff62f120f8f4705dd8868eae09768dc5b285b488203da61e98f1  experiments/core_400/deepseek_chat_v3_2/java/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
