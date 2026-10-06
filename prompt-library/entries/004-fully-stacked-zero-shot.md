# 004 — Fully stacked zero-shot prompt

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Zero-shot fully stacked — output constraints + negative constraints + specificity filters

## Use case
Production-grade prompt for any topic requiring consistent, audience-specific output.

## The prompt (verbatim)
```text
Explain AI response rating in 5 bullet points, 2 sentences each. Write for a freelancer at implementation level. Focus on how a junior AI/ML engineer applies this in real work. Do not include technical jargon, do not use exclamation marks, avoid unverified data.
```

## Output sample
```text
AI response rating helps freelancers check whether an AI answer is clear, useful, and matches the user's request. It also helps improve the quality of future AI responses by identifying weak or inaccurate outputs.
[first bullet only]
```

## Why it works (mechanism)
Stacking all three constraint types removes model discretion — format, exclusions, and audience angle together produce reliable, repeatable, audience-specific output.

## Failure mode (specific, never generic)
Overlapping angle descriptors ("implementation level for a freelancer" + "junior AI/ML engineer") create redundancy; each constraint slot should add new information, not repeat another. Bare-topic baseline went textbook (accuracy/clarity/relevance) with extra sentences per bullet.

## Evaluation angle
A fully stacked prompt demonstrates systematic thinking — prompting as a design process, which is what Mercor / Outlier higher tiers screen for. Produced Template 01.

## Date
2026-05-27

## Model used
ChatGPT (web; exact model not recorded)
