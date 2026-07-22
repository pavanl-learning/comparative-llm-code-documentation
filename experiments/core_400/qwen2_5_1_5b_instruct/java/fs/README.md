# Qwen2.5 1.5B Instruct — java — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct__java__fs` |
| Full model display name | Qwen2.5 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
| Language | java |
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

- Prompt input file: [prompts/core_400/java/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/java/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_java_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/qwen25_1_5b_instruct_P1_few_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_few_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_1_5b_instruct_P1_few_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct/java/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
baffa982a4da2984b3b30b7c9676be95e378d7184e5cfa096b13871b4d204074  experiments/core_400/qwen2_5_1_5b_instruct/java/fs/generation/raw_generations.jsonl
d4c6805c641a9d66a4f1d8961baf4d6d06cb0ad4944bddc77dede2acc01c14a0  experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/automatic_detailed.jsonl
15d97b59ed49aff0f1268048e731d27acea5854c769dac8e81f8f418d5792dc1  experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/automatic_summary.json
ac377eec86cb9db8b897f7feb33428918e237659aad6a91efcfa7e66071c51eb  experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/code_grounded_detailed.jsonl
be0ccd2544f69c3d7c32ffd694e2ebdfb9eb61a02581d20bf5731784b7c99cd8  experiments/core_400/qwen2_5_1_5b_instruct/java/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
