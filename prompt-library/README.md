# Prompt Library

Tested prompts, one technique per entry. Each entry records the exact prompt, a real output, why it works, how it fails, and how to evaluate it.

- Entries live in [`entries/`](entries/) as `NNN-short-name.md`.
- Copy [`entries/000-entry-template.md`](entries/000-entry-template.md) to start a new one.
- Every new entry gets a row in the index below.

All prompts here are personal practice exercises. No client or platform task content.

## Index

| # | Entry | Technique | Use case | Model | Date |
|---|---|---|---|---|---|
| 000 | [Entry template](entries/000-entry-template.md) | — | Template for new entries | — | — |
| 001 | [Zero-shot with output constraints](entries/001-zero-shot-output-constraints.md) | Zero-shot | Structured, predictable explanations | ChatGPT | 2026-05-26 |
| 002 | [Negative constraints](entries/002-negative-constraints.md) | Zero-shot + negative constraints | Tighten focus by exclusion | ChatGPT | 2026-05-27 |
| 003 | [Specificity filters — altitude and angle](entries/003-specificity-altitude-angle.md) | Specificity filters | Same topic, different audiences | ChatGPT | 2026-05-27 |
| 004 | [Fully stacked zero-shot prompt](entries/004-fully-stacked-zero-shot.md) | Constraint stacking | Production-grade audience-specific output | ChatGPT | 2026-05-27 |
| 005 | [Template stress-testing](entries/005-template-stress-test.md) | Stress-testing | Find where a template breaks | ChatGPT | 2026-05-27 |
| 006 | [Deliberate failure analysis](entries/006-failure-analysis-five-types.md) | Failure analysis | Root-cause 5 failure types | ChatGPT, Perplexity | 2026-05-29 |
| 007 | [Failure repair](entries/007-failure-repair.md) | Failure repair | Fix all 5 failure types | ChatGPT | 2026-05-29 |
| 008 | [Few-shot KDP classifier](entries/008-few-shot-kdp-classifier.md) ⚠️ output not recorded | Few-shot classification | Classify blurbs into KDP niches | ChatGPT (planned) | 2026-07 |
| 009 | [Truncation detection via stop_reason](entries/009-stop-reason-truncation.md) | Response inspection (stop_reason) | Catch cut-off outputs in a pipeline | claude-haiku-4-5-20251001 | 2026-10-04 |
| 010 | [Typed API error handling](entries/010-api-error-handling.md) | SDK exception handling | Fail cleanly with one actionable message | claude-haiku-4-5-20251001 | 2026-10-06 |
| 011 | [Retries with backoff and jitter](entries/011-retry-backoff-jitter.md) | Exponential backoff + jitter | Survive transient API failures | claude-haiku-4-5-20251001 | 2026-10-06 |
