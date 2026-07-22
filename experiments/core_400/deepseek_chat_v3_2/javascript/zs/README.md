# DeepSeek Chat — javascript — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `deepseek_chat_v3_2__javascript__zs` |
| Full model display name | DeepSeek Chat |
| Raw model identifier | `deepseek-chat` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | javascript |
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

- Prompt input file: [prompts/core_400/javascript/zs/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/zs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_deepseek.py](../../../../../scripts/generation/run_generation_deepseek.py)
- Command file: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_deepseek.py --input ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_zero_shot_javascript_400_v1.jsonl --model deepseek-chat --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_zero_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_zero_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_zero_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/deepseek_chat_P1_zero_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/deepseek_chat_v3_2/javascript/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
8ed5d09e4e7880b8132124fbfa3c5fbf911e87f961564248ed23502923fcf7f0  experiments/core_400/deepseek_chat_v3_2/javascript/zs/generation/raw_generations.jsonl
864ba0333dcd2da54f95448cca31f0bf1c254d14bc8c0b3a71f3646a3dd73fb5  experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/automatic_detailed.jsonl
a8a6a068f383d2f00856ffad9cf6c114b2cfbcb2f6a87afe24c3cba8c49e31a4  experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/automatic_summary.json
7cc6931a4b15335b7a5f5d8b18367facc17ad8f52337fde30e2b4e0edfcca08c  experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/code_grounded_detailed.jsonl
804d207c61f1cdf9f742c29e91b6e56c6eac59c9e69b3a1ea28f4904bf25b525  experiments/core_400/deepseek_chat_v3_2/javascript/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
