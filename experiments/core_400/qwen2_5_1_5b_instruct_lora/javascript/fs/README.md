# Qwen2.5 1.5B Instruct LoRA Multilingual — javascript — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct_lora__javascript__fs` |
| Full model display name | Qwen2.5 1.5B Instruct LoRA Multilingual |
| Raw model identifier | `qwen25_coder_1_5b_instruct_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
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
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_javascript_400_v1.jsonl --base-model Qwen/Qwen2.5-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_javascript_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/eval/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_javascript_400_v1_eval.json
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_javascript_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_javascript_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
6e6474ce207d1da34848a753dd1462cb30a1411335c6ae047f61261ac2d7426d  experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/generation/raw_generations.jsonl
6ed1e662b5feeeee658f68ae00aa1c1c44a43e79c386d78553f3dedd469243bb  experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/automatic_detailed.jsonl
43cf27dbd28a83f11319a3e0e46bfde1937472ef75ad915f03507b5d353bcf9a  experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/automatic_summary.json
6c3cd6c4d37da4d00b9cd087ff859fdc0b355bf5f90cae88cffdc7e3424d1cd0  experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/code_grounded_detailed.jsonl
af83f1c4b4f2865ba54778eff7163940e741be45080eb455c45f030e6ed8c72f  experiments/core_400/qwen2_5_1_5b_instruct_lora/javascript/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
