# 006 — Deliberate failure analysis — 5 failure types

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Deliberate failure analysis — 5 core zero-shot failure types

## Use case
Identifying and documenting root causes of prompt failure for evaluation work.

## The prompt (verbatim)
```text
5 deliberately bad prompts, one per failure type: ambiguity ("Write something about RAG models"), constraint conflict (RLHF — very detailed but two sentences), audience mismatch (APIs), scope overflow (MCPs), constraint conflict (pylon.py).
```

## Output sample
```text
"Write something about RAG models" — model produced a 4-section tutorial with no format control, no audience, and no depth filter because zero constraints were given.
```

## Why it works (mechanism)
Each failure type has a distinct root cause: ambiguity lets the model guess, scope overflow removes boundaries, constraint conflict forces impossible trade-offs, audience mismatch removes context, altitude collapse removes depth direction.

## Failure mode (specific, never generic)
Several failure types can trigger at once (pylon.py: constraint conflict with ambiguity layered under it). Name the primary failure first, then secondary ones — labelling one prompt as both scope overflow and constraint conflict without ranking them is imprecise.

## Evaluation angle
Evaluators who know failure types can explain WHY an output is weak, not just THAT it is — the root-cause precision that separates 3-star from 5-star evaluators on Outlier and Mercor.

## Date
2026-05-29

## Model used
ChatGPT, Perplexity AI (exact models not recorded)
