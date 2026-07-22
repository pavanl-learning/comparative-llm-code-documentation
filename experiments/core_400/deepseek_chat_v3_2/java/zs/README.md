# DeepSeek Chat — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `deepseek_chat_v3_2__java__zs` |
| Full model display name | DeepSeek Chat |
| Raw model identifier | `deepseek-chat` |
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
- Generation script: [scripts/generation/run_generation_deepseek.py](../../../../../scripts/generation/run_generation_deepseek.py)
- Command file: [experiments/core_400/deepseek_chat_v3_2/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_deepseek.py --input ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_zero_shot_java_400_v1.jsonl --model deepseek-chat --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/deepseek_chat_P1_zero_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/deepseek_chat_v3_2/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/deepseek_chat_v3_2/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/deepseek_chat_v3_2/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/deepseek_chat_v3_2/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/deepseek_chat_v3_2/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/deepseek_chat_v3_2/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
bb00e42153b6c66b8b51bfc93ab2e43c317d53bd3ed25ec2d6d1d3db6ca87924  experiments/core_400/deepseek_chat_v3_2/java/zs/generation/raw_generations.jsonl
492fb3c8d0ed20d22b59a45446787b920f1c7f06112b85c554a822e80e518b56  experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/automatic_detailed.jsonl
03eaa835fb3d5fc830f3c35ed3d3f904f8de87857d64d0d92f3baebbd8bae98d  experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/automatic_summary.json
01904ec460a130d23991da997ccd48660ca5da4f7956fd3af338e1bea75f904d  experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/code_grounded_detailed.jsonl
8f2478f41657cf0d7eb8c1a16d531134b057178762ef2884343f85981059f464  experiments/core_400/deepseek_chat_v3_2/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
