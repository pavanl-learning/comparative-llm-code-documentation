# Reproducibility and validation

## Purpose and research rationale

Documents requirements, command catalogue, manifests, checksums, row counts, links, and gate reports.

This page is a navigation companion. It links to canonical repository artefacts rather than duplicating full 400-row evidence files.

## Inputs

- Evidence not available in the repository.

## Actual scripts

- [scripts/result_assembly/organize_segregated_results.py](../../scripts/result_assembly/organize_segregated_results.py)

## Exact commands found in the repository

- [COMMAND_CATALOGUE.md](../../COMMAND_CATALOGUE.md)
- Per-condition commands are linked from [RUN_INDEX.md](../../RUN_INDEX.md).

## Key configuration values

Configuration evidence is taken from scripts, run manifests, command files, training manifests, and validation reports linked on this page. Unsupported configuration claims are intentionally not added.

## Processing and validation steps

- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)
- [manifests/public_artifact_manifest.csv](../../manifests/public_artifact_manifest.csv)
- [manifests/public_file_manifest.csv](../../manifests/public_file_manifest.csv)
- [manifests/public_sha256.csv](../../manifests/public_sha256.csv)
- [manifests/source_to_public_manifest.csv](../../manifests/source_to_public_manifest.csv)
- [manifests/validation/absolute_path_report.csv](../../manifests/validation/absolute_path_report.csv)
- [manifests/validation/broken_link_report.csv](../../manifests/validation/broken_link_report.csv)
- [manifests/validation/core_108_validation.csv](../../manifests/validation/core_108_validation.csv)
- [manifests/validation/detailed_summary_recomputation.csv](../../manifests/validation/detailed_summary_recomputation.csv)
- [manifests/validation/final_publication_gate.json](../../manifests/validation/final_publication_gate.json)
- [manifests/validation/final_result_row_trace.csv](../../manifests/validation/final_result_row_trace.csv)
- [manifests/validation/large_file_report.csv](../../manifests/validation/large_file_report.csv)
- Additional files omitted from this list: 27

## Outputs

- [experiments/core_400/codegemma_2b/java/fs/run_manifest.json](../../experiments/core_400/codegemma_2b/java/fs/run_manifest.json)
- [experiments/core_400/codegemma_2b/java/fs/validation/checksums.sha256](../../experiments/core_400/codegemma_2b/java/fs/validation/checksums.sha256)
- [experiments/core_400/codegemma_2b/java/fs/validation/row_count_validation.json](../../experiments/core_400/codegemma_2b/java/fs/validation/row_count_validation.json)
- [experiments/core_400/codegemma_2b/java/fs/validation/sample_id_validation.json](../../experiments/core_400/codegemma_2b/java/fs/validation/sample_id_validation.json)
- [experiments/core_400/codegemma_2b/java/fs/validation/schema_validation.json](../../experiments/core_400/codegemma_2b/java/fs/validation/schema_validation.json)
- [experiments/core_400/codegemma_2b/java/fs/validation/source_provenance.json](../../experiments/core_400/codegemma_2b/java/fs/validation/source_provenance.json)
- [experiments/core_400/codegemma_2b/java/os/run_manifest.json](../../experiments/core_400/codegemma_2b/java/os/run_manifest.json)
- [experiments/core_400/codegemma_2b/java/os/validation/checksums.sha256](../../experiments/core_400/codegemma_2b/java/os/validation/checksums.sha256)
- [experiments/core_400/codegemma_2b/java/os/validation/row_count_validation.json](../../experiments/core_400/codegemma_2b/java/os/validation/row_count_validation.json)
- [experiments/core_400/codegemma_2b/java/os/validation/sample_id_validation.json](../../experiments/core_400/codegemma_2b/java/os/validation/sample_id_validation.json)
- [experiments/core_400/codegemma_2b/java/os/validation/schema_validation.json](../../experiments/core_400/codegemma_2b/java/os/validation/schema_validation.json)
- [experiments/core_400/codegemma_2b/java/os/validation/source_provenance.json](../../experiments/core_400/codegemma_2b/java/os/validation/source_provenance.json)
- [experiments/core_400/codegemma_2b/java/zs/run_manifest.json](../../experiments/core_400/codegemma_2b/java/zs/run_manifest.json)
- [experiments/core_400/codegemma_2b/java/zs/validation/checksums.sha256](../../experiments/core_400/codegemma_2b/java/zs/validation/checksums.sha256)
- Additional files omitted from this list: 683

## Representative sample evidence

- Evidence previews, where generated from actual artefacts, are stored under [companion/14_reproducibility_and_validation/evidence_previews](evidence_previews).

## Full-evidence links

- [experiments/core_400/README.md](../../experiments/core_400/README.md)
- [experiments/CONDITION_MATRIX.md](../../experiments/CONDITION_MATRIX.md)
- [manifests/core_108_condition_manifest.csv](../../manifests/core_108_condition_manifest.csv)

## Relationship to the next stage

This stage feeds the subsequent implementation stage shown in [workflow/research_implementation_workflow.mmd](../../workflow/research_implementation_workflow.mmd).

## Related Chapter 4 subsection placeholder

Insert the final thesis subsection number and title here after the dissertation chapter numbering is finalised.
