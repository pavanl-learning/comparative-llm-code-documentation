#!/usr/bin/env python3
"""
Build zero-shot, one-shot, and few-shot prompt files for code documentation generation.

Inputs used in this stage:
- data/processed/prompted/P1_zero_shot_balanced_15000.jsonl
- data/processed/demo_bank.jsonl

Outputs:
- data/processed/prompted_shots/P1_zero_shot_balanced_15000_ZS.jsonl
- data/processed/prompted_shots/P1_zero_shot_balanced_15000_OS.jsonl
- data/processed/prompted_shots/P1_zero_shot_balanced_15000_FS.jsonl
"""

from __future__ import annotations

import ast
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple


EVAL_INPUT = Path("data/processed/prompted/P1_zero_shot_balanced_15000.jsonl")
DEMO_INPUT = Path("data/processed/demo_bank.jsonl")

OUTPUT_DIR = Path("data/processed/prompted_shots")
ZS_OUTPUT = OUTPUT_DIR / "P1_zero_shot_balanced_15000_ZS.jsonl"
OS_OUTPUT = OUTPUT_DIR / "P1_zero_shot_balanced_15000_OS.jsonl"
FS_OUTPUT = OUTPUT_DIR / "P1_zero_shot_balanced_15000_FS.jsonl"

PROMPT_INSTRUCTION = (
    "Write a very short API-docstring-style description for the following function in plain text. "
    "Use exactly 1 sentence when possible, and never more than 2 short sentences. Start with the function's main purpose. "
    "Mention parameters or return value only if they are clearly inferable from the code and can be stated briefly. "
    "Use only information supported by the code. If details are unclear, keep the description general. "
    "Keep the wording brief, direct, and compact. Do not include markdown, code blocks, examples, headings, lists, "
    "implementation steps, or speculative details."
)

LEADING_DOC_BLOCK_RE = re.compile(r"^\s*/\*\*.*?\*/\s*", re.DOTALL)
LEADING_BLOCK_RE = re.compile(r"^\s*/\*.*?\*/\s*", re.DOTALL)
LEADING_LINE_COMMENTS_RE = re.compile(r"^(?:\s*//[^\n]*\n)+", re.DOTALL)

PYTHON_NAME_RE = re.compile(
    r"^\s*(?:async\s+)?def\s+([A-Za-z_][A-Za-z0-9_]*)\s*\(",
    re.MULTILINE,
)

JS_FUNCTION_RE = re.compile(
    r"^\s*(?:export\s+default\s+|export\s+)?(?:async\s+)?function\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*\(",
    re.MULTILINE,
)

JS_ASSIGNED_FUNCTION_RE = re.compile(
    r"^\s*(?:const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*(?:async\s+)?function\b",
    re.MULTILINE,
)

JS_ARROW_FUNCTION_RE = re.compile(
    r"^\s*(?:const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*(?:async\s+)?(?:\([^)]*\)|[A-Za-z_$][A-Za-z0-9_$]*)\s*=>",
    re.MULTILINE,
)

JS_METHOD_RE = re.compile(
    r"^\s*(?!if\b|for\b|while\b|switch\b|catch\b|function\b)([A-Za-z_$][A-Za-z0-9_$]*)\s*\([^)]*\)\s*\{",
    re.MULTILINE,
)

JAVA_METHOD_RE = re.compile(
    r"""
    ^\s*
    (?:
        public|protected|private
    )?\s*
    (?:
        static|final|synchronized|abstract|native|strictfp
    \s+)*
    (?:<[^>]+>\s+)?
    [A-Za-z_$][A-Za-z0-9_<>\[\].,?\s]*
    \s+
    ([A-Za-z_$][A-Za-z0-9_$]*)
    \s*\(
    """,
    re.MULTILINE | re.VERBOSE,
)

