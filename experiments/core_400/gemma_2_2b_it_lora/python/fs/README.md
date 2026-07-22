# Gemma 2 2B IT LoRA Multilingual — python — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gemma_2_2b_it_lora__python__fs` |
| Full model display name | Gemma 2 2B IT LoRA Multilingual |
| Raw model identifier | `gemma_2_2b_it_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/python/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/gemma_2_2b_it_lora/python/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_few_shot_python_400_v1.jsonl --base-model google/gemma-2-2b-it --adapter-path ${ADAPTER_ROOT}/gemma_2_2b_it_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_few_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/80f917558e10_gemma_2_2b_it_lora_multilang_P1_few_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/gemma_2_2b_it_lora_multilang/gemma_2_2b_it_lora_multilang_P1_few_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/592b1872a60d_gemma_2_2b_it_lora_multilang_P1_few_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gemma_2_2b_it_lora/python/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gemma_2_2b_it_lora/python/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gemma_2_2b_it_lora/python/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gemma_2_2b_it_lora/python/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gemma_2_2b_it_lora/python/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gemma_2_2b_it_lora/python/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
3adc67125d4960d79feef3585b3cd7144e2d9edcbc99b8ce6e2d04987a86732f  experiments/core_400/gemma_2_2b_it_lora/python/fs/generation/raw_generations.jsonl
6cf00d9b3a256e5449a8a6b02406d808da02cf83bf8e06abd73dc9375016412d  experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/automatic_detailed.jsonl
6dd21b06171f51662eaf176aef99661302c4d1ba54a359bfca68dd96e92d22bd  experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/automatic_summary.json
ce98d486562c4396229148b1e3412d34a4bf39313ad506a3200ab3ab1c850b3f  experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/code_grounded_detailed.jsonl
458968b2e53f33bfe219d23f2f63f682e0d77d9d9638be4e448dcf2d50088f12  experiments/core_400/gemma_2_2b_it_lora/python/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
