# Open-source execution

## Purpose and research rationale

Links to Hugging Face runner evidence and representative full-run artefacts.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- Evidence not available in the repository.

## Actual scripts

- [scripts/data_preparation/run_missing_qwen_few_shot_correctness_400.sh](../../scripts/data_preparation/run_missing_qwen_few_shot_correctness_400.sh)
- [scripts/data_preparation/run_qwen_base_zs_fs_400.sh](../../scripts/data_preparation/run_qwen_base_zs_fs_400.sh)
- [scripts/data_preparation/run_qwen_base_zs_fs_correctness_400.sh](../../scripts/data_preparation/run_qwen_base_zs_fs_correctness_400.sh)
- [scripts/evaluation/evaluate_generations.py](../../scripts/evaluation/evaluate_generations.py)
- [scripts/evaluation/evaluate_qwen_base_zs_fs_400.sh](../../scripts/evaluation/evaluate_qwen_base_zs_fs_400.sh)
- [scripts/fine_tuning/finetune_qwen_lora.py](../../scripts/fine_tuning/finetune_qwen_lora.py)
- [scripts/fine_tuning/run_full_codegemma_2b.sh](../../scripts/fine_tuning/run_full_codegemma_2b.sh)
- [scripts/fine_tuning/run_full_gemma_2_2b_it.sh](../../scripts/fine_tuning/run_full_gemma_2_2b_it.sh)
- [scripts/fine_tuning/run_full_qwen25_1_5b_instruct.sh](../../scripts/fine_tuning/run_full_qwen25_1_5b_instruct.sh)
- [scripts/fine_tuning/run_smoke_codegemma_2b.sh](../../scripts/fine_tuning/run_smoke_codegemma_2b.sh)
- [scripts/fine_tuning/run_smoke_gemma_2_2b_it.sh](../../scripts/fine_tuning/run_smoke_gemma_2_2b_it.sh)
- [scripts/fine_tuning/run_smoke_qwen25_1_5b_instruct.sh](../../scripts/fine_tuning/run_smoke_qwen25_1_5b_instruct.sh)
- Additional files omitted from this list: 9

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- Evidence not available in the repository.

## Outputs

- [experiments/core_400/codegemma_2b/java/fs/README.md](../../experiments/core_400/codegemma_2b/java/fs/README.md)
- [experiments/core_400/codegemma_2b/java/fs/assessment/automatic_detailed.jsonl](../../experiments/core_400/codegemma_2b/java/fs/assessment/automatic_detailed.jsonl)
- [experiments/core_400/codegemma_2b/java/fs/assessment/automatic_summary.json](../../experiments/core_400/codegemma_2b/java/fs/assessment/automatic_summary.json)
- [experiments/core_400/codegemma_2b/java/fs/assessment/code_grounded_detailed.jsonl](../../experiments/core_400/codegemma_2b/java/fs/assessment/code_grounded_detailed.jsonl)
- [experiments/core_400/codegemma_2b/java/fs/assessment/code_grounded_summary.json](../../experiments/core_400/codegemma_2b/java/fs/assessment/code_grounded_summary.json)
- [experiments/core_400/codegemma_2b/java/fs/command.txt](../../experiments/core_400/codegemma_2b/java/fs/command.txt)
- [experiments/core_400/codegemma_2b/java/fs/environment.txt](../../experiments/core_400/codegemma_2b/java/fs/environment.txt)
- [experiments/core_400/codegemma_2b/java/fs/examples/sample_records.md](../../experiments/core_400/codegemma_2b/java/fs/examples/sample_records.md)
- [experiments/core_400/codegemma_2b/java/fs/generation/raw_generations.jsonl](../../experiments/core_400/codegemma_2b/java/fs/generation/raw_generations.jsonl)
- [experiments/core_400/codegemma_2b/java/fs/input/input_reference.json](../../experiments/core_400/codegemma_2b/java/fs/input/input_reference.json)
- [experiments/core_400/codegemma_2b/java/fs/input/prompt_sample.jsonl](../../experiments/core_400/codegemma_2b/java/fs/input/prompt_sample.jsonl)
- [experiments/core_400/codegemma_2b/java/fs/run_manifest.json](../../experiments/core_400/codegemma_2b/java/fs/run_manifest.json)
- [experiments/core_400/codegemma_2b/java/fs/validation/checksums.sha256](../../experiments/core_400/codegemma_2b/java/fs/validation/checksums.sha256)
- [experiments/core_400/codegemma_2b/java/fs/validation/row_count_validation.json](../../experiments/core_400/codegemma_2b/java/fs/validation/row_count_validation.json)
- Additional files omitted from this list: 1330

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/06_open_source_execution/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
