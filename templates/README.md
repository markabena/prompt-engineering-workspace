# Templates

Reusable prompt templates: fill-in-the-blank structures for recurring tasks. Where the [prompt library](../prompt-library/) records a single tested prompt and its evaluation, a template is a reusable scaffold.

- Naming: `NN-short-name.md`.
- Copy [`000-template.md`](000-template.md) to start a new one.

## Index

| # | Template | Purpose | Variables |
|---|---|---|---|
| 000 | [Template skeleton](000-template.md) | Starting point for new templates | — |
| 01 | [Universal zero-shot explainer](01-universal-zero-shot-explainer.md) | Explain any topic to any audience (superseded by 02) | topic, number, sentences, audience, altitude, angle, exclusions |
| 02 | [Universal zero-shot explainer — refined](02-universal-zero-shot-explainer-refined.md) | Same, with no definition drift and an audience-depth guardrail | topic, number, sentences, audience, altitude, angle, exclusions |
