# GPT-5.1 Codex — javascript — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1_codex__javascript__fs` |
| Full model display name | GPT-5.1 Codex |
| Raw model identifier | `gpt-5.1-codex` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | javascript |
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

- Prompt input file: [prompts/core_400/javascript/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1_codex/javascript/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_few_shot_javascript_400_v1.jsonl --model gpt-5.1-codex --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_few_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_few_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_few_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_few_shot_javascript_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1_codex/javascript/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1_codex/javascript/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1_codex/javascript/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1_codex/javascript/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1_codex/javascript/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1_codex/javascript/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
4ee632e76ddb5c1200103b495e60d87d823a7a9e266f7a65ee317644cc8bd0cc  experiments/core_400/gpt_5_1_codex/javascript/fs/generation/raw_generations.jsonl
b24be17b27be2f919ca05cd10a459ae7ec188dc891e6652a9a91e61e45c9885f  experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/automatic_detailed.jsonl
3ef8dea69977ea9de1a94b6350e57a2d99d85924ecb60277ee547f86076340b4  experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/automatic_summary.json
37fad6b3467ada1dba3aac676755702c1331439ccbe2e7303014197b5369af33  experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/code_grounded_detailed.jsonl
282f5c79f8b7cac1822cc1f3090a39e7205f473efcc7bf072f1e843c5d4935f7  experiments/core_400/gpt_5_1_codex/javascript/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
