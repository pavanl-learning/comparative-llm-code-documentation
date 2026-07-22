# Qwen2.5 1.5B Instruct — python — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct__python__zs` |
| Full model display name | Qwen2.5 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_1_5b_instruct_P1_zero_shot_python_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct/python/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
e452ebac590faa83a7463cf76b024992cda5ef31e515de563d54a6460d9da7a0  experiments/core_400/qwen2_5_1_5b_instruct/python/zs/generation/raw_generations.jsonl
85eb544627c1fc5e94023bb5c2075dc99a443ab73384b7c7c34de312186ee597  experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/automatic_detailed.jsonl
bc93b473489bfc9a102906ae1a4a7dd2bdcca3e8a45ca0976eded8170ed54d7e  experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/automatic_summary.json
c075ef9df0930052e1c9b9dc15456cf4a188495299210ca6e18cf31c4525d5ca  experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/code_grounded_detailed.jsonl
a107e40bfa65b5d4566ad9a645d76503bf090ba358df6e462c640fdffa287adc  experiments/core_400/qwen2_5_1_5b_instruct/python/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
