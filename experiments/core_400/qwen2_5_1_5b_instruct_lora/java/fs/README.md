# Qwen2.5 1.5B Instruct LoRA Multilingual — java — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_1_5b_instruct_lora__java__fs` |
| Full model display name | Qwen2.5 1.5B Instruct LoRA Multilingual |
| Raw model identifier | `qwen25_coder_1_5b_instruct_lora_multilang` |
| Model group | open-source-fine-tuned |
| Model category | lora_fine_tuned |
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
- Generation script: [scripts/generation/run_finetuned_generation.py](../../../../../scripts/generation/run_finetuned_generation.py)
- Command file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_finetuned_generation.py --input ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_java_400_v1.jsonl --base-model Qwen/Qwen2.5-1.5B-Instruct --adapter-path ${ADAPTER_ROOT}/qwen2_5_1_5b_instruct_lora --max-new-tokens 64 --temperature 0.0 --top-p 1.0 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/_long_paths/d55b8e9f9b3a_qwen25_1_5b_instruct_lora_multilang_P1_few_shot_java_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source-fine-tuned/qwen25_1_5b_instruct_lora_multilang/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-lora/correctness/qwen25_1_5b_instruct_lora_multilang_P1_few_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
383ed423a52a8bf29af6e8c8ca55fb969fddc5045fcc045304bb0a860bd72e2d  experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/generation/raw_generations.jsonl
8368019733109c4b13149aa53e401e8fa291a68258d75ec7a29574b1632f41ea  experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/automatic_detailed.jsonl
c00838ff7b0ac47bba6e7bbe64063a5e81a126fd3d83cf262aed6183be135d7a  experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/automatic_summary.json
65be89fbfb1fd3f7ac79ace5ad895ccf0a101aceab5b0b32480e6488e3870ac9  experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/code_grounded_detailed.jsonl
ef816a385339af1b7fd186f79652b461b222a4e511795bb80e070c449b145ece  experiments/core_400/qwen2_5_1_5b_instruct_lora/java/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
