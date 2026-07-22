# Qwen2.5 1.5B Instruct — javascript — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct__javascript__fs` |
| Full model display name | Qwen2.5 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_1_5b_instruct_P1_few_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
8eb1c3666d25ef702cfe88f54efdd84ff38dc08ba00383609b89ea070123910f  experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/generation/raw_generations.jsonl
69432bd46e0d3fbd1b6ca7b68b540d16b28ce4a56c7da2ee9d9159b19192d799  experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/automatic_detailed.jsonl
3bbc50ae7e6f4cc5d5767aac5a13194e743800745f4ef26eb84397b851243004  experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/automatic_summary.json
69932a1e04488f0c84d71962a15f228268434f3d0ec6701e452a6a34f13db293  experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/code_grounded_detailed.jsonl
81cb9c99dcfa7eb8f25cf3c91fe0438144385f7a26e8b94d9e57966c8e262309  experiments/core_400/qwen2_5_1_5b_instruct/javascript/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
