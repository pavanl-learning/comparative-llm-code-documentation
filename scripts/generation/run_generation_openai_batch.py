#!/usr/bin/env python3
"""
run_generation_openai_batch.py

Cost-optimized OpenAI Batch runner for thesis experiments.

Design goals
------------
- Batch API only
- Tight token controls
- Resumable state tracking
- Stable custom_id mapping
- Normalized JSONL output for evaluator compatibility

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
from typing import Any, Dict, Iterable, List, Optional, Tuple

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


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
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


def write_json(path: Path, obj: Dict[str, Any]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def read_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    ensure_parent(path)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def safe_get(d: Dict[str, Any], keys: List[str], default: Any = None) -> Any:
    for key in keys:
        if key in d and d[key] is not None:
            return d[key]
    return default


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


def derive_artifact_paths(output_file: Path) -> Dict[str, Path]:
    stem = output_file.stem
    batch_dir = Path("outputs") / "batches" / stem
    return {
        "batch_dir": batch_dir,
        "state": batch_dir / "state.json",
        "requests_jsonl": batch_dir / "batch_requests.jsonl",
        "output_jsonl": batch_dir / "batch_output.jsonl",
        "error_jsonl": batch_dir / "batch_errors.jsonl",
        "normalized_jsonl": output_file,
    }


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


def build_responses_body(
    *,
    model: str,
    prompt: str,
    max_output_tokens: int,
    reasoning_effort: Optional[str],
) -> Dict[str, Any]:
    body: Dict[str, Any] = {
        "model": model,
        "input": prompt,
        "max_output_tokens": max_output_tokens,
    }

    if reasoning_effort and reasoning_effort != "none":
        body["reasoning"] = {"effort": reasoning_effort}

    return body


def make_batch_requests(
    source_rows: List[Dict[str, Any]],
    *,
    model: str,
    max_output_tokens: int,
    reasoning_effort: Optional[str],
) -> Tuple[List[Dict[str, Any]], Dict[str, Dict[str, Any]]]:
    requests: List[Dict[str, Any]] = []
    source_map: Dict[str, Dict[str, Any]] = {}

    for idx, row in enumerate(source_rows, start=1):
        custom_id = extract_sample_id(row, idx)
        prompt = extract_prompt(row)

        req = {
            "custom_id": custom_id,
            "method": "POST",
            "url": "/v1/responses",
            "body": build_responses_body(
                model=model,
                prompt=prompt,
                max_output_tokens=max_output_tokens,
                reasoning_effort=reasoning_effort,
            ),
        }

        requests.append(req)
        source_map[custom_id] = row

    return requests, source_map


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


def parse_batch_output_line(line_obj: Dict[str, Any]) -> Tuple[str, str, Optional[str], Dict[str, Any]]:
    custom_id = str(line_obj.get("custom_id", "")).strip()
    error_obj = line_obj.get("error")

    if error_obj:
        return custom_id, "", json.dumps(error_obj, ensure_ascii=False), line_obj

    response = line_obj.get("response", {})
    if not isinstance(response, dict):
        return custom_id, "", "Missing response object", line_obj

    status_code = response.get("status_code")
    body = response.get("body", {})

    if status_code is not None and int(status_code) >= 400:
        return custom_id, "", json.dumps(body, ensure_ascii=False), line_obj

    text = ""
    if isinstance(body, dict):
        text = collect_text_from_response_obj(body)

    return custom_id, text, None, line_obj


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


def upload_batch_input_file(client: OpenAI, requests_jsonl_path: Path) -> Dict[str, Any]:
    with requests_jsonl_path.open("rb") as f:
        file_obj = client.files.create(file=f, purpose="batch")
    return as_dict(file_obj)


def create_batch_job(
    client: OpenAI,
    *,
    input_file_id: str,
    description: str,
    output_retention_days: Optional[int] = None,
) -> Dict[str, Any]:
    kwargs: Dict[str, Any] = {
        "input_file_id": input_file_id,
        "endpoint": "/v1/responses",
        "completion_window": "24h",
        "metadata": {"description": description},
    }

    if output_retention_days is not None:
        seconds = int(output_retention_days) * 24 * 60 * 60
        kwargs["output_expires_after"] = {
            "anchor": "created_at",
            "seconds": seconds,
        }

    batch = client.batches.create(**kwargs)
    return as_dict(batch)


def retrieve_batch_job(client: OpenAI, batch_id: str) -> Dict[str, Any]:
    batch = client.batches.retrieve(batch_id)
    return as_dict(batch)


def download_file_content(client: OpenAI, file_id: str) -> bytes:
    content = client.files.content(file_id)
    data = getattr(content, "content", None)
    if isinstance(data, bytes):
        return data
    text_data = getattr(content, "text", None)
    if isinstance(text_data, str):
        return text_data.encode("utf-8")
    return str(content).encode("utf-8")


@dataclass
class RunContext:
    input_file: Optional[Path]
    output_file: Path
    model: Optional[str]
    max_output_tokens: int
    reasoning_effort: Optional[str]
    poll_interval: int
    output_retention_days: Optional[int]

    @property
    def artifacts(self) -> Dict[str, Path]:
        return derive_artifact_paths(self.output_file)


def init_state(ctx: RunContext) -> Dict[str, Any]:
    return {
        "created_at": utc_now_iso(),
        "updated_at": utc_now_iso(),
        "input_file": str(ctx.input_file) if ctx.input_file else None,
        "output_file": str(ctx.output_file),
        "model": ctx.model,
        "max_output_tokens": ctx.max_output_tokens,
        "reasoning_effort": ctx.reasoning_effort,
        "poll_interval": ctx.poll_interval,
        "output_retention_days": ctx.output_retention_days,
        "openai": {
            "input_file_id": None,
            "batch_id": None,
            "batch_status": None,
            "output_file_id": None,
            "error_file_id": None,
        },
        "stats": {
            "source_rows": None,
            "normalized_rows_written": None,
            "normalized_rows_failed": None,
        },
    }


def save_state(state_path: Path, state: Dict[str, Any]) -> None:
    state["updated_at"] = utc_now_iso()
    write_json(state_path, state)


def load_state_or_init(ctx: RunContext) -> Dict[str, Any]:
    state_path = ctx.artifacts["state"]
    if state_path.exists():
        return read_json(state_path)
    state = init_state(ctx)
    save_state(state_path, state)
    return state


def action_submit(ctx: RunContext) -> None:
    if ctx.input_file is None:
        raise SystemExit("--input_file is required for mode=submit")

    client = build_client()
    state = load_state_or_init(ctx)
    artifacts = ctx.artifacts

    if state["openai"].get("batch_id"):
        print(f"Batch already exists: {state['openai']['batch_id']}")
        print(f"State file: {artifacts['state']}")
        return

    source_rows = read_jsonl(ctx.input_file)
    requests, _source_map = make_batch_requests(
        source_rows,
        model=ctx.model or "",
        max_output_tokens=ctx.max_output_tokens,
        reasoning_effort=ctx.reasoning_effort,
    )

    ensure_parent(artifacts["requests_jsonl"])
    write_jsonl(artifacts["requests_jsonl"], requests)

    uploaded = upload_batch_input_file(client, artifacts["requests_jsonl"])
    input_file_id = uploaded.get("id")
    if not input_file_id:
        raise RuntimeError(f"Upload succeeded but no file id returned: {uploaded}")

    description = f"Thesis batch for {ctx.output_file.stem}"
    batch = create_batch_job(
        client,
        input_file_id=input_file_id,
        description=description,
        output_retention_days=ctx.output_retention_days,
    )

    batch_id = batch.get("id")
    if not batch_id:
        raise RuntimeError(f"Batch creation succeeded but no batch id returned: {batch}")

    state["openai"]["input_file_id"] = input_file_id
    state["openai"]["batch_id"] = batch_id
    state["openai"]["batch_status"] = batch.get("status")
    state["stats"]["source_rows"] = len(source_rows)
    save_state(artifacts["state"], state)

    print(f"Prepared requests: {artifacts['requests_jsonl']}")
    print(f"Uploaded input file id: {input_file_id}")
    print(f"Created batch id: {batch_id}")
    print(f"Initial status: {batch.get('status')}")
    print(f"State saved to: {artifacts['state']}")


def action_status(ctx: RunContext, *, quiet: bool = False) -> Dict[str, Any]:
    client = build_client()
    state = load_state_or_init(ctx)
    artifacts = ctx.artifacts

    batch_id = state["openai"].get("batch_id")
    if not batch_id:
        raise SystemExit(f"No batch_id found in state: {artifacts['state']}")

    batch = retrieve_batch_job(client, batch_id)
    state["openai"]["batch_status"] = batch.get("status")
    state["openai"]["output_file_id"] = batch.get("output_file_id")
    state["openai"]["error_file_id"] = batch.get("error_file_id")
    save_state(artifacts["state"], state)

    if not quiet:
        print(json.dumps(batch, indent=2, ensure_ascii=False))

    return batch


def action_download(ctx: RunContext) -> None:
    client = build_client()
    state = load_state_or_init(ctx)
    artifacts = ctx.artifacts

    batch_id = state["openai"].get("batch_id")
    if not batch_id:
        raise SystemExit(f"No batch_id found in state: {artifacts['state']}")

    batch = action_status(ctx, quiet=True)
    status = batch.get("status")
    output_file_id = batch.get("output_file_id")
    error_file_id = batch.get("error_file_id")

    print(f"Batch status: {status}")

    if output_file_id:
        output_bytes = download_file_content(client, output_file_id)
        ensure_parent(artifacts["output_jsonl"])
        artifacts["output_jsonl"].write_bytes(output_bytes)
        print(f"Downloaded output file to: {artifacts['output_jsonl']}")
    else:
        print("No output_file_id available yet")

    if error_file_id:
        error_bytes = download_file_content(client, error_file_id)
        ensure_parent(artifacts["error_jsonl"])
        artifacts["error_jsonl"].write_bytes(error_bytes)
        print(f"Downloaded error file to: {artifacts['error_jsonl']}")
    else:
        print("No error_file_id available")

    if not artifacts["output_jsonl"].exists():
        print("No batch output JSONL found locally; skipping normalization")
        return

    if ctx.input_file is None:
        input_file_in_state = read_json(artifacts["state"]).get("input_file")
        if not input_file_in_state:
            raise SystemExit("Input file path is missing from state; cannot normalize output")
        source_input_file = Path(input_file_in_state)
    else:
        source_input_file = ctx.input_file

    source_rows = read_jsonl(source_input_file)
    _, source_map = make_batch_requests(
        source_rows,
        model=ctx.model or state.get("model") or "",
        max_output_tokens=ctx.max_output_tokens,
        reasoning_effort=ctx.reasoning_effort,
    )

    normalized_rows: List[Dict[str, Any]] = []
    failed_count = 0

    with artifacts["output_jsonl"].open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            try:
                obj = json.loads(line)
            except json.JSONDecodeError as e:
                failed_count += 1
                normalized_rows.append({
                    "custom_id": f"unparsed_line_{line_no}",
                    "generated_documentation": "",
                    "generated_text": "",
                    "generation": "",
                    "error": f"Invalid JSON in batch output line {line_no}: {e}",
                    "raw_batch_line": line,
                })
                continue

            custom_id, generated_text, error_msg, raw_line = parse_batch_output_line(obj)
            source_row = source_map.get(custom_id)

            if source_row is None:
                failed_count += 1
                normalized_rows.append({
                    "custom_id": custom_id or f"missing_source_line_{line_no}",
                    "generated_documentation": generated_text,
                    "generated_text": generated_text,
                    "generation": generated_text,
                    "error": error_msg or "custom_id not found in source mapping",
                    "raw_batch_line": raw_line,
                })
                continue

            out_row = dict(source_row)
            out_row["custom_id"] = custom_id
            out_row["model_name"] = state.get("model")
            out_row["generated_documentation"] = generated_text
            out_row["generated_text"] = generated_text
            out_row["generation"] = generated_text
            out_row["error"] = error_msg
            out_row["batch_request_succeeded"] = error_msg is None
            out_row["batch_raw_response"] = raw_line

            normalized_rows.append(out_row)

            if error_msg is not None:
                failed_count += 1

    write_jsonl(artifacts["normalized_jsonl"], normalized_rows)

    state["stats"]["normalized_rows_written"] = len(normalized_rows)
    state["stats"]["normalized_rows_failed"] = failed_count
    save_state(artifacts["state"], state)

    print(f"Normalized output written to: {artifacts['normalized_jsonl']}")
    print(f"Rows written: {len(normalized_rows)}")
    print(f"Rows with errors: {failed_count}")


def action_run_all(ctx: RunContext) -> None:
    action_submit(ctx)

    terminal_statuses = {"completed", "failed", "expired", "cancelled"}

    while True:
        batch = action_status(ctx, quiet=True)
        status = batch.get("status")
        counts = batch.get("request_counts") or {}
        completed = counts.get("completed")
        failed = counts.get("failed")
        total = counts.get("total")

        print(
            f"[{utc_now_iso()}] status={status} "
            f"completed={completed} failed={failed} total={total}"
        )

        if status in terminal_statuses:
            break

        time.sleep(ctx.poll_interval)

    action_download(ctx)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run OpenAI Batch generation for thesis experiments"
    )
    parser.add_argument(
        "--mode",
        required=True,
        choices=["submit", "status", "download", "run-all"],
        help="submit: prepare/upload/create batch; status: inspect batch; "
             "download: download files and normalize output; run-all: submit and poll",
    )
    parser.add_argument(
        "--input_file",
        type=Path,
        default=None,
        help="Source experiment JSONL containing prompts",
    )
    parser.add_argument(
        "--output_file",
        type=Path,
        required=True,
        help="Final normalized raw generations JSONL path",
    )
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help="Model id, e.g. gpt-5.1",
    )
    parser.add_argument(
        "--max_output_tokens",
        type=int,
        default=96,
        help="Tight output cap for cost-efficient doc generation",
    )
    parser.add_argument(
        "--reasoning_effort",
        type=str,
        default="none",
        choices=["none", "low", "medium", "high"],
        help="Default kept at none for price/token optimization",
    )
    parser.add_argument(
        "--poll_interval",
        type=int,
        default=60,
        help="Polling interval in seconds for run-all mode",
    )
    parser.add_argument(
        "--output_retention_days",
        type=int,
        default=7,
        help="Retention period for batch output/error files in days (1-30)",
    )

    args = parser.parse_args()

    if args.mode in {"submit", "run-all"}:
        if args.input_file is None:
            parser.error("--input_file is required for submit/run-all")
        if not args.input_file.exists():
            parser.error(f"--input_file does not exist: {args.input_file}")
        if not args.model:
            parser.error("--model is required for submit/run-all")

    if args.output_retention_days is not None:
        if args.output_retention_days < 1 or args.output_retention_days > 30:
            parser.error("--output_retention_days must be between 1 and 30")

    return args


def main() -> None:
    args = parse_args()

    ctx = RunContext(
        input_file=args.input_file,
        output_file=args.output_file,
        model=args.model,
        max_output_tokens=args.max_output_tokens,
        reasoning_effort=args.reasoning_effort,
        poll_interval=args.poll_interval,
        output_retention_days=args.output_retention_days,
    )

    if args.mode == "submit":
        action_submit(ctx)
    elif args.mode == "status":
        action_status(ctx)
    elif args.mode == "download":
        action_download(ctx)
    elif args.mode == "run-all":
        action_run_all(ctx)
    else:
        raise SystemExit(f"Unsupported mode: {args.mode}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user", file=sys.stderr)
        sys.exit(130)