# CodeGemma 2B LoRA Multilingual — java — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `codegemma_2b_lora__java__os` |
| Full model display name | CodeGemma 2B LoRA Multilingual |
| Raw model identifier | `codegemma_2b_lora_multilang` |
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
- Command file: [experiments/core_400/codegemma_2b_lora/java/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_one_shot_java_400_v1.jsonl --base-model google/codegemma-2b --adapter-path ${ADAPTER_ROOT}/codegemma_2b_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_one_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/636e0ce9eb98_codegemma_2b_lora_multilang_P1_one_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/codegemma_2b_lora_multilang/codegemma_2b_lora_multilang_P1_one_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/b074b30c28ae_codegemma_2b_lora_multilang_P1_one_shot_java_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/codegemma_2b_lora/java/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/codegemma_2b_lora/java/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/codegemma_2b_lora/java/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/codegemma_2b_lora/java/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/codegemma_2b_lora/java/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/codegemma_2b_lora/java/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/codegemma_2b_lora/java/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/codegemma_2b_lora/java/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/codegemma_2b_lora/java/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/codegemma_2b_lora/java/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
a7d30decac5be2d03dc153af7e079ac05f131f5eaa82d060416cc3e68729a1a4  experiments/core_400/codegemma_2b_lora/java/os/generation/raw_generations.jsonl
641151584969f0495e403162397b6bcecc1c718f3cc9c0b2de3cf0da36b50c97  experiments/core_400/codegemma_2b_lora/java/os/assessment/automatic_detailed.jsonl
56463ceb26bbd02dde4cbac8ccacb08df098133244f7fb999a1b26dc8f6fafc7  experiments/core_400/codegemma_2b_lora/java/os/assessment/automatic_summary.json
0dac1573fe33cf4228e88c8e6f1388629fffb8455d89bbd07d6394c330b9682f  experiments/core_400/codegemma_2b_lora/java/os/assessment/code_grounded_detailed.jsonl
d41c37ff48ed2fd29e4434f17a9af1bb397bab7a2e6b66aad8296661740d0b26  experiments/core_400/codegemma_2b_lora/java/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
