# 003 — Specificity filters — altitude and angle

> Recovered 2026-10-06 from the original training chat. Output samples are the excerpts saved at the time; full outputs were not preserved.

## Technique
Zero-shot with specificity filters (altitude and angle)

## Use case
Tailoring the same topic for different audiences without changing the subject.

## The prompt (verbatim)
```text
Explain data privacy at an implementation level for a developer. In 3 bullet points, 2 sentences each. Focus on what needs to be built, not what data privacy means.
```

## Output sample
```text
Data privacy in software development involves controlling how user data is collected, stored, processed, and shared within an application. Developers implement this using access controls, encryption, secure authentication, and proper database permissions.
[first bullet only]
```

## Why it works (mechanism)
The altitude filter sets the depth, the angle filter sets the perspective — together they eliminate the model's default general-audience tone and force domain-relevant output.

## Failure mode (specific, never generic)
Executive/business-angle prompts drift generic without consequence-level specificity ("builds customer trust", "strengthens brand reputation"). Push angle prompts toward numbers, liability, or decisions.

## Evaluation angle
Specificity filters adapt one prompt pattern to any audience. In Mercor / Outlier assessments audience-awareness is scored directly — generic responses fail even when factually correct.

## Date
2026-05-27

## Model used
ChatGPT (web; exact model not recorded)
