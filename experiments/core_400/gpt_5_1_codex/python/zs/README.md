# GPT-5.1 Codex — python — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1_codex__python__zs` |
| Full model display name | GPT-5.1 Codex |
| Raw model identifier | `gpt-5.1-codex` |
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
- Command file: [experiments/core_400/gpt_5_1_codex/python/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_python_400_v1.jsonl --model gpt-5.1-codex --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_zero_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/gpt_5_1_codex_P1_zero_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1_codex/python/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1_codex/python/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1_codex/python/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1_codex/python/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1_codex/python/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1_codex/python/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1_codex/python/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1_codex/python/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1_codex/python/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1_codex/python/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
ac58f377da3d7121a2a71fc7568059078f1c0f38e46d775be9cd45042c21d486  experiments/core_400/gpt_5_1_codex/python/zs/generation/raw_generations.jsonl
d26163b11d7576680077eeb175b301b9076a82cff13111169a265f5689baef5a  experiments/core_400/gpt_5_1_codex/python/zs/assessment/automatic_detailed.jsonl
4c2c01b4b341fc7856e42ed072b5a3e75d4548a3f8b20cc1d252673f6e45e674  experiments/core_400/gpt_5_1_codex/python/zs/assessment/automatic_summary.json
6afdeb58d596b089596b7e242226205b7ce64748018f12c00177b82866e1d171  experiments/core_400/gpt_5_1_codex/python/zs/assessment/code_grounded_detailed.jsonl
7d638962a60da9d6d76a2d71b5a2c6bded6e688d5a933fbfdff95418ac82ada1  experiments/core_400/gpt_5_1_codex/python/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
