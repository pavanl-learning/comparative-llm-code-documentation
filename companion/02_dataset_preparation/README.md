# Dataset preparation

## Purpose and research rationale

Documents CodeSearchNet-derived data preparation, filtering, balancing, and exclusions.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- Evidence not available in the repository.

## Actual scripts

- [scripts/data_preparation/eda_codesearchnet.py](../../scripts/data_preparation/eda_codesearchnet.py)
- [scripts/data_preparation/prepare_codesearchnet_balanced.py](../../scripts/data_preparation/prepare_codesearchnet_balanced.py)
- [scripts/fine_tuning/build_finetune_dataset.py](../../scripts/fine_tuning/build_finetune_dataset.py)
- [scripts/fine_tuning/finetune_lora_multilang.py](../../scripts/fine_tuning/finetune_lora_multilang.py)
- [scripts/fine_tuning/finetune_qwen_lora.py](../../scripts/fine_tuning/finetune_qwen_lora.py)
- [scripts/fine_tuning/run_full_finetune.sh](../../scripts/fine_tuning/run_full_finetune.sh)
- [scripts/fine_tuning/run_smoke_finetune.sh](../../scripts/fine_tuning/run_smoke_finetune.sh)
- [scripts/generation/run_finetuned_generation.py](../../scripts/generation/run_finetuned_generation.py)
- [scripts/prompting/create_balanced_prompt_subset.py](../../scripts/prompting/create_balanced_prompt_subset.py)

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- Evidence not available in the repository.

## Outputs

- [fine_tuning/codegemma_2b_lora/dataset_manifest.json](../../fine_tuning/codegemma_2b_lora/dataset_manifest.json)
- [fine_tuning/gemma_2_2b_it_lora/dataset_manifest.json](../../fine_tuning/gemma_2_2b_it_lora/dataset_manifest.json)
- [fine_tuning/qwen2_5_1_5b_instruct_lora/dataset_manifest.json](../../fine_tuning/qwen2_5_1_5b_instruct_lora/dataset_manifest.json)
- [fine_tuning/qwen2_5_coder_1_5b_instruct_lora/dataset_manifest.json](../../fine_tuning/qwen2_5_coder_1_5b_instruct_lora/dataset_manifest.json)
- [results/final/clean_full_results.csv](../../results/final/clean_full_results.csv)

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/02_dataset_preparation/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
