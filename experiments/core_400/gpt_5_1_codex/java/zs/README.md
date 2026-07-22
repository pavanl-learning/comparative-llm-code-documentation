# GPT-5.1 Codex — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1_codex__java__zs` |
| Full model display name | GPT-5.1 Codex |
| Raw model identifier | `gpt-5.1-codex` |
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
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1_codex/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_java_400_v1.jsonl --model gpt-5.1-codex --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/correctness/gpt_5_1_codex_P1_zero_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1_codex/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1_codex/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1_codex/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1_codex/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1_codex/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1_codex/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1_codex/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1_codex/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1_codex/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1_codex/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
09ce2ec8c9fef7a28da8bc79325d248bc182edad7b9955635c11e38f1f493383  experiments/core_400/gpt_5_1_codex/java/zs/generation/raw_generations.jsonl
e3f4c26a2814a96b1a008e3f0064812489eab50921e1bf04a18b9f9acde4b91c  experiments/core_400/gpt_5_1_codex/java/zs/assessment/automatic_detailed.jsonl
8783746e7bc55910f35ffe3945d13adb2b9ed62b9992b37cf1f143e887be74a2  experiments/core_400/gpt_5_1_codex/java/zs/assessment/automatic_summary.json
d4b6b7d4df328f11943632bfbe82ba68e308673a8ba173a3204ccdc63ed499cb  experiments/core_400/gpt_5_1_codex/java/zs/assessment/code_grounded_detailed.jsonl
763dfec769551e80a9b79dcdb0ce052a1d78e8d2eb283723f8345015b83df3cc  experiments/core_400/gpt_5_1_codex/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
