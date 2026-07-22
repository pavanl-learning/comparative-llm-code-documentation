#!/usr/bin/env python3
import argparse
import json
import os
import time
from pathlib import Path
from typing import Any

from openai import OpenAI


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at {path}:{line_no}: {exc}") from exc
    return rows


def load_existing_sample_ids(path: Path) -> set[str]:
    sample_ids: set[str] = set()
    if not path.exists():
        return sample_ids

    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON at existing output {path}:{line_no}: {exc}") from exc
            sample_id = row.get("sample_id")
            if sample_id:
                sample_ids.add(str(sample_id))
    return sample_ids


def clean_generated_text(text: str) -> str:
    text = (text or "").strip()

    prefixes = [
        "Documentation:",
        "Description:",
        "Docstring:",
        "Answer:",
        "Output:",
    ]
    for prefix in prefixes:
        if text.startswith(prefix):
            text = text[len(prefix):].strip()

    text = text.replace("```", " ")
    text = " ".join(text.split())

    bad_prefixes = (
        "def ",
        "class ",
        "return ",
        "if ",
        "for ",
        "while ",
        "try:",
        "except ",
        "with ",
        "function ",
        "const ",
        "let ",
        "var ",
        "public ",
        "private ",
        "protected ",
        "@param",
        "@returns",
        "@return",
    )

    if text.startswith(bad_prefixes):
        parts = text.split(". ")
        kept = []
        for part in parts:
            s = part.strip()
            if s.startswith(bad_prefixes):
                continue
            kept.append(part)
        text = ". ".join(kept).strip()

    sentences = []
    current = ""
    for ch in text:
        current += ch
        if ch in ".!?":
            sentences.append(current.strip())
            current = ""
            if len(sentences) == 2:
                break

    if sentences:
        text = " ".join(sentences).strip()
    else:
        words = text.split()
        text = " ".join(words[:30]).strip()

    return text


def build_prompt(row: dict[str, Any]) -> str:
    prompt = row.get("prompt")
    if prompt and str(prompt).strip():
        return str(prompt)

    parts = []
    if row.get("language"):
        parts.append(f"Language: {row['language']}")

    func_name = str(row.get("func_name", "") or "").strip()
    if func_name:
        parts.append(f"Function name: {func_name}")

    code = row.get("code", "")
    parts.append(f"Code:\n{code}")
    parts.append("")
    parts.append("Documentation:")
    return "\n".join(parts)


def extract_response_text(response: Any) -> str:
    try:
        msg = response.choices[0].message

        content = getattr(msg, "content", None)

        # Case 1: plain string content
        if isinstance(content, str) and content.strip():
            return content.strip()

        # Case 2: list/structured content blocks
        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict):
                    text = item.get("text") or item.get("content")
                    if text:
                        parts.append(str(text))
                else:
                    text = getattr(item, "text", None) or getattr(item, "content", None)
                    if text:
                        parts.append(str(text))
            if parts:
                return " ".join(parts).strip()

        # Case 3: reasoning models may expose a separate field
        reasoning = getattr(msg, "reasoning_content", None)
        if isinstance(reasoning, str) and reasoning.strip():
            return reasoning.strip()

        return ""
    except Exception:
        return ""


def is_rate_limit_error(exc: Exception) -> bool:
    msg = str(exc)
    msg_lower = msg.lower()
    return (
        "429" in msg
        or "resource_exhausted" in msg_lower
        or "rate limit" in msg_lower
        or "quota" in msg_lower
        or "too many requests" in msg_lower
    )


