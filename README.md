# Comparative Evaluation of Open-source and Commercial Large Language Models for Code Documentation

This repository is an evaluator-facing research companion for the MSc dissertation implementation. It preserves the validated full-evidence repository and adds a structured navigation layer for Chapter 4 implementation evidence and Chapter 5 result evidence.

## Research objective

The research compares open-source pre-trained, commercial pre-trained, and open-source LoRA fine-tuned large language models for function-level code documentation across Python, Java, and JavaScript.

## Research questions

The exact thesis research-question wording was not present in the repository artefacts inspected during this build. Insert the final thesis wording here before publication if required.

## Implementation scope

The companion covers dataset preparation, exploratory analysis, prompt construction, model execution, LoRA fine-tuning evidence, automatic evaluation, code-grounded evaluation, human-evaluation artefacts where available, final result assembly, and publication validation.

## Experimental design

- Models: 12
- Languages: Python, Java, JavaScript
- Prompt regimes: zero-shot (ZS), one-shot (OS), few-shot (FS)
- Core conditions: 108
- Rows per condition: 400
- Generated documentation outputs represented by full evidence: 43,200

## Models evaluated

- Gemma-2-2b-it
- Qwen2.5-1.5B-Instruct
- Codegemma-2b
- Qwen2.5-Coder-1.5B-Instruct
- Deepseek-chat-v3.2
- Gemini-3-Flash
- Gpt-5.1
- Gpt-5.1-Codex
- Gemma-2-2b-it_LoRA
- Qwen2.5-1.5B-Instruct_LoRA
- Codegemma-2b_LoRA
- Qwen2.5-Coder-1.5B-Instruct_LoRA

## Programming languages

- Python
- Java
- JavaScript

## Prompt regimes

- ZS: zero-shot instruction
- OS: one-shot instruction with a demonstration
- FS: few-shot instruction with demonstrations

## Evaluation framework

The repository preserves automatic metrics, code-grounded coverage and hallucination checks, row-count validation, sample-ID alignment, checksums, final result tables, and publication-gate reports.

## Implementation workflow diagram

Start with the editable Mermaid workflow: [workflow/research_implementation_workflow.mmd](workflow/research_implementation_workflow.mmd). Renderer availability is documented in [workflow/DIAGRAM_SOURCES.md](workflow/DIAGRAM_SOURCES.md).

## Repository navigation

- [EVALUATOR_START_HERE.md](EVALUATOR_START_HERE.md)
- [RESEARCH_IMPLEMENTATION_INDEX.md](RESEARCH_IMPLEMENTATION_INDEX.md)
- [CHAPTER4_IMPLEMENTATION_MAP.md](CHAPTER4_IMPLEMENTATION_MAP.md)
- [CHAPTER5_RESULTS_MAP.md](CHAPTER5_RESULTS_MAP.md)
- [RUN_INDEX.md](RUN_INDEX.md)
- [validation/research_companion_publication_gate.md](validation/research_companion_publication_gate.md)

## Chapter 4 implementation companion

The Chapter 4 companion is organised under [companion/](companion/) by implementation stage. Each stage README links to actual scripts, inputs, outputs, commands, representative evidence previews, and full evidence paths.

## Chapter 5 results companion

The Chapter 5 companion is under [companion/13_chapter5_results/](companion/13_chapter5_results/) and links to final corrected tables, figures, LoRA deltas, cross-language/prompt evidence, and validation reports.

## 108-condition evidence

The complete run evidence remains in [experiments/core_400/](experiments/core_400/). The navigable indexes are:

- [experiments/BY_MODEL.md](experiments/BY_MODEL.md)
- [experiments/BY_LANGUAGE.md](experiments/BY_LANGUAGE.md)
- [experiments/BY_PROMPT_REGIME.md](experiments/BY_PROMPT_REGIME.md)
- [experiments/CONDITION_MATRIX.md](experiments/CONDITION_MATRIX.md)

## Reproducibility quick start

1. Review [requirements_finetune.txt](requirements_finetune.txt) and implementation scripts under [scripts/](scripts/).
2. Inspect [COMMAND_CATALOGUE.md](COMMAND_CATALOGUE.md) for repository commands and per-condition command files.
3. Use provider credentials through environment variables only; credentials are not stored in this repository.
4. Verify retained evidence using [validation/research_companion_publication_gate.md](validation/research_companion_publication_gate.md).

## Repository statistics

- Total files: 2073
- Total size MB: 170.583
- Core run manifests: 108
- Final gate: PASS

## Publication exclusions

Downloaded model weights, Hugging Face caches, virtual environments, package caches, credentials, private evaluator details, and unapproved checkpoints are excluded or represented by checksum manifests.

## Limitations

Commercial-model reproduction requires valid provider access. Some diagrams are published as Mermaid source only when a local renderer is unavailable. Human-evaluation content is limited to supported repository evidence.

## Licence and third-party model notes

Check third-party model, dataset, and API-provider licence terms before public release or redistribution of derived artefacts.

## Citation guidance

See [CITATION.md](CITATION.md).
