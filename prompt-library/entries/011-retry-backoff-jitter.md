# 011 — Retries with exponential backoff and jitter

## Technique
Selective retry loop: retry only temporary API errors, cap the attempts, double the wait each time, and add random jitter.

## Use case
Keeping an LLM pipeline alive through short outages (rate limits, server overload, network drops) without hammering the API or retrying requests that can never succeed.

## The prompt (verbatim)
```text
N/A — pipeline-level technique. create_with_retry() in scripts/pipeline.py, SDK built-in retries disabled (max_retries=0) so the loop is visible.
Tested by forcing failures:
1) Wi-Fi off                  -> APIConnectionError (temporary)
2) fake key via $env          -> 401 (permanent)
3) account with zero credits  -> 400 (permanent)
```

## Output sample
```text
1) Attempt 1 failed (APIConnectionError). Retrying in 1s...
   Attempt 2 failed (APIConnectionError). Retrying in 2s...
   ERROR: Could not reach the API. Check your internet connection.
2) ERROR 401: API key rejected. Check ANTHROPIC_API_KEY in .env.        (no retries)
3) ERROR 400: ... 'Your credit balance is too low ...'                   (no retries)
```
Run before jitter was added; with jitter the waits read e.g. 1.4s, 2.7s.

## Why it works (mechanism)
- Only `RateLimitError`, `APIConnectionError` and `InternalServerError` are caught by the loop; permanent errors pass straight through to the typed handlers from entry 010.
- `max_attempts` bounds the total time and number of calls.
- Doubling the wait (1s, 2s, 4s) clears short blips fast while giving an overloaded server progressively more room to recover, with few total calls.
- Jitter (random 0–1s) spreads out clients that failed at the same moment, so they don't all retry in the same instant.

## Failure mode (specific, never generic)
- Retrying permanent errors (400/401/404): every attempt fails identically and burns time.
- No attempt cap: an outage turns into an endless loop.
- Fixed wait with no jitter: 1,000 clients rate-limited together retry together, re-trigger the limit, and fail in lockstep again (thundering herd).
- Stacking retry layers: leaving the SDK's default `max_retries=2` on while adding your own loop of 3 means up to 9 calls per request.

## Evaluation angle
Mercor / Outlier engineering-track question: "how does your pipeline handle transient failures?"
- 5/5: classifies errors (temporary vs permanent), retries only temporary ones, capped attempts, exponential backoff with jitter, aware of the SDK's own built-in retries.
- 2/5: `while True` retry on every exception, or a fixed sleep with no cap.

## Date
2026-10-06

## Model used
claude-haiku-4-5-20251001 set in config (no live call — all tests were forced failures)