def call_deepseek_with_retry(
    client: OpenAI,
    model_name: str,
    prompt: str,
    retry_sleep_seconds: float,
    backoff_multiplier: float,
    max_retry_sleep_seconds: float,
    max_retries: int,
    temperature: float,
    max_tokens: int,
) -> tuple[Any, float]:
    attempt = 0
    sleep_seconds = retry_sleep_seconds

    while True:
        start = time.time()
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[
                    {"role": "user", "content": prompt},
                ],
                stream=False,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            latency = time.time() - start
            return response, latency
        except Exception as e:
            if not is_rate_limit_error(e):
                raise

            attempt += 1
            if attempt > max_retries:
                raise RuntimeError(
                    f"Exceeded max retries ({max_retries}) due to rate limiting/quota exhaustion. "
                    f"Last error: {e}"
                ) from e

            print(
                f"Rate limit hit (attempt {attempt}/{max_retries}), "
                f"sleeping {sleep_seconds:.0f}s before retry..."
            )
            time.sleep(sleep_seconds)
            sleep_seconds = min(sleep_seconds * backoff_multiplier, max_retry_sleep_seconds)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input JSONL file")
    parser.add_argument("--output", required=True, help="Output JSONL file")
    parser.add_argument("--model", default="deepseek-chat", help="DeepSeek model name")
    parser.add_argument("--limit", type=int, default=None, help="Optional number of rows to process")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite output if it exists")
    parser.add_argument(
        "--start-from-existing-output",
        action="store_true",
        help="Resume by skipping sample_ids already present in the output file",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=1.0,
        help="Delay after each successful request",
    )
    parser.add_argument(
        "--retry-sleep-seconds",
        type=float,
        default=20.0,
        help="Initial delay before retry when a 429/rate-limit error occurs",
    )
    parser.add_argument(
        "--backoff-multiplier",
        type=float,
        default=2.0,
        help="Multiplier applied to retry sleep after each consecutive 429",
    )
    parser.add_argument(
        "--max-retry-sleep-seconds",
        type=float,
        default=180.0,
        help="Maximum retry sleep cap in seconds",
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=5,
        help="Maximum consecutive rate-limit retries before exiting",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=0.2,
        help="Sampling temperature",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=96,
        help="Maximum output tokens for each completion",
    )
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if output_path.exists() and args.overwrite and args.start_from_existing_output:
        raise ValueError("Use either --overwrite or --start-from-existing-output, not both.")

    if output_path.exists() and not args.overwrite and not args.start_from_existing_output:
        raise FileExistsError(
            f"Output file already exists: {output_path}. "
            f"Use --overwrite or --start-from-existing-output."
        )

    if "DEEPSEEK_API_KEY" not in os.environ:
        raise EnvironmentError("DEEPSEEK_API_KEY is not set in the environment.")

    rows = load_jsonl(input_path)
    if args.limit is not None:
        rows = rows[:args.limit]

    if not rows:
        raise ValueError(f"No rows found in input: {input_path}")

    completed_ids: set[str] = set()
    if args.start_from_existing_output and output_path.exists():
        completed_ids = load_existing_sample_ids(output_path)
        print(f"Found {len(completed_ids)} completed sample_ids in existing output.")

    pending_rows = [row for row in rows if str(row["sample_id"]) not in completed_ids]

    if not pending_rows:
        print("No pending rows to process. Output is already complete for the selected input/limit.")
        return

    output_path.parent.mkdir(parents=True, exist_ok=True)

    write_mode = "w"
    if args.start_from_existing_output and output_path.exists():
        write_mode = "a"

    client = OpenAI(
        api_key=os.environ["DEEPSEEK_API_KEY"],
        base_url="https://api.deepseek.com",
    )

    total_pending = len(pending_rows)
    print(f"Processing {total_pending} pending rows out of {len(rows)} total rows.")

    with output_path.open(write_mode, encoding="utf-8") as f:
        for idx, row in enumerate(pending_rows, start=1):
            prompt = build_prompt(row)

            response, latency = call_deepseek_with_retry(
                client=client,
                model_name=args.model,
                prompt=prompt,
                retry_sleep_seconds=args.retry_sleep_seconds,
                backoff_multiplier=args.backoff_multiplier,
                max_retry_sleep_seconds=args.max_retry_sleep_seconds,
                max_retries=args.max_retries,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
            )

            raw_text = extract_response_text(response)
            generated_text = clean_generated_text(raw_text)

            out = {
                "sample_id": row["sample_id"],
                "language": row["language"],
                "func_name": row.get("func_name", ""),
                "prompt_template_id": row.get("prompt_template_id", ""),
                "model_name": args.model,
                "reference_documentation": row.get("reference_documentation", ""),
                "generated_documentation": generated_text,
                "latency_seconds": round(latency, 4),
            }

            if "resolved_func_name" in row:
                out["resolved_func_name"] = row.get("resolved_func_name", "")
            if "func_name_source" in row:
                out["func_name_source"] = row.get("func_name_source", "")

            f.write(json.dumps(out, ensure_ascii=False) + "\n")
            f.flush()

            print(
                f"[{idx}/{total_pending}] {row['sample_id']} done in {latency:.2f}s "
                f"(completed overall: {len(completed_ids) + idx}/{len(rows)})"
            )

            if idx < total_pending:
                time.sleep(args.sleep_seconds)

    print(f"Wrote/updated {output_path}")


if __name__ == "__main__":
    main()