# CodeGemma 2B LoRA Multilingual — python — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b_lora__python__os` |
| Full model display name | CodeGemma 2B LoRA Multilingual |
| Raw model identifier | `codegemma_2b_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/os/prompt_input_400.jsonl](../../../../../prompts/core_400/python/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/codegemma_2b_lora/python/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_one_shot_python_400_v1.jsonl --base-model google/codegemma-2b --adapter-path ${ADAPTER_ROOT}/codegemma_2b_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_one_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/7e611c0afe5d_codegemma_2b_lora_multilang_P1_one_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_one_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/adfde55fd9fa_codegemma_2b_lora_multilang_P1_one_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b_lora/python/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b_lora/python/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b_lora/python/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b_lora/python/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b_lora/python/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b_lora/python/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b_lora/python/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b_lora/python/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b_lora/python/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b_lora/python/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
f5f4b78f784f2625588f7481f61bb89f69fb0bd037356be8a74ffa1b0065818b  experiments/core_400/codegemma_2b_lora/python/os/generation/raw_generations.jsonl
1c1773a70210f50f0064c43941fad8a30a8c215158403e4de58606c2d2983aed  experiments/core_400/codegemma_2b_lora/python/os/assessment/automatic_detailed.jsonl
c8e10bd3db947170565732f204e35b2bd40b7e773a8aa2674908ee3c8b239802  experiments/core_400/codegemma_2b_lora/python/os/assessment/automatic_summary.json
1d59dfa7f1e013f77df4c673bf74b3b8b9ca520b75085c9cc2b98025a75318fd  experiments/core_400/codegemma_2b_lora/python/os/assessment/code_grounded_detailed.jsonl
9a19faf23e4f9e87207d4ea9bb463575b1fdcc2cddf9ce1721911c5e762440fb  experiments/core_400/codegemma_2b_lora/python/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
