# Qwen2.5 Coder 1.5B Instruct — javascript — OS

## Run identity

| Field | Value |
|---|---|
| Condition ID | `qwen2_5_coder_1_5b_instruct__javascript__os` |
| Full model display name | Qwen2.5 Coder 1.5B Instruct |
| Raw model identifier | `Qwen/Qwen2.5-Coder-1.5B-Instruct` |
| Model group | open-source |
| Model category | open_source_base |
| Language | javascript |
| Prompt regime | OS |
| Validation status | PASS |

## Row-count validation

| Artefact | Expected | Observed |
|---|---:|---:|
| Raw generations | 400 | 400 |
| Automatic detailed evaluation | 400 | 400 |
| Code-grounded detailed evaluation | 400 | 400 |

Sample-ID alignment: `True`.

## Inputs and execution

- Prompt input file: [prompts/core_400/javascript/os/prompt_input_400.jsonl](../../../../../prompts/core_400/javascript/os/prompt_input_400.jsonl)
- Generation script: [scripts/generation/run_generation_hf.py](../../../../../scripts/generation/run_generation_hf.py)
- Command file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/command.txt](command.txt)
- Command provenance label: `reconstructed_from_manifest`
- Decoding settings: documented in the linked command file and script where available; unsupported values are not restated here.

```text
python scripts/generation/run_generation_hf.py --model Qwen/Qwen2.5-Coder-1.5B-Instruct --input ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output ${OUTPUT_ROOT}/outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired.jsonl --max-new-tokens 120 --overwrite
python scripts/evaluation/evaluate_generations.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/may2026/open-source/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired
python scripts/evaluation/evaluate_code_grounded_correctness.py --input ${OUTPUT_ROOT}/outputs/raw_generations/open-source/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired.jsonl --source ${REPO_ROOT}/prompts/core_400/javascript/os/prompt_input_400.jsonl --output-prefix ${OUTPUT_ROOT}/outputs/segregated_results/open-source-base/correctness/qwen25_coder_1_5b_instruct_P1_one_shot_javascript_400_v3_repaired_correctness
```

## Evidence artefacts

- Raw generation file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/generation/raw_generations.jsonl](generation/raw_generations.jsonl)
- Automatic detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/automatic_detailed.jsonl](assessment/automatic_detailed.jsonl)
- Automatic summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/automatic_summary.json](assessment/automatic_summary.json)
- Code-grounded detailed file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/code_grounded_detailed.jsonl](assessment/code_grounded_detailed.jsonl)
- Code-grounded summary file: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/code_grounded_summary.json](assessment/code_grounded_summary.json)
- Run manifest: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/run_manifest.json](run_manifest.json)
- Row-count validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/validation/row_count_validation.json](validation/row_count_validation.json)
- Sample-ID validation: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/validation/sample_id_validation.json](validation/sample_id_validation.json)
- Checksums: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/validation/checksums.sha256](validation/checksums.sha256)
- Final-result traceability report: [validation/final_result_traceability.csv](../../../../../validation/final_result_traceability.csv)
- Final result table: [results/final/clean_full_results.csv](../../../../../results/final/clean_full_results.csv)
- Representative sample records: [experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/examples/sample_records.md](examples/sample_records.md)

## SHA-256 checksums

```text
d6a0c3ab009901d6f81899c40c73959ea7972fafdf53e1c2fc885837dc90e561  experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/generation/raw_generations.jsonl
752daa52b533ca7a8fe44b6501cacc86a188c5ceef37374473b325f30b0e8cff  experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/automatic_detailed.jsonl
9cade998abc0f7ab0dfa40783db3e16dc96ea0e3e4e7057aad7d1c5c2f6bd62e  experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/automatic_summary.json
bae8979c01b0c8e29b96d5b970e241f49272447d51e77d6f69f391770c4d08cf  experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/code_grounded_detailed.jsonl
b0d83c79512de814c6abd51ff6c9d4394b99fbca35bdac09fb8b3d4406170ebb  experiments/core_400/qwen2_5_coder_1_5b_instruct/javascript/os/assessment/code_grounded_summary.json
```

## Known caveats

Provider credentials, downloaded model weights, and private caches are intentionally excluded. Commercial-model re-execution requires valid provider access.
