# Qwen2.5 Coder 1.5B Instruct LoRA Multilingual — javascript — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_coder_1_5b_instruct_lora__javascript__os` |
| Full model display name | Qwen2.5 Coder 1.5B Instruct LoRA Multilingual |
| Raw model identifier | `qwen25_coder_1_5b_instruct_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
| Language | javascript |
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

- Prompt input file: [prompts/core_400/javascript/os/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_coder_1_5b_lora_multilang/qwen25_coder_1_5b_instruct_lora_multilang_P1_one_shot_javascript_400_v1.jsonl --base-model Qwen/Qwen2.5-Coder-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_coder_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_coder_1_5b_lora_multilang/qwen25_coder_1_5b_instruct_lora_multilang_P1_one_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/eval/qwen25_coder_1_5b_instruct_lora_multilang_P1_one_shot_javascript_400_v1_eval.json
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_coder_1_5b_lora_multilang/qwen25_coder_1_5b_instruct_lora_multilang_P1_one_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_coder_1_5b_instruct_lora_multilang_P1_one_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
ed1c407758f7856658d0daac41f37d44c730291f16620153ddb1a14f29135976  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/generation/raw_generations.jsonl
9a240c7c01a54534f62700817570a695e19eac38e026f31c0533407e723ad658  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/automatic_detailed.jsonl
aa914f23ee18df6c8de166c3a089ce5b73f071f9136f10ba77671e784c3b4524  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/automatic_summary.json
c58d8069837a5d0037cca56746e00a387407ff6908cbfe5e1b64bdf970da78f8  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/code_grounded_detailed.jsonl
9e5cc95faed7f55535cd56753452d4b77d76db5ae170148374437b21cf5f1393  experiments/core_400/qwen2_5_coder_1_5b_instruct_lora/javascript/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
