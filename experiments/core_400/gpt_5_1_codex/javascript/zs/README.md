# GPT-5.1 Codex — javascript — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1_codex__javascript__zs` |
| Full model display name | GPT-5.1 Codex |
| Raw model identifier | `gpt-5.1-codex` |
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
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1_codex/javascript/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_javascript_400_v1.jsonl --model gpt-5.1-codex --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_zero_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/gpt_5_1_codex_P1_zero_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1_codex/javascript/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1_codex/javascript/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1_codex/javascript/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1_codex/javascript/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1_codex/javascript/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1_codex/javascript/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
128f7a332c9854352b791ce10073b794ee950ce75206e5b8da6003e061e5d85d  experiments/core_400/gpt_5_1_codex/javascript/zs/generation/raw_generations.jsonl
15b34ac1cc0436603e74471e7f72311124215d07888f00846f9a78f60db81578  experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/automatic_detailed.jsonl
844b135f9a576522e178bebe3ca37888e3b7951ec191aff883b5ca8f5fed8ae9  experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/automatic_summary.json
cf8ea8c63ada79d8849d95c3ba87bdd6c464268aafe40a088cbafffacee7245a  experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/code_grounded_detailed.jsonl
6a1d3493ed46082710c18ba6b6f89e4422a646e3ac67ef5c4698d140b0353f8c  experiments/core_400/gpt_5_1_codex/javascript/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
