# 005 — Template stress-testing

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Zero-shot template stress-testing

## Use case
Identifying where a reusable prompt template breaks across different topic types.

## The prompt (verbatim)
```text
Template 01 run three times:
1) Reinforcement learning — 4 bullets, 2 sentences, business executive, executive altitude, investment risk/opportunity only; no jargon, no how-it-works, no academic language
2) How to fine-tune an LLM — 5 bullets, 2 sentences, junior developer, implementation, practical steps and common mistakes only; no theory, no ML term definitions, no vague advice
3) AI rewrite and editing tasks — own slot fills
```

## Output sample
```text
Start by cleaning and structuring your dataset into consistent input–output pairs in a format your training script expects. A common mistake is mixing formats or leaving noisy text, which silently ruins training quality.
[Run 2, first bullet]
```

## Why it works (mechanism)
Templates perform most reliably on process and task topics at implementation level; concept topics need an extra exclusion to prevent definition drift.

## Failure mode (specific, never generic)
Executive-angle runs drift into defining the topic without an explicit "do not introduce or define" exclusion; implementation altitude creeps above the stated audience level on complex technical topics (Run 3 read mid-level, not junior). Fixes produced Template 02.

## Evaluation angle
Stress-testing proves a prompt is production-ready, not lucky. Mercor / Outlier assessors check whether you can identify failure conditions systematically.

## Date
2026-05-27

## Model used
ChatGPT (web; exact model not recorded)
