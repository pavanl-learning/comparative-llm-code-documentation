#!/usr/bin/env python3

import argparse
import ast
import json
import re
import statistics
from collections import defaultdict
from pathlib import Path


EXPLICIT_PARAM_PATTERNS = [
    r"\bparam(?:eter)?\s+([A-Za-z_][A-Za-z0-9_]*)\b",
    r"\bargument\s+([A-Za-z_][A-Za-z0-9_]*)\b",
]


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def safe_text(x):
    if x is None:
        return ""
    return " ".join(str(x).split()).strip()


def text_contains_token(text: str, token: str) -> bool:
    return re.search(rf"\b{re.escape(token)}\b", text, re.IGNORECASE) is not None


def detect_return_mention(text: str) -> bool:
    patterns = [
        r"\breturn\b",
        r"\breturns\b",
        r"\breturned\b",
    ]
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def extract_exception_mentions(text: str):
    matches = set()
    for m in re.finditer(r"\b([A-Z][A-Za-z0-9_]*(Error|Exception))\b", text):
        matches.add(m.group(1))
    return matches


def extract_explicit_parameter_mentions(text: str):
    mentions = set()
    for pattern in EXPLICIT_PARAM_PATTERNS:
        for m in re.finditer(pattern, text, re.IGNORECASE):
            mentions.add(m.group(1))
    return mentions


def extract_python_code_facts(code: str):
    facts = {
        "parameters": [],
        "has_return_value": False,
        "exceptions": [],
        "parse_failed": False,
    }

    try:
        tree = ast.parse(code)
    except SyntaxError:
        facts["parse_failed"] = True
        return facts

    func_node = None
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            func_node = node
            break

    if func_node is None:
        facts["parse_failed"] = True
        return facts

    params = []
    for arg in func_node.args.args:
        if arg.arg not in {"self", "cls"}:
            params.append(arg.arg)

    if func_node.args.vararg and func_node.args.vararg.arg not in {"self", "cls"}:
        params.append(func_node.args.vararg.arg)

    for arg in func_node.args.kwonlyargs:
        if arg.arg not in {"self", "cls"}:
            params.append(arg.arg)

    if func_node.args.kwarg and func_node.args.kwarg.arg not in {"self", "cls"}:
        params.append(func_node.args.kwarg.arg)

    exceptions = []
    has_return_value = False

    for node in ast.walk(func_node):
        if isinstance(node, ast.Return):
            if node.value is not None:
                if not (isinstance(node.value, ast.Constant) and node.value.value is None):
                    has_return_value = True

        if isinstance(node, ast.Raise) and node.exc is not None:
            exc_name = None
            if isinstance(node.exc, ast.Call):
                if isinstance(node.exc.func, ast.Name):
                    exc_name = node.exc.func.id
                elif isinstance(node.exc.func, ast.Attribute):
                    exc_name = node.exc.func.attr
            elif isinstance(node.exc, ast.Name):
                exc_name = node.exc.id

            if exc_name:
                exceptions.append(exc_name)

    facts["parameters"] = sorted(set(params))
    facts["has_return_value"] = has_return_value
    facts["exceptions"] = sorted(set(exceptions))
    return facts


def extract_generic_code_facts(code: str):
    facts = {
        "parameters": [],
        "has_return_value": False,
        "exceptions": [],
        "parse_failed": False,
    }

    if not code.strip():
        facts["parse_failed"] = True
        return facts

    m = re.search(r"\((.*?)\)", code, re.DOTALL)
    if m:
        raw = m.group(1).strip()
        if raw:
            params = []
            for p in raw.split(","):
                p = p.strip()
                if not p:
                    continue
                token = re.split(r"\s+|=|:", p.strip())[-1]
                token = re.sub(r"[^A-Za-z0-9_]", "", token)
                if token and token not in {"self", "cls"}:
                    params.append(token)
            facts["parameters"] = sorted(set(params))

    if re.search(r"\breturn\b\s+[^;}\n]+", code):
        facts["has_return_value"] = True

    exceptions = set()
    patterns = [
        r"\braise\s+([A-Za-z_][A-Za-z0-9_]*)",
        r"\bthrow\s+new\s+([A-Za-z_][A-Za-z0-9_]*)",
        r"\bthrows\s+([A-Za-z_][A-Za-z0-9_]*)",
    ]
    for pat in patterns:
        for m in re.finditer(pat, code):
            exceptions.add(m.group(1))

    facts["exceptions"] = sorted(exceptions)
    return facts


def extract_code_facts(language: str, code: str):
    language = (language or "").lower()
    if language == "python":
        return extract_python_code_facts(code)
    return extract_generic_code_facts(code)


