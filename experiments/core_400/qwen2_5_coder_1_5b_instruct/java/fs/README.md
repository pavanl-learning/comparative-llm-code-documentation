# Qwen2.5 Coder 1.5B Instruct — java — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_coder_1_5b_instruct__java__fs` |
| Full model display name | Qwen2.5 Coder 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-Coder-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
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
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-Coder-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/eval/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1_eval.json
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/java/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_coder_1_5b_instruct_P1_few_shot_java_400_v1_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
2bfdb5070c21278d0546e14be692c44b7f2f2e2d2ca9c79ed4c98666ed90e427  experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/generation/raw_generations.jsonl
6e73c68b3a0a001b604de2508cb2723462e20f3a306e4cdcce04f8b6c560f490  experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/automatic_detailed.jsonl
4aa61fa57dab35ef29f2a59530cd743408144e5323202fc3e14e981dcdc67f0c  experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/automatic_summary.json
57a17449fa90872f826d52c85ba31df35f7ac6a5549c7d80d0c40695bdd18acf  experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/code_grounded_detailed.jsonl
4350b1fdfaeb4dff7982db10a34eff929558858af87a742cd393852662a75f80  experiments/core_400/qwen2_5_coder_1_5b_instruct/java/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
