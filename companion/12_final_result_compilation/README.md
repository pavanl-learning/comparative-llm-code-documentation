# Final result compilation

## Purpose and research rationale

Links to authoritative 108-row final table, result manifests, plots, and traceability.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- Evidence not available in the repository.

## Actual scripts

- [scripts/data_preparation/generate_final_report_run_details.py](../../scripts/data_preparation/generate_final_report_run_details.py)
- [scripts/result_assembly/compare_prompt_results.py](../../scripts/result_assembly/compare_prompt_results.py)
- [scripts/result_assembly/generate_completed_qwen_thesis_tables.py](../../scripts/result_assembly/generate_completed_qwen_thesis_tables.py)
- [scripts/result_assembly/generate_final_results_tables_and_plots.py](../../scripts/result_assembly/generate_final_results_tables_and_plots.py)
- [scripts/result_assembly/organize_final_results.py](../../scripts/result_assembly/organize_final_results.py)
- [scripts/result_assembly/organize_segregated_results.py](../../scripts/result_assembly/organize_segregated_results.py)
- [scripts/result_assembly/per_language_comparison.py](../../scripts/result_assembly/per_language_comparison.py)

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- [manifests/validation/final_publication_gate.json](../../manifests/validation/final_publication_gate.json)
- [manifests/validation/final_result_row_trace.csv](../../manifests/validation/final_result_row_trace.csv)
- [validation/final_result_traceability.csv](../../validation/final_result_traceability.csv)
- [validation/final_result_traceability_summary.md](../../validation/final_result_traceability_summary.md)

## Outputs

- [fine_tuning/codegemma_2b_lora/final_adapter_manifest.json](../../fine_tuning/codegemma_2b_lora/final_adapter_manifest.json)
- [fine_tuning/gemma_2_2b_it_lora/final_adapter_manifest.json](../../fine_tuning/gemma_2_2b_it_lora/final_adapter_manifest.json)
- [fine_tuning/qwen2_5_1_5b_instruct_lora/final_adapter_manifest.json](../../fine_tuning/qwen2_5_1_5b_instruct_lora/final_adapter_manifest.json)
- [fine_tuning/qwen2_5_coder_1_5b_instruct_lora/final_adapter_manifest.json](../../fine_tuning/qwen2_5_coder_1_5b_instruct_lora/final_adapter_manifest.json)
- [manifests/validation/final_publication_gate.json](../../manifests/validation/final_publication_gate.json)
- [manifests/validation/final_result_row_trace.csv](../../manifests/validation/final_result_row_trace.csv)
- [results/final/clean_full_results.csv](../../results/final/clean_full_results.csv)
- [results/final/family_language_prompt_averages.csv](../../results/final/family_language_prompt_averages.csv)
- [results/final/final_prompt_run_details.csv](../../results/final/final_prompt_run_details.csv)
- [results/final/final_report_run_details.md](../../results/final/final_report_run_details.md)
- [results/final/java_full_comparison.csv](../../results/final/java_full_comparison.csv)
- [results/final/javascript_full_comparison.csv](../../results/final/javascript_full_comparison.csv)
- [results/final/language_level_averages.csv](../../results/final/language_level_averages.csv)
- [results/final/language_prompt_averages.csv](../../results/final/language_prompt_averages.csv)
- Additional files omitted from this list: 6

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/12_final_result_compilation/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
