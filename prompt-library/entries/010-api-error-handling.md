# 010 — Typed API error handling

## Technique
Exception handling with SDK-specific error classes, ordered specific → general, plus a startup check for the API key.

## Use case
Keeping an LLM pipeline from crashing on predictable API failures, and telling the operator in one line exactly what to fix.

## The prompt (verbatim)
```text
N/A — pipeline-level technique. Tested with scripts/pipeline.py by forcing three failures:
A) account with zero credits          -> 400
B) $env:ANTHROPIC_API_KEY="sk-fake-key-123" -> 401
C) Wi-Fi turned off                   -> connection error
```

## Output sample
```text
A) ERROR 400: Error code: 400 - {... 'Your credit balance is too low to access the Anthropic API. ...'}
B) ERROR 401: API key rejected. Check ANTHROPIC_API_KEY in .env.
C) ERROR: Could not reach the API. Check your internet connection.
```

## Why it works (mechanism)
Each SDK error class maps to one cause and one fix (`AuthenticationError` 401, `NotFoundError` 404, `RateLimitError` 429, `APIConnectionError`, `APIStatusError` as catch-all). Python uses the first matching `except`, so specific classes go first and the parent `APIStatusError` goes last. The function returns `None` on failure and the caller checks for it, so the script exits cleanly instead of crashing one line later.

## Failure mode (specific, never generic)
- Catch-all `APIStatusError` placed first swallows every specific error, so all failures print the same generic message.
- Returning `None` without the caller checking for `None` crashes on `result['response']`.
- Retrying permanent errors (400 credits, 401 bad key, 404 retired model) loops forever and never succeeds.

## Evaluation angle
"How does your pipeline handle API failures?"
- 5/5: separates permanent errors (400/401/404 — never retry, report and stop) from temporary ones (429/5xx/connection — limited retries with backoff), one actionable message per error type.
- 2/5: no try/except, or one catch-all that prints the raw exception.
Grade of the pre-Day-2 runner: 2/5 — unhandled exceptions; evidence: ~40-line traceback with the cause on the last line; root cause: no try/except and no key check; fix: typed excepts + startup key guard + None check.

## Date
2026-10-06

## Model used
claude-haiku-4-5-20251001 set in config (no live call — all tests were forced failures)