def compute_code_grounded_metrics(language: str, code: str, prediction: str):
    facts = extract_code_facts(language, code)
    pred = safe_text(prediction)

    expected_params = facts["parameters"]
    expected_excs = facts["exceptions"]
    expected_return = facts["has_return_value"]

    mentioned_params = [p for p in expected_params if text_contains_token(pred, p)]
    mentioned_return = detect_return_mention(pred) if expected_return else False
    mentioned_excs = [e for e in expected_excs if text_contains_token(pred, e)]

    total_expected = len(expected_params) + int(expected_return) + len(expected_excs)
    total_mentioned = len(mentioned_params) + int(mentioned_return) + len(mentioned_excs)
    total_missing = total_expected - total_mentioned if total_expected > 0 else None

    omission_rate = (total_missing / total_expected) if total_expected > 0 else None

    pred_excs = extract_exception_mentions(pred)
    hallucinated_excs = sorted(pred_excs - set(expected_excs))

    explicit_param_mentions = extract_explicit_parameter_mentions(pred)
    hallucinated_params = sorted(x for x in explicit_param_mentions if x not in expected_params)

    hallucinated_return = 1 if (detect_return_mention(pred) and not expected_return and total_expected > 0) else 0

    hallucination_count = len(hallucinated_params) + len(hallucinated_excs) + hallucinated_return
    hallucination_flag = 1 if hallucination_count > 0 else 0

    return {
        "code_available": bool(code.strip()),
        "code_parse_failed": facts["parse_failed"],

        "expected_parameter_count": len(expected_params),
        "mentioned_parameter_count": len(mentioned_params),
        "parameter_coverage": (len(mentioned_params) / len(expected_params)) if expected_params else None,

        "expected_return": int(expected_return),
        "mentioned_return": int(mentioned_return),
        "return_coverage": float(mentioned_return) if expected_return else None,

        "expected_exception_count": len(expected_excs),
        "mentioned_exception_count": len(mentioned_excs),
        "exception_coverage": (len(mentioned_excs) / len(expected_excs)) if expected_excs else None,

        "total_expected_elements": total_expected,
        "total_missing_elements": total_missing,
        "omission_rate": omission_rate,

        "hallucinated_parameters": hallucinated_params,
        "hallucinated_exceptions": hallucinated_excs,
        "hallucinated_return": hallucinated_return,
        "hallucination_count": hallucination_count,
        "hallucination_flag": hallucination_flag,
    }


def mean_or_none(values):
    values = [v for v in values if v is not None]
    return statistics.mean(values) if values else None


def summarize_rows(rows):
    return {
        "num_samples": len(rows),
        "samples_with_code": sum(1 for r in rows if r["code_available"]),
        "samples_with_parse_failures": sum(1 for r in rows if r["code_parse_failed"]),
        "samples_with_expected_parameters": sum(1 for r in rows if r["expected_parameter_count"] > 0),
        "samples_with_expected_return": sum(r["expected_return"] for r in rows),
        "samples_with_expected_exceptions": sum(1 for r in rows if r["expected_exception_count"] > 0),

        "mean_parameter_coverage": mean_or_none([r["parameter_coverage"] for r in rows]),
        "mean_return_coverage": mean_or_none([r["return_coverage"] for r in rows]),
        "mean_exception_coverage": mean_or_none([r["exception_coverage"] for r in rows]),
        "mean_omission_rate": mean_or_none([r["omission_rate"] for r in rows]),
        "hallucination_sample_rate": statistics.mean(r["hallucination_flag"] for r in rows) if rows else None,
        "mean_hallucination_count": statistics.mean(r["hallucination_count"] for r in rows) if rows else None,
    }


def parse_args():
    parser = argparse.ArgumentParser(description="Evaluate code-grounded correctness of generated documentation.")
    parser.add_argument("--input", required=True, help="Input generations JSONL")
    parser.add_argument("--source", required=True, help="Source prompted JSONL containing code")
    parser.add_argument("--output-prefix", required=True, help="Prefix for detailed and summary outputs")
    return parser.parse_args()


def main():
    args = parse_args()

    input_file = Path(args.input)
    source_file = Path(args.source)
    output_prefix = Path(args.output_prefix)

    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
    if not source_file.exists():
        raise FileNotFoundError(f"Source file not found: {source_file}")

    detailed_out = Path(str(output_prefix) + "_detailed.jsonl")
    summary_out = Path(str(output_prefix) + "_summary.json")

    detailed_out.parent.mkdir(parents=True, exist_ok=True)
    summary_out.parent.mkdir(parents=True, exist_ok=True)

    gen_rows = load_jsonl(input_file)
    source_rows = load_jsonl(source_file)

    if not gen_rows:
        raise ValueError(f"No rows found in {input_file}")
    if not source_rows:
        raise ValueError(f"No rows found in {source_file}")

    source_by_id = {str(r["sample_id"]): r for r in source_rows}

    detailed_rows = []

    for row in gen_rows:
        sample_id = str(row["sample_id"])
        source_row = source_by_id.get(sample_id, {})

        language = row.get("language", source_row.get("language", ""))
        code = source_row.get("code", "")
        pred = safe_text(row.get("generated_documentation", ""))

        metrics = compute_code_grounded_metrics(language, code, pred)

        out_row = {
            "sample_id": sample_id,
            "language": language,
            "model_name": row["model_name"],
            "prompt_template_id": row["prompt_template_id"],
            "generated_documentation": pred,
            "source_found": bool(source_row),
            **metrics,
        }

        detailed_rows.append(out_row)

    overall_summary = summarize_rows(detailed_rows)

    grouped = defaultdict(list)
    for row in detailed_rows:
        grouped[row["language"]].append(row)

    per_language = {
        lang: summarize_rows(lang_rows)
        for lang, lang_rows in sorted(grouped.items())
    }

    summary = {
        "input_file": str(input_file),
        "source_file": str(source_file),
        "num_samples": len(detailed_rows),
        "model_name": detailed_rows[0]["model_name"],
        "prompt_template_id": detailed_rows[0]["prompt_template_id"],
        **overall_summary,
        "per_language": per_language,
    }

    with detailed_out.open("w", encoding="utf-8") as f:
        for row in detailed_rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")

    with summary_out.open("w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    print(f"Wrote {detailed_out}")
    print(f"Wrote {summary_out}")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()