JS_OBJECT_FUNCTION_RE = re.compile(
    r"""^\s*['"]?([A-Za-z_$][A-Za-z0-9_$]*)['"]?\s*:\s*(?:async\s+)?function\b""",
    re.MULTILINE,
)

JS_PROTOTYPE_FUNCTION_RE = re.compile(
    r"""^\s*[A-Za-z_$][A-Za-z0-9_$]*\.prototype\.([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*(?:async\s+)?function\b""",
    re.MULTILINE,
)

JS_PROTOTYPE_ARROW_RE = re.compile(
    r"""^\s*[A-Za-z_$][A-Za-z0-9_$]*\.prototype\.([A-Za-z_$][A-Za-z0-9_$]*)\s*=\s*(?:async\s+)?(?:\([^)]*\)|[A-Za-z_$][A-Za-z0-9_$]*)\s*=>""",
    re.MULTILINE,
)

JAVA_CONTROL_KEYWORDS = {"if", "for", "while", "switch", "catch", "return", "new"}


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON in {path} at line {line_no}: {exc}") from exc
    return rows


def write_jsonl(path: Path, rows: List[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def normalize_reference_text(text: str) -> str:
    return " ".join(str(text).split()).strip()


def normalize_func_name(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def strip_python_docstring(code: str) -> str:
    """
    Remove a leading Python docstring from a standalone function/class snippet.
    First tries AST-based removal; if that misses, falls back to conservative
    removal of the first indented triple-quoted block after the signature.
    """
    try:
        module = ast.parse(code)
    except SyntaxError:
        module = None

    if module and module.body:
        node = module.body[0]
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.body:
            first_stmt = node.body[0]
            is_docstring = (
                isinstance(first_stmt, ast.Expr)
                and isinstance(first_stmt.value, ast.Constant)
                and isinstance(first_stmt.value.value, str)
            )
            if is_docstring:
                lines = code.splitlines()
                start = first_stmt.lineno - 1
                end = first_stmt.end_lineno
                stripped = lines[:start] + lines[end:]
                return "\n".join(stripped)

    lines = code.splitlines()
    if len(lines) < 2:
        return code

    out = [lines[0]]
    i = 1

    while i < len(lines) and lines[i].strip() == "":
        out.append(lines[i])
        i += 1

    if i < len(lines):
        stripped = lines[i].lstrip()
        if stripped.startswith('"""') or stripped.startswith("'''"):
            quote = '"""' if stripped.startswith('"""') else "'''"
            if stripped.count(quote) >= 2:
                i += 1
            else:
                i += 1
                while i < len(lines):
                    if quote in lines[i]:
                        i += 1
                        break
                    i += 1

    out.extend(lines[i:])
    return "\n".join(out)


def strip_leading_doc_comments(code: str) -> str:
    new_code = LEADING_DOC_BLOCK_RE.sub("", code, count=1)
    if new_code != code:
        return new_code

    new_code = LEADING_BLOCK_RE.sub("", code, count=1)
    if new_code != code:
        return new_code

    new_code = LEADING_LINE_COMMENTS_RE.sub("", code, count=1)
    return new_code


def strip_target_documentation(language: str, code: str) -> str:
    lang = language.strip().lower()
    if lang == "python":
        return strip_python_docstring(code)
    if lang in {"java", "javascript"}:
        return strip_leading_doc_comments(code)
    return code


def extract_python_name(code: str) -> str | None:
    match = PYTHON_NAME_RE.search(code)
    return match.group(1) if match else None


def extract_javascript_name(code: str) -> str | None:
    for pattern in (
        JS_FUNCTION_RE,
        JS_ASSIGNED_FUNCTION_RE,
        JS_ARROW_FUNCTION_RE,
        JS_OBJECT_FUNCTION_RE,
        JS_PROTOTYPE_FUNCTION_RE,
        JS_PROTOTYPE_ARROW_RE,
        JS_METHOD_RE,
    ):
        match = pattern.search(code)
        if match:
            name = match.group(1)
            if name not in {"if", "for", "while", "switch", "catch"}:
                return name
    return None


def extract_java_name(code: str) -> str | None:
    match = JAVA_METHOD_RE.search(code)
    if not match:
        return None

    name = match.group(1)
    if name in JAVA_CONTROL_KEYWORDS:
        return None
    return name


def resolve_func_name(language: str, raw_func_name: Any, code: str) -> Tuple[str, str]:
    raw = normalize_func_name(raw_func_name)
    if raw:
        return raw, "dataset"

    lang = language.strip().lower()

    inferred: str | None = None
    if lang == "python":
        inferred = extract_python_name(code)
    elif lang == "javascript":
        inferred = extract_javascript_name(code)
    elif lang == "java":
        inferred = extract_java_name(code)

    if inferred:
        return inferred, "inferred"

    return "", "omitted"


def build_zero_shot_prompt(language: str, func_name: str, code: str) -> str:
    parts = [
        PROMPT_INSTRUCTION,
        "",
        f"Language: {language}",
    ]
    if func_name and func_name.strip():
        parts.append(f"Function name: {func_name}")
    parts.extend([
        f"Code:\n{code}",
        "",
        "Documentation:",
    ])
    return "\n".join(parts)


def build_demo_block(demo_row: Dict[str, Any]) -> str:
    demo_code = strip_target_documentation(demo_row["language"], demo_row["code"])
    resolved_func_name, _ = resolve_func_name(
        demo_row["language"],
        demo_row.get("func_name"),
        demo_code,
    )
    demo_doc = normalize_reference_text(demo_row["reference_documentation"])

    parts = [
        f"Language: {demo_row['language']}",
    ]
    if resolved_func_name:
        parts.append(f"Function name: {resolved_func_name}")

    parts.extend([
        f"Code:\n{demo_code}",
        "",
        f"Documentation:\n{demo_doc}",
    ])
    return "\n".join(parts)


def build_one_shot_prompt(
    language: str,
    func_name: str,
    code: str,
    demo_row: Dict[str, Any],
) -> str:
    demo_block = build_demo_block(demo_row)

    parts = [
        PROMPT_INSTRUCTION,
        "",
        "Example:",
        demo_block,
        "",
        "Now document this function.",
        "",
        f"Language: {language}",
    ]
    if func_name and func_name.strip():
        parts.append(f"Function name: {func_name}")
    parts.extend([
        f"Code:\n{code}",
        "",
        "Documentation:",
    ])
    return "\n".join(parts)


def build_few_shot_prompt(
    language: str,
    func_name: str,
    code: str,
    demo_rows: List[Dict[str, Any]],
) -> str:
    example_parts = []
    for idx, demo_row in enumerate(demo_rows, start=1):
        example_parts.append(f"Example {idx}:\n{build_demo_block(demo_row)}")

    parts = [
        PROMPT_INSTRUCTION,
        "",
        "\n\n".join(example_parts),
        "",
        "Now document this function.",
        "",
        f"Language: {language}",
    ]
    if func_name and func_name.strip():
        parts.append(f"Function name: {func_name}")
    parts.extend([
        f"Code:\n{code}",
        "",
        "Documentation:",
    ])
    return "\n".join(parts)


def group_by_language(rows: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    grouped: Dict[str, List[Dict[str, Any]]] = {}
    for row in rows:
        lang = row["language"].strip().lower()
        grouped.setdefault(lang, []).append(row)
    return grouped


def pick_one_shot_demo(
    sample_row: Dict[str, Any],
    demos_by_language: Dict[str, List[Dict[str, Any]]],
) -> Dict[str, Any]:
    lang = sample_row["language"].strip().lower()

    if lang in demos_by_language and demos_by_language[lang]:
        return demos_by_language[lang][0]

    for demo_list in demos_by_language.values():
        if demo_list:
            return demo_list[0]

    raise ValueError("No demo examples available for one-shot prompt construction.")


def pick_few_shot_demos(
    sample_row: Dict[str, Any],
    demos_by_language: Dict[str, List[Dict[str, Any]]],
) -> List[Dict[str, Any]]:
    lang = sample_row["language"].strip().lower()

    if lang in demos_by_language and len(demos_by_language[lang]) >= 3:
        return demos_by_language[lang][:3]

    fallback: List[Dict[str, Any]] = []
    for demo_list in demos_by_language.values():
        fallback.extend(demo_list)

    if not fallback:
        raise ValueError("No demo examples available for few-shot prompt construction.")

    return fallback[:3]


def validate_required_fields(rows: List[Dict[str, Any]], path: Path) -> None:
    required = {"sample_id", "language", "func_name", "code", "reference_documentation"}
    for i, row in enumerate(rows, start=1):
        missing = required - set(row.keys())
        if missing:
            raise ValueError(
                f"Missing required fields in {path} at row {i}: {sorted(missing)}"
            )


def validate_demo_bank(demo_rows: List[Dict[str, Any]]) -> None:
    demos_by_language = group_by_language(demo_rows)
    for lang in ("python", "java", "javascript"):
        if lang not in demos_by_language:
            raise ValueError(f"Demo bank missing language: {lang}")
        if len(demos_by_language[lang]) == 0:
            raise ValueError(f"Demo bank has no examples for language: {lang}")


def validate_built_rows(rows: List[Dict[str, Any]], prompt_id: str) -> None:
    if not rows:
        raise ValueError(f"{prompt_id} produced no rows.")

    for i, row in enumerate(rows[: min(20, len(rows))], start=1):
        language = row["language"].strip().lower()
        code = row["code"]
        prompt = row["prompt"]

        if not prompt.rstrip().endswith("Documentation:"):
            raise ValueError(f"{prompt_id} row {i} does not end with 'Documentation:'")

        if "Function name:\n" in prompt:
            raise ValueError(f"{prompt_id} row {i} contains a blank function name line")

        if "Function name: \n" in prompt:
            raise ValueError(f"{prompt_id} row {i} contains an empty function name value")

        if row.get("func_name_source") not in {"dataset", "inferred", "omitted"}:
            raise ValueError(f"{prompt_id} row {i} has invalid func_name_source")

        if language == "python":
            lines = code.splitlines()
            for ln in lines[1:]:
                stripped = ln.lstrip()
                if not stripped:
                    continue
                if stripped.startswith('"""') or stripped.startswith("'''"):
                    raise ValueError(f"{prompt_id} row {i} still contains a leading Python docstring")
                break

        if language in {"java", "javascript"}:
            stripped = code.lstrip()
            if stripped.startswith("/**") or stripped.startswith("/*"):
                raise ValueError(
                    f"{prompt_id} row {i} still contains a leading doc comment"
                )

        if "```" in prompt:
            raise ValueError(f"{prompt_id} row {i} unexpectedly contains markdown fences")


def build_zs_rows(eval_rows: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    output_rows: List[Dict[str, Any]] = []

    for row in eval_rows:
        clean_code = strip_target_documentation(row["language"], row["code"])
        resolved_func_name, func_name_source = resolve_func_name(
            row["language"],
            row.get("func_name"),
            clean_code,
        )

        prompt = build_zero_shot_prompt(
            language=row["language"],
            func_name=resolved_func_name,
            code=clean_code,
        )

        output_rows.append({
            "sample_id": row["sample_id"],
            "language": row["language"],
            "func_name": resolved_func_name,
            "raw_func_name": normalize_func_name(row.get("func_name")),
            "resolved_func_name": resolved_func_name,
            "func_name_source": func_name_source,
            "code": clean_code,
            "reference_documentation": row["reference_documentation"],
            "prompt_template_id": "ZS",
            "prompt": prompt,
        })

    return output_rows


def build_os_rows(
    eval_rows: List[Dict[str, Any]],
    demos_by_language: Dict[str, List[Dict[str, Any]]],
) -> List[Dict[str, Any]]:
    output_rows: List[Dict[str, Any]] = []

    for row in eval_rows:
        clean_code = strip_target_documentation(row["language"], row["code"])
        resolved_func_name, func_name_source = resolve_func_name(
            row["language"],
            row.get("func_name"),
            clean_code,
        )
        demo_row = pick_one_shot_demo(row, demos_by_language)

        prompt = build_one_shot_prompt(
            language=row["language"],
            func_name=resolved_func_name,
            code=clean_code,
            demo_row=demo_row,
        )

        output_rows.append({
            "sample_id": row["sample_id"],
            "language": row["language"],
            "func_name": resolved_func_name,
            "raw_func_name": normalize_func_name(row.get("func_name")),
            "resolved_func_name": resolved_func_name,
            "func_name_source": func_name_source,
            "code": clean_code,
            "reference_documentation": row["reference_documentation"],
            "prompt_template_id": "OS",
            "prompt": prompt,
        })

    return output_rows


def build_fs_rows(
    eval_rows: List[Dict[str, Any]],
    demos_by_language: Dict[str, List[Dict[str, Any]]],
) -> List[Dict[str, Any]]:
    output_rows: List[Dict[str, Any]] = []

    for row in eval_rows:
        clean_code = strip_target_documentation(row["language"], row["code"])
        resolved_func_name, func_name_source = resolve_func_name(
            row["language"],
            row.get("func_name"),
            clean_code,
        )
        demo_rows = pick_few_shot_demos(row, demos_by_language)

        prompt = build_few_shot_prompt(
            language=row["language"],
            func_name=resolved_func_name,
            code=clean_code,
            demo_rows=demo_rows,
        )

        output_rows.append({
            "sample_id": row["sample_id"],
            "language": row["language"],
            "func_name": resolved_func_name,
            "raw_func_name": normalize_func_name(row.get("func_name")),
            "resolved_func_name": resolved_func_name,
            "func_name_source": func_name_source,
            "code": clean_code,
            "reference_documentation": row["reference_documentation"],
            "prompt_template_id": "FS",
            "prompt": prompt,
        })

    return output_rows


def main() -> None:
    if not EVAL_INPUT.exists():
        raise FileNotFoundError(f"Evaluation input not found: {EVAL_INPUT}")
    if not DEMO_INPUT.exists():
        raise FileNotFoundError(f"Demo input not found: {DEMO_INPUT}")

    print(f"Using evaluation input: {EVAL_INPUT}")
    print(f"Using demo input: {DEMO_INPUT}")

    eval_rows = read_jsonl(EVAL_INPUT)
    demo_rows = read_jsonl(DEMO_INPUT)

    validate_required_fields(eval_rows, EVAL_INPUT)
    validate_required_fields(demo_rows, DEMO_INPUT)
    validate_demo_bank(demo_rows)

    demos_by_language = group_by_language(demo_rows)

    zs_rows = build_zs_rows(eval_rows)
    os_rows = build_os_rows(eval_rows, demos_by_language)
    fs_rows = build_fs_rows(eval_rows, demos_by_language)

    validate_built_rows(zs_rows, "ZS")
    validate_built_rows(os_rows, "OS")
    validate_built_rows(fs_rows, "FS")

    write_jsonl(ZS_OUTPUT, zs_rows)
    write_jsonl(OS_OUTPUT, os_rows)
    write_jsonl(FS_OUTPUT, fs_rows)

    print(f"Wrote {ZS_OUTPUT} ({len(zs_rows)} rows)")
    print(f"Wrote {OS_OUTPUT} ({len(os_rows)} rows)")
    print(f"Wrote {FS_OUTPUT} ({len(fs_rows)} rows)")


if __name__ == "__main__":
    main()