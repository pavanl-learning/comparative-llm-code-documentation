# Sample size and diagnostics

## Purpose and research rationale

Distinguishes exploratory, smoke, saturation, and final 400-row run evidence.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- [data/benchmark/eda/eda_sample_size_feasibility.csv](../../data/benchmark/eda/eda_sample_size_feasibility.csv)
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

- [scripts/data_preparation/run_missing_lora_downstream_400.py](../../scripts/data_preparation/run_missing_lora_downstream_400.py)
- [scripts/data_preparation/run_missing_qwen_few_shot_correctness_400.sh](../../scripts/data_preparation/run_missing_qwen_few_shot_correctness_400.sh)
- [scripts/data_preparation/run_one_shot_400.sh](../../scripts/data_preparation/run_one_shot_400.sh)
- [scripts/data_preparation/run_qwen_base_zs_fs_400.sh](../../scripts/data_preparation/run_qwen_base_zs_fs_400.sh)
- [scripts/data_preparation/run_qwen_base_zs_fs_correctness_400.sh](../../scripts/data_preparation/run_qwen_base_zs_fs_correctness_400.sh)
- [scripts/evaluation/evaluate_one_shot_400.sh](../../scripts/evaluation/evaluate_one_shot_400.sh)
- [scripts/evaluation/evaluate_qwen_base_zs_fs_400.sh](../../scripts/evaluation/evaluate_qwen_base_zs_fs_400.sh)
- [scripts/evaluation/evaluate_saturation_runs.sh](../../scripts/evaluation/evaluate_saturation_runs.sh)
- [scripts/fine_tuning/run_smoke_codegemma_2b.sh](../../scripts/fine_tuning/run_smoke_codegemma_2b.sh)
- [scripts/fine_tuning/run_smoke_finetune.sh](../../scripts/fine_tuning/run_smoke_finetune.sh)
- [scripts/fine_tuning/run_smoke_gemma_2_2b_it.sh](../../scripts/fine_tuning/run_smoke_gemma_2_2b_it.sh)
- [scripts/fine_tuning/run_smoke_qwen25_1_5b_instruct.sh](../../scripts/fine_tuning/run_smoke_qwen25_1_5b_instruct.sh)
- Additional files omitted from this list: 3

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- [manifests/validation/sample_id_set_audit.csv](../../manifests/validation/sample_id_set_audit.csv)

## Outputs

- [diagnostics/README.md](../../diagnostics/README.md)
- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/core_400/RUN_INDEX.md](../../experiments/core_400/RUN_INDEX.md)
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
- Additional files omitted from this list: 1839

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/05_sample_size_and_diagnostics/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
