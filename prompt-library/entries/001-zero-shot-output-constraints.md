# 001 — Zero-shot with output constraints

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Zero-shot prompting

## Use case
Getting structured, predictable explanations on any topic.

## The prompt (verbatim)
```text
Explain Machine Learning in 5 bullet points. Each bullet should be two sentences. Focus on the meaning and advantages in recent times, how to scale up, key evidences and conclusion
```

## Output sample
```text
Machine Learning is a branch of Artificial Intelligence that allows computers to learn patterns from data and improve performance without being directly programmed for every task. It helps systems make predictions, recognize trends, and automate decision-making across industries such as healthcare, finance, aerospace, and cybersecurity.
[first bullet only — remaining bullets not preserved]
```

## Why it works (mechanism)
Constraints remove the model's discretion — format, length, scope and exclusion filters force the output into a predictable shape.

## Failure mode (specific, never generic)
Too many simultaneous constraints create conflict; vague scope filters let the model default to generic content. Observed: all 5 bullets came out at the same depth and voice — constraints controlled structure but not per-section specificity.

## Evaluation angle
Zero-shot works reliably when you treat the prompt like a spec — task, format, scope, and exclusion. Without constraints the model optimizes for completeness, not usefulness. (Mercor / Outlier)

## Date
2026-05-26

## Model used
ChatGPT (web; exact model not recorded)
