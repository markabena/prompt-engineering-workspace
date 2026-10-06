# 007 — Failure repair — all 5 types fixed

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Zero-shot failure repair using constraint layering and Template 02

## Use case
Rebuilding broken prompts so each failure type is closed.

## The prompt (verbatim)
```text
The 5 prompts from Entry 006 rewritten with Template 02: format + audience slots added (ambiguity), contradiction removed (constraint conflicts), single matched audience (audience mismatch), bullet count + focus filter (scope overflow).
```

## Output sample
```text
Human evaluators compare and rank multiple model responses, creating preference data that reflects which outputs are more useful and aligned with desired behavior.
[RLHF fix, one bullet]
```

## Why it works (mechanism)
Applying format, audience, altitude, angle, and exclusion constraints together closes every gap type that causes zero-shot failures. "Do not introduce or define the topic" removed definition openers in the RLHF and MCP fixes.

## Failure mode (specific, never generic)
Junior audience + complex technical topic still produces altitude creep (API fix used "reduces coupling", "standardized access layer"). Add "avoid advanced architectural terminology" as a default exclusion for junior-audience prompts.

## Evaluation angle
A repaired prompt shows you know not just what failed but why — the diagnose-to-fix loop is the core evaluator skill on Outlier and Mercor. Week 1 mock assessment exposed the written-evaluation depth gap, which produced the 5-element evaluation standard.

## Date
2026-05-29

## Model used
ChatGPT (web; exact model not recorded)
