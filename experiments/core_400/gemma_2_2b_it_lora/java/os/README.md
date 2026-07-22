# Gemma 2 2B IT LoRA Multilingual — java — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it_lora__java__os` |
| Full model display name | Gemma 2 2B IT LoRA Multilingual |
| Raw model identifier | `gemma_2_2b_it_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | java |
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

- Prompt input file: [prompts/core_400/java/os/prompt_input_400.jsonl](../../../../../prompts/core_400/java/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/gemma_2_2b_it_lora/java/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_one_shot_java_400_v1.jsonl --base-model google/gemma-2-2b-it --adapter-path ${ADAPTER_ROOT}/gemma_2_2b_it_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_one_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/394c99e547f8_gemma_2_2b_it_lora_multilang_P1_one_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_one_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/fe63a138ddea_gemma_2_2b_it_lora_multilang_P1_one_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it_lora/java/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it_lora/java/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it_lora/java/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it_lora/java/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it_lora/java/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it_lora/java/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
f268aec78ca3577d1720b1463fa222cd8bea3304f1c38f3492121cbdcfb05828  experiments/core_400/gemma_2_2b_it_lora/java/os/generation/raw_generations.jsonl
93bfe6afe922ddd46a6262d22c32bbcd25ea7f556f469ae14072196b52e76804  experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/automatic_detailed.jsonl
b0d9c75263587906e0dea868abae420f90a08977a4dc110a73075692e8ef274d  experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/automatic_summary.json
bf9f3a0a3d64a1cbbf37b04e5b30eece55845c5c021f3d8289743565996e51b8  experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/code_grounded_detailed.jsonl
523016cca923877d8528d5bbebebfcc13f3773e79d4ae58337b5eea6dd8426e1  experiments/core_400/gemma_2_2b_it_lora/java/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
