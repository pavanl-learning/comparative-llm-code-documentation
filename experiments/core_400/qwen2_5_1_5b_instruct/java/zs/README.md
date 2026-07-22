# Qwen2.5 1.5B Instruct — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct__java__zs` |
| Full model display name | Qwen2.5 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_1_5b_instruct_P1_zero_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
1ab24f6aa521b58a1776d12ed2c6e2c84380efec77864a9f582bfacfa8c8cdb6  experiments/core_400/qwen2_5_1_5b_instruct/java/zs/generation/raw_generations.jsonl
62a4c661409ecdc2cbd9b1aba4fcd6e39e84a50a1a2970e29ea9c1fbf9256eb8  experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/automatic_detailed.jsonl
0d41ee9d2443f25defef0893ddf99b001b27377bacc48c6db9eea72b554aa2a4  experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/automatic_summary.json
a5fa2f5b49c806306ae17c12f9a8862f99516af99fc58ea28c694b23a3c5f547  experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/code_grounded_detailed.jsonl
a3d6138c2725f1c1059b9c1a6f64cd02f8e064f01c7c93b90dc6f09cde2df936  experiments/core_400/qwen2_5_1_5b_instruct/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
