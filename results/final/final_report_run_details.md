# Final Report Run Details Manifest

This manifest is generated from `outputs/segregated_results/index/segregated_results_index.csv` and only counts files whose copied destination exists.

## Organized Result Folders

- `outputs/segregated_results/open-source-base/`: open-source pretrained/base model runs
- `outputs/segregated_results/open-source-lora/`: open-source LoRA/fine-tuned model runs
- `outputs/segregated_results/commercial-base/`: commercial model runs
- `outputs/segregated_results/shared-aggregate/`: shared tables, plots, human-eval, and mixed-family aggregate files
- `outputs/segregated_results/index/`: file indexes and verification reports

## File Counts

| Category | Files |
|---|---:|
| commercial-base | 554 |
| open-source-base | 792 |
| open-source-lora | 197 |
| shared-aggregate | 106 |
| **Total** | **1649** |

## Core 400-Sample Run Coverage

Each core model should have 9 combinations: 3 languages (`python`, `java`, `javascript`) x 3 prompt settings (`zero_shot`, `one_shot`, `few_shot`).

| Category | Model | Listed combos | Raw present | Metrics present | Correctness present | Complete raw+metrics+correctness |
|---|---|---:|---:|---:|---:|---:|
| commercial-base | deepseek_chat | 9 | 9 | 9 | 9 | 9 |
| commercial-base | gemini_3_flash_preview | 9 | 9 | 9 | 9 | 9 |
| commercial-base | gpt_5_1 | 9 | 9 | 9 | 9 | 9 |
| commercial-base | gpt_5_1_codex | 9 | 9 | 9 | 9 | 9 |
| open-source-base | codegemma_2b | 9 | 9 | 9 | 9 | 9 |
| open-source-base | gemma_2_2b_it | 9 | 9 | 9 | 9 | 9 |
| open-source-base | qwen25_1_5b_instruct | 9 | 9 | 9 | 9 | 9 |
| open-source-base | qwen25_coder_1_5b_instruct | 9 | 9 | 9 | 9 | 9 |
| open-source-lora | codegemma_2b_lora_multilang | 9 | 9 | 9 | 9 | 9 |
| open-source-lora | gemma_2_2b_it_lora_multilang | 9 | 9 | 9 | 9 | 9 |
| open-source-lora | qwen25_1_5b_instruct_lora_multilang | 9 | 9 | 9 | 9 | 9 |
| open-source-lora | qwen25_coder_1_5b_instruct_lora_multilang | 9 | 9 | 9 | 9 | 9 |

## Core 400-Sample Downstream Gaps

No downstream gaps found for core 400-sample runs.

## Preserved Partial Or Legacy Commercial 400-Sample Runs

| Category | Model | Listed combos | Raw present | Metrics present | Correctness present | Complete raw+metrics+correctness |
|---|---|---:|---:|---:|---:|---:|
| commercial-base | deepseek_reasoner | 1 | 1 | 1 | 1 | 1 |
| commercial-base | gpt_5_3_codex | 3 | 3 | 3 | 3 | 3 |
| commercial-base | gpt_5_4 | 3 | 3 | 3 | 3 | 3 |

## Companion Files

- `final_report_run_details.csv`: per-combination file counts and copied destination paths
- `segregated_results_index.csv`: complete file-level source-to-destination index
- `main_400_core_run_presence.csv`: compact core 400-sample presence report
- `main_400_artifact_verification_from_index.csv`: detailed artifact verification from copied destination index
