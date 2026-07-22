# CodeGemma 2B — java — ZS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b__java__zs` |
| Full model display name | CodeGemma 2B |
| Raw model identifier | `google/codegemma-2b` |
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
- Command file: [experiments/core_400/codegemma_2b/java/zs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model google/codegemma-2b --input ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_zero_shot_java_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_zero_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/codegemma_2b_P1_zero_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/codegemma_2b_P1_zero_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/zs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/codegemma_2b_P1_zero_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b/java/zs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b/java/zs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b/java/zs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b/java/zs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b/java/zs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b/java/zs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b/java/zs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b/java/zs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b/java/zs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b/java/zs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
986090993b79d21a78ecc0c66b6398718c896b5eb30174f0f42bd0ecc53501a5  experiments/core_400/codegemma_2b/java/zs/generation/raw_generations.jsonl
ba45db8063b8232aa4cd240e095a45127819af3e8fd6d2d3a8fffa8f5af40483  experiments/core_400/codegemma_2b/java/zs/assessment/automatic_detailed.jsonl
abeaa11e25116daff3b92f709c9210e11f9a9244b1f86f5333a9f94a23227c15  experiments/core_400/codegemma_2b/java/zs/assessment/automatic_summary.json
97a0e9223a945ad40aca47a51594b46e6bdd5d3401b6499abceb5627ff1bfa60  experiments/core_400/codegemma_2b/java/zs/assessment/code_grounded_detailed.jsonl
42d3018bab38709bd5a4483f649724afe354d0653ad3d21bab25c90a96aef636  experiments/core_400/codegemma_2b/java/zs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
