# LoRA fine-tuning

## Purpose and research rationale

Documents split construction, training configuration, adapter evidence, inference, and exclusions.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- Evidence not available in the repository.

## Actual scripts

- [scripts/data_preparation/run_missing_lora_downstream_400.py](../../scripts/data_preparation/run_missing_lora_downstream_400.py)
- [scripts/fine_tuning/build_finetune_dataset.py](../../scripts/fine_tuning/build_finetune_dataset.py)
- [scripts/fine_tuning/finetune_lora_multilang.py](../../scripts/fine_tuning/finetune_lora_multilang.py)
- [scripts/fine_tuning/finetune_qwen_lora.py](../../scripts/fine_tuning/finetune_qwen_lora.py)
- [scripts/fine_tuning/run_full_finetune.sh](../../scripts/fine_tuning/run_full_finetune.sh)
- [scripts/fine_tuning/run_smoke_finetune.sh](../../scripts/fine_tuning/run_smoke_finetune.sh)
- [scripts/fine_tuning/train_sft_lora.py](../../scripts/fine_tuning/train_sft_lora.py)
- [scripts/generation/run_finetuned_generation.py](../../scripts/generation/run_finetuned_generation.py)
- [scripts/generation/run_generation_hf_lora.py](../../scripts/generation/run_generation_hf_lora.py)

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- Evidence not available in the repository.

## Outputs

- [experiments/core_400/codegemma_2b_lora/java/fs/README.md](../../experiments/core_400/codegemma_2b_lora/java/fs/README.md)
- [experiments/core_400/codegemma_2b_lora/java/fs/assessment/automatic_detailed.jsonl](../../experiments/core_400/codegemma_2b_lora/java/fs/assessment/automatic_detailed.jsonl)
- [experiments/core_400/codegemma_2b_lora/java/fs/assessment/automatic_summary.json](../../experiments/core_400/codegemma_2b_lora/java/fs/assessment/automatic_summary.json)
- [experiments/core_400/codegemma_2b_lora/java/fs/assessment/code_grounded_detailed.jsonl](../../experiments/core_400/codegemma_2b_lora/java/fs/assessment/code_grounded_detailed.jsonl)
- [experiments/core_400/codegemma_2b_lora/java/fs/assessment/code_grounded_summary.json](../../experiments/core_400/codegemma_2b_lora/java/fs/assessment/code_grounded_summary.json)
- [experiments/core_400/codegemma_2b_lora/java/fs/command.txt](../../experiments/core_400/codegemma_2b_lora/java/fs/command.txt)
- [experiments/core_400/codegemma_2b_lora/java/fs/environment.txt](../../experiments/core_400/codegemma_2b_lora/java/fs/environment.txt)
- [experiments/core_400/codegemma_2b_lora/java/fs/examples/sample_records.md](../../experiments/core_400/codegemma_2b_lora/java/fs/examples/sample_records.md)
- [experiments/core_400/codegemma_2b_lora/java/fs/generation/raw_generations.jsonl](../../experiments/core_400/codegemma_2b_lora/java/fs/generation/raw_generations.jsonl)
- [experiments/core_400/codegemma_2b_lora/java/fs/input/input_reference.json](../../experiments/core_400/codegemma_2b_lora/java/fs/input/input_reference.json)
- [experiments/core_400/codegemma_2b_lora/java/fs/input/prompt_sample.jsonl](../../experiments/core_400/codegemma_2b_lora/java/fs/input/prompt_sample.jsonl)
- [experiments/core_400/codegemma_2b_lora/java/fs/run_manifest.json](../../experiments/core_400/codegemma_2b_lora/java/fs/run_manifest.json)
- [experiments/core_400/codegemma_2b_lora/java/fs/validation/checksums.sha256](../../experiments/core_400/codegemma_2b_lora/java/fs/validation/checksums.sha256)
- [experiments/core_400/codegemma_2b_lora/java/fs/validation/row_count_validation.json](../../experiments/core_400/codegemma_2b_lora/java/fs/validation/row_count_validation.json)
- Additional files omitted from this list: 683

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/08_lora_fine_tuning/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
