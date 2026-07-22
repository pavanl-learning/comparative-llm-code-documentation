# Prompt engineering

## Purpose and research rationale

Documents zero-shot, one-shot, few-shot prompt construction and prompt artefact validation.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- [prompts/core_400/java/fs/prompt_input_400.jsonl](../../prompts/core_400/java/fs/prompt_input_400.jsonl)
- [prompts/core_400/java/os/prompt_input_400.jsonl](../../prompts/core_400/java/os/prompt_input_400.jsonl)
- [prompts/core_400/java/zs/prompt_input_400.jsonl](../../prompts/core_400/java/zs/prompt_input_400.jsonl)
- [prompts/core_400/javascript/fs/prompt_input_400.jsonl](../../prompts/core_400/javascript/fs/prompt_input_400.jsonl)
- [prompts/core_400/javascript/os/prompt_input_400.jsonl](../../prompts/core_400/javascript/os/prompt_input_400.jsonl)
- [prompts/core_400/javascript/zs/prompt_input_400.jsonl](../../prompts/core_400/javascript/zs/prompt_input_400.jsonl)
- [prompts/core_400/python/fs/prompt_input_400.jsonl](../../prompts/core_400/python/fs/prompt_input_400.jsonl)
- [prompts/core_400/python/os/prompt_input_400.jsonl](../../prompts/core_400/python/os/prompt_input_400.jsonl)
- [prompts/core_400/python/zs/prompt_input_400.jsonl](../../prompts/core_400/python/zs/prompt_input_400.jsonl)

## Actual scripts

- [scripts/data_preparation/run_missing_qwen_few_shot_correctness_400.sh](../../scripts/data_preparation/run_missing_qwen_few_shot_correctness_400.sh)
- [scripts/data_preparation/run_one_shot_400.sh](../../scripts/data_preparation/run_one_shot_400.sh)
- [scripts/data_preparation/run_qwen_base_zs_fs_400.sh](../../scripts/data_preparation/run_qwen_base_zs_fs_400.sh)
- [scripts/data_preparation/run_qwen_base_zs_fs_correctness_400.sh](../../scripts/data_preparation/run_qwen_base_zs_fs_correctness_400.sh)
- [scripts/evaluation/evaluate_one_shot_400.sh](../../scripts/evaluation/evaluate_one_shot_400.sh)
- [scripts/evaluation/evaluate_qwen_base_zs_fs_400.sh](../../scripts/evaluation/evaluate_qwen_base_zs_fs_400.sh)
- [scripts/prompting/build_prompts.py](../../scripts/prompting/build_prompts.py)
- [scripts/prompting/build_shot_prompts.py](../../scripts/prompting/build_shot_prompts.py)
- [scripts/prompting/create_balanced_prompt_subset.py](../../scripts/prompting/create_balanced_prompt_subset.py)
- [scripts/prompting/create_demo_bank.py](../../scripts/prompting/create_demo_bank.py)
- [scripts/result_assembly/compare_prompt_results.py](../../scripts/result_assembly/compare_prompt_results.py)

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- [validation/repository_statistics.json](../../validation/repository_statistics.json)
- [validation/repository_statistics.md](../../validation/repository_statistics.md)
- [validation/source_repository_baseline.json](../../validation/source_repository_baseline.json)
- [validation/source_repository_baseline.md](../../validation/source_repository_baseline.md)

## Outputs

- [diagnostics/README.md](../../diagnostics/README.md)
- [experiments/BY_PROMPT_REGIME.md](../../experiments/BY_PROMPT_REGIME.md)
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
- Additional files omitted from this list: 1828

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/04_prompt_engineering/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
