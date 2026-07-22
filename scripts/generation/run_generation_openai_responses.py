#!/usr/bin/env python3
"""
run_generation_openai_responses.py

OpenAI Responses API runner for thesis experiments.
Intended for models that are not usable through Batch in the current account,
such as gpt-5.1-codex and gpt-5.1-codex-max.

Features
--------
- Reads the same input JSONL format as the Batch script
- Writes thesis-compatible normalized JSONL output
- Supports resume mode by skipping rows already written
- Persists per-run state for documentation continuity
- Stores generated_documentation for evaluator compatibility
- Captures per-sample latency_seconds
- Supports optional reasoning_effort values where allowed

Expected input JSONL
--------------------
One JSON object per line.

Prompt fields supported:
- prompt
- input_text
- input
- user_prompt
- prompt_text

Sample id fields supported:
- id
- sample_id
- custom_id

Example usage
-------------
Smoke test:
python scripts/run_generation_openai_responses.py \
  --input_file data/processed/prompted_shots/P1_zero_shot_python_10_ZS.jsonl \
  --output_file outputs/raw_generations/gpt_5_1_codex_P1_zero_shot_python_10_smoke_v1.jsonl \
  --model gpt-5.1-codex \
  --max_output_tokens 160

Full run:
python scripts/run_generation_openai_responses.py \
  --input_file data/processed/prompted_shots/P1_zero_shot_python_400_ZS.jsonl \
  --output_file outputs/raw_generations/gpt_5_1_codex_P1_zero_shot_python_400_v1.jsonl \
  --model gpt-5.1-codex \
  --max_output_tokens 160 \
  --checkpoint_every 10

Environment
-----------
Required:
- OPENAI_API_KEY

Optional:
- OPENAI_ORG_ID
- OPENAI_PROJECT_ID
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set

try:
    from openai import OpenAI
except ImportError as exc:
    raise SystemExit(
        "Missing dependency: openai\n"
        "Install with: pip install -U openai"
    ) from exc


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, obj: Dict[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def load_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSONL at {path} line {line_no}: {e}") from e
    return rows


def append_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("a", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def safe_get(d: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    for key in keys:
        if key in d and d[key] is not None:
            return d[key]
    return default


def compact_prompt(text: str) -> str:
    return " ".join(text.split()).strip()


def extract_prompt(row: Dict[str, Any]) -> str:
    prompt = safe_get(
        row,
        ["prompt", "input_text", "input", "user_prompt", "prompt_text"],
        default=None,
    )
    if prompt is None:
        raise ValueError(
            "Could not find prompt text in row. Expected one of: "
            "prompt, input_text, input, user_prompt, prompt_text"
        )
    if not isinstance(prompt, str):
        raise ValueError(f"Prompt must be a string, got {type(prompt).__name__}")
    prompt = compact_prompt(prompt)
    if not prompt:
        raise ValueError("Prompt is empty after compaction")
    return prompt


def extract_sample_id(row: Dict[str, Any], idx: int) -> str:
    raw = safe_get(row, ["id", "sample_id", "custom_id"], default=None)
    if raw is None:
        return f"sample_{idx:06d}"
    return str(raw)


def as_dict(obj: Any) -> Dict[str, Any]:
    if obj is None:
        return {}
    if isinstance(obj, dict):
        return obj
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if hasattr(obj, "to_dict"):
        return obj.to_dict()
    try:
        return dict(obj)
    except Exception:
        return {"value": str(obj)}


def collect_text_from_response_obj(response_obj: Dict[str, Any]) -> str:
    if not response_obj:
        return ""

    output_text = response_obj.get("output_text")
    if isinstance(output_text, str) and output_text.strip():
        return output_text.strip()

    output = response_obj.get("output")
    collected: List[str] = []

    if isinstance(output, list):
        for item in output:
            if not isinstance(item, dict):
                continue
            content = item.get("content")
            if isinstance(content, list):
                for c in content:
                    if not isinstance(c, dict):
                        continue
                    text_val = c.get("text")
                    if isinstance(text_val, str) and text_val.strip():
                        collected.append(text_val.strip())
                    nested_output_text = c.get("output_text")
                    if isinstance(nested_output_text, str) and nested_output_text.strip():
                        collected.append(nested_output_text.strip())

    if collected:
        return "\n".join(collected).strip()

    choices = response_obj.get("choices")
    if isinstance(choices, list):
        parts: List[str] = []
        for choice in choices:
            if not isinstance(choice, dict):
                continue
            message = choice.get("message", {})
            if isinstance(message, dict):
                content = message.get("content")
                if isinstance(content, str) and content.strip():
                    parts.append(content.strip())
        if parts:
            return "\n".join(parts).strip()

    return ""


def build_client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY is not set")

    kwargs: Dict[str, Any] = {"api_key": api_key}

    org_id = os.environ.get("OPENAI_ORG_ID")
    if org_id:
        kwargs["organization"] = org_id

    project_id = os.environ.get("OPENAI_PROJECT_ID")
    if project_id:
        kwargs["project"] = project_id

    return OpenAI(**kwargs)


def build_input_messages(prompt: str) -> List[Dict[str, Any]]:
    return [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": prompt,
                }
            ],
        }
    ]


def build_request_kwargs(
    *,
    model: str,
    prompt: str,
    max_output_tokens: int,
    reasoning_effort: str,
    temperature: Optional[float],
    top_p: Optional[float],
) -> Dict[str, Any]:
    verbosity = "medium" if model == "gpt-5.1-codex" else "low"

    kwargs: Dict[str, Any] = {
        "model": model,
        "input": build_input_messages(prompt),
        "max_output_tokens": max_output_tokens,
        "text": {
            "format": {"type": "text"},
            "verbosity": verbosity,
        },
    }

    if reasoning_effort != "none":
        kwargs["reasoning"] = {"effort": reasoning_effort}

    if temperature is not None:
        kwargs["temperature"] = temperature

    if top_p is not None:
        kwargs["top_p"] = top_p

    return kwargs


def derive_artifact_paths(output_file: Path) -> Dict[str, Path]:
    stem = output_file.stem
    run_dir = Path("outputs") / "responses" / stem
    return {
        "run_dir": run_dir,
        "state": run_dir / "state.json",
        "raw_responses_jsonl": run_dir / "raw_responses.jsonl",
        "normalized_jsonl": output_file,
    }


def load_existing_ids(output_path: Path) -> Set[str]:
    if not output_path.exists():
        return set()

    seen: Set[str] = set()
    with output_path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            custom_id = row.get("custom_id")
            if custom_id is not None:
                seen.add(str(custom_id))
    return seen


@dataclass
class RunContext:
    input_file: Path
    output_file: Path
    model: str
    max_output_tokens: int
    reasoning_effort: str
    temperature: Optional[float]
    top_p: Optional[float]
    checkpoint_every: int
    sleep_seconds: float
    resume: bool

    @property
    def artifacts(self) -> Dict[str, Path]:
        return derive_artifact_paths(self.output_file)


def init_state(ctx: RunContext) -> Dict[str, Any]:
    return {
        "created_at": utc_now_iso(),
        "updated_at": utc_now_iso(),
        "input_file": str(ctx.input_file),
        "output_file": str(ctx.output_file),
        "model": ctx.model,
        "max_output_tokens": ctx.max_output_tokens,
        "reasoning_effort": ctx.reasoning_effort,
        "temperature": ctx.temperature,
        "top_p": ctx.top_p,
        "checkpoint_every": ctx.checkpoint_every,
        "sleep_seconds": ctx.sleep_seconds,
        "resume": ctx.resume,
        "stats": {
            "source_rows": None,
            "attempted_rows": 0,
            "written_rows": 0,
            "success_rows": 0,
            "error_rows": 0,
            "skipped_existing_rows": 0,
        },
    }


def save_state(path: Path, state: Dict[str, Any]) -> None:
    state["updated_at"] = utc_now_iso()
    write_json(path, state)


def load_state_or_init(ctx: RunContext) -> Dict[str, Any]:
    state_path = ctx.artifacts["state"]
    if state_path.exists():
        return read_json(state_path)
    state = init_state(ctx)
    save_state(state_path, state)
    return state


def create_success_row(
    source_row: Dict[str, Any],
    *,
    custom_id: str,
    model_name: str,
    generated_text: str,
    latency_seconds: float,
    raw_response: Dict[str, Any],
) -> Dict[str, Any]:
    out_row = dict(source_row)
    out_row["custom_id"] = custom_id
    out_row["model_name"] = model_name
    out_row["generated_documentation"] = generated_text
    out_row["generated_text"] = generated_text
    out_row["generation"] = generated_text
    out_row["latency_seconds"] = latency_seconds
    out_row["error"] = None
    out_row["request_succeeded"] = True
    out_row["raw_response"] = raw_response
    return out_row


def create_error_row(
    source_row: Dict[str, Any],
    *,
    custom_id: str,
    model_name: str,
    latency_seconds: float,
    error_message: str,
) -> Dict[str, Any]:
    out_row = dict(source_row)
    out_row["custom_id"] = custom_id
    out_row["model_name"] = model_name
    out_row["generated_documentation"] = ""
    out_row["generated_text"] = ""
    out_row["generation"] = ""
    out_row["latency_seconds"] = latency_seconds
    out_row["error"] = error_message
    out_row["request_succeeded"] = False
    return out_row


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run OpenAI Responses API generation for thesis experiments"
    )
    parser.add_argument("--input_file", type=Path, required=True, help="Input prompt JSONL")
    parser.add_argument("--output_file", type=Path, required=True, help="Normalized output JSONL")
    parser.add_argument("--model", type=str, required=True, help="Model id, e.g. gpt-5.1-codex")
    parser.add_argument("--max_output_tokens", type=int, default=160, help="Output token cap")
    parser.add_argument(
        "--reasoning_effort",
        type=str,
        default="none",
        choices=["none", "low", "medium", "high"],
        help="Reasoning effort for supported models",
    )
    parser.add_argument("--temperature", type=float, default=None, help="Optional temperature")
    parser.add_argument("--top_p", type=float, default=None, help="Optional top_p")
    parser.add_argument(
        "--checkpoint_every",
        type=int,
        default=10,
        help="Save state progress every N processed rows",
    )
    parser.add_argument(
        "--sleep_seconds",
        type=float,
        default=0.0,
        help="Optional sleep between requests to throttle usage",
    )
    parser.add_argument(
        "--no_resume",
        action="store_true",
        help="Disable resume behavior and reprocess all rows",
    )
    args = parser.parse_args()

    if not args.input_file.exists():
        raise FileNotFoundError(f"Input file not found: {args.input_file}")

    ctx = RunContext(
        input_file=args.input_file,
        output_file=args.output_file,
        model=args.model,
        max_output_tokens=args.max_output_tokens,
        reasoning_effort=args.reasoning_effort,
        temperature=args.temperature,
        top_p=args.top_p,
        checkpoint_every=args.checkpoint_every,
        sleep_seconds=args.sleep_seconds,
        resume=not args.no_resume,
    )

    client = build_client()
    state = load_state_or_init(ctx)
    artifacts = ctx.artifacts

    source_rows = load_jsonl(ctx.input_file)
    state["stats"]["source_rows"] = len(source_rows)
    save_state(artifacts["state"], state)

    existing_ids: Set[str] = set()
    if ctx.resume:
        existing_ids = load_existing_ids(ctx.output_file)

    skipped_existing = 0
    batch_to_append: List[Dict[str, Any]] = []
    raw_batch_to_append: List[Dict[str, Any]] = []

    for idx, source_row in enumerate(source_rows, start=1):
        custom_id = extract_sample_id(source_row, idx)

        if custom_id in existing_ids:
            skipped_existing += 1
            continue

        prompt = extract_prompt(source_row)

        started = time.perf_counter()
        try:
            response = client.responses.create(
                **build_request_kwargs(
                    model=ctx.model,
                    prompt=prompt,
                    max_output_tokens=ctx.max_output_tokens,
                    reasoning_effort=ctx.reasoning_effort,
                    temperature=ctx.temperature,
                    top_p=ctx.top_p,
                )
            )
            latency = time.perf_counter() - started

            response_dict = as_dict(response)
            generated_text = collect_text_from_response_obj(response_dict)

            out_row = create_success_row(
                source_row,
                custom_id=custom_id,
                model_name=ctx.model,
                generated_text=generated_text,
                latency_seconds=latency,
                raw_response=response_dict,
            )
            raw_record = {
                "custom_id": custom_id,
                "latency_seconds": latency,
                "response": response_dict,
            }

            batch_to_append.append(out_row)
            raw_batch_to_append.append(raw_record)

            state["stats"]["success_rows"] += 1

        except Exception as exc:
            latency = time.perf_counter() - started
            out_row = create_error_row(
                source_row,
                custom_id=custom_id,
                model_name=ctx.model,
                latency_seconds=latency,
                error_message=str(exc),
            )
            raw_record = {
                "custom_id": custom_id,
                "latency_seconds": latency,
                "error": str(exc),
            }

            batch_to_append.append(out_row)
            raw_batch_to_append.append(raw_record)

            state["stats"]["error_rows"] += 1

        state["stats"]["attempted_rows"] += 1

        if len(batch_to_append) >= ctx.checkpoint_every:
            append_jsonl(ctx.output_file, batch_to_append)
            append_jsonl(artifacts["raw_responses_jsonl"], raw_batch_to_append)
            state["stats"]["written_rows"] += len(batch_to_append)
            save_state(artifacts["state"], state)
            print(
                f"[{utc_now_iso()}] processed={state['stats']['attempted_rows']} "
                f"written={state['stats']['written_rows']} "
                f"success={state['stats']['success_rows']} "
                f"errors={state['stats']['error_rows']}"
            )
            batch_to_append.clear()
            raw_batch_to_append.clear()

        if ctx.sleep_seconds > 0:
            time.sleep(ctx.sleep_seconds)

    if batch_to_append:
        append_jsonl(ctx.output_file, batch_to_append)
        append_jsonl(artifacts["raw_responses_jsonl"], raw_batch_to_append)
        state["stats"]["written_rows"] += len(batch_to_append)

    state["stats"]["skipped_existing_rows"] = skipped_existing
    save_state(artifacts["state"], state)

    print(f"Output written to: {ctx.output_file}")
    print(f"Raw responses written to: {artifacts['raw_responses_jsonl']}")
    print(json.dumps(state["stats"], indent=2))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user", file=sys.stderr)
        sys.exit(130)