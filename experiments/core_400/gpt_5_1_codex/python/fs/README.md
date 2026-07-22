# GPT-5.1 Codex — python — FS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `gpt_5_1_codex__python__fs` |
| Full model display name | GPT-5.1 Codex |
| Raw model identifier | `gpt-5.1-codex` |
| Model group | commercial-new |
| Model category | commercial_api |
| Language | python |
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

- Prompt input file: [prompts/core_400/python/fs/prompt_input_400.jsonl](../../../../../prompts/core_400/python/fs/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_openai_responses.py](../../../../../scripts/generation/run_generation_openai_responses.py)
- Command file: [experiments/core_400/gpt_5_1_codex/python/fs/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_openai_responses.py --input_file ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output_file ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_few_shot_python_400_v1.jsonl --model gpt-5.1-codex --max_output_tokens 160 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_few_shot_python_400_v1.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_few_shot_python_400_v1
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/commercial-new/gpt_5_1_codex_P1_few_shot_python_400_v1.jsonl --source ${REPO_ROOT}/prompts/core_400/python/fs/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/commercial-base/may2026/commercial-new/gpt_5_1_codex_P1_few_shot_python_400_v1_code_grounded
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/gpt_5_1_codex/python/fs/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/gpt_5_1_codex/python/fs/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/gpt_5_1_codex/python/fs/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/gpt_5_1_codex/python/fs/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/gpt_5_1_codex/python/fs/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/gpt_5_1_codex/python/fs/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/gpt_5_1_codex/python/fs/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/gpt_5_1_codex/python/fs/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/gpt_5_1_codex/python/fs/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/gpt_5_1_codex/python/fs/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
40f57b52f03066e91b4c35d1d140f73af90100bad33a90e0c2be169d841cda33  experiments/core_400/gpt_5_1_codex/python/fs/generation/raw_generations.jsonl
120fe6dc1f89667a80d5b173e409a5713f263ea9ff23acefd574373b5020116e  experiments/core_400/gpt_5_1_codex/python/fs/assessment/automatic_detailed.jsonl
6f8bbb4388e8f04932f84f6d6e4d652e23fb598c673373b133fe3dc321aae3c3  experiments/core_400/gpt_5_1_codex/python/fs/assessment/automatic_summary.json
47c1094aa8908f3db5669aae5a9658191d88225116eb251954fe8f463734911b  experiments/core_400/gpt_5_1_codex/python/fs/assessment/code_grounded_detailed.jsonl
0c70c5262870b08eebc950950f661bbca75d2c03cb803e728bb21c92158da4e8  experiments/core_400/gpt_5_1_codex/python/fs/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
