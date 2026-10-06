# 009 — Truncation detection via stop_reason

## Technique
Response inspection at the API level: reading `stop_reason` and `usage` instead of only the text.

## Use case
Catching incomplete model outputs before they are saved to a results file or passed to a downstream step in a Python pipeline.

## The prompt (verbatim)
```text
User: What are the three most important habits for staying productive?
```
Run twice through `scripts/day1_inspect.py`: once with `max_tokens=1024`, once with `max_tokens=20`.

## Output sample
```text
[EXPECTED — not run live; API account had no credits on 2026-10-04]

===== max_tokens = 1024 =====
stop_reason : end_turn
tokens      : 21 in / ~210 out
text        : full three-item answer

===== max_tokens = 20 =====
stop_reason : max_tokens
tokens      : 21 in / 20 out
text        : Here are three of the most important habits for staying productive: 1. **Prior
```

## Why it works (mechanism)
`stop_reason` is the API's own report of why generation ended. `end_turn` means the model finished; `max_tokens` means it was cut off by the limit. Checking it turns a silent truncation into a detectable, loggable event. `output_tokens == max_tokens` is a second, independent signal.

## Failure mode (specific, never generic)
A runner that reads only `response.content[0].text` and never checks `stop_reason` saves the 20-token answer ("…1. **Prior") as a complete result. The same runner also breaks once responses contain non-text blocks (e.g. `tool_use`), because block 0 may not be text.

## Evaluation angle
Engineering-track assessments: "how does your pipeline detect incomplete outputs?"
- 5/5: checks `stop_reason` on every call, joins all text blocks, warns/retries/flags on `max_tokens`, sizes `max_tokens` to expected output.
- 2/5: reads `content[0].text` only, no truncation check.
Grade the truncated run: 1/5 — output truncation + silent pipeline failure; evidence: stop_reason=max_tokens, 20/20 tokens, text ends mid-word; root cause: limit too low and runner never inspects stop_reason; fix: size the limit and check stop_reason.

## Date
2026-10-04

## Model used
claude-haiku-4-5-20251001 (planned), max_tokens 1024 vs 20
