# 002 — Zero-shot with negative constraints

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Zero-shot with negative constraints

## Use case
Controlling what the model excludes to tighten output focus.

## The prompt (verbatim)
```text
Describe the benefits of cloud computing in 5 bullet points, two sentences each. Focus on real-world business applications only. Do not mention databases, do not include cost-related points, do not use technical jargon.
```

## Output sample
```text
Cloud computing improves collaboration among users and teams. Multiple people can work on the same files and applications in real time.
[one bullet only — rest not preserved]

Baseline ("Describe the benefits of cloud computing", no constraints): 7 bullets instead of 5, unrequested headers, longer bullets.
```

## Why it works (mechanism)
Negative constraints remove the model's default filler topics — without them the model covers everything it associates with the subject regardless of relevance.

## Failure mode (specific, never generic)
Vague exclusions like "avoid unnecessary grammar" are ignored — the model has no concrete target to exclude. Constraints must be concrete (e.g. "do not use technical jargon").

## Evaluation angle
Negative constraints are what separate a prompt that works once from one that works reliably. Evaluators (Mercor / Outlier) test for this by checking output consistency across multiple runs.

## Date
2026-05-27

## Model used
ChatGPT (web; exact model not recorded)
