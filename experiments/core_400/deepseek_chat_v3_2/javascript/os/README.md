# DeepSeek Chat — javascript — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `deepseek_chat_v3_2__javascript__os` |
| Full model display name | DeepSeek Chat |
| Raw model identifier | `deepseek-chat` |
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
- Generation script: [scripts/generation/run_generation_deepseek.py](../../../../../scripts/generation/run_generation_deepseek.py)
- Command file: [experiments/core_400/deepseek_chat_v3_2/javascript/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_deepseek.py --input ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_javascript_400_v1.jsonl --model deepseek-chat --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/deepseek_chat_P1_one_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/deepseek_chat_P1_one_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/deepseek_chat_P1_one_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/deepseek_chat_v3_2/javascript/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/deepseek_chat_v3_2/javascript/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/deepseek_chat_v3_2/javascript/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/deepseek_chat_v3_2/javascript/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/deepseek_chat_v3_2/javascript/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/deepseek_chat_v3_2/javascript/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
a56a397d6858e7aa3d86b78e7ec75ccdf829273da481bc9740b34a3a80559286  experiments/core_400/deepseek_chat_v3_2/javascript/os/generation/raw_generations.jsonl
f7fae25503beceb635103c23e222d0f9a501e22ab638200a1fa5f880ce07e576  experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/automatic_detailed.jsonl
876c8acb41029c19c3e8597a442104daea837bf9fd6c339d3b51e2a13f63aa4b  experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/automatic_summary.json
e9a920e803b99ef80ddccc4a93362167f7535e405b892abedc6609ccaacc6b76  experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/code_grounded_detailed.jsonl
aee1ddb38efdd905f69c2aa55dcc342718b8f5c0615534d7cb4b4183be446e26  experiments/core_400/deepseek_chat_v3_2/javascript/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
