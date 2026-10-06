# 02 — Universal Zero-Shot Explainer (Refined)

> Recovered 2026-10-06 from the original training chat. Created 2026-05-27 (library entry 005).

**Purpose:** Explain any topic to any audience with full output control and no definition drift.
**Best with:** ChatGPT (tested on concept, process, and task topics).

## Variables
| Variable | Description | Example |
|---|---|---|
| `{{topic}}` | Subject to explain | How to fine-tune an LLM |
| `{{number}}` | Bullet count | 5 |
| `{{sentences}}` | Sentences per bullet | 2 |
| `{{audience}}` | Who is reading | Junior developer |
| `{{altitude}}` | surface / implementation / executive | implementation |
| `{{angle}}` | The one aspect to focus on | Practical steps and common mistakes |
| `{{exclusion_1..3}}` | 2–3 concrete exclusions | theoretical background |

## System prompt
```text
(none — single user prompt)
```

## User prompt
```text
Explain {{topic}} in {{number}} bullet points, {{sentences}} sentences each. Write for {{audience}} at {{altitude}} level. Focus on {{angle}} only. Do not introduce or define the topic, do not include {{exclusion_1}}, do not use {{exclusion_2}}, avoid {{exclusion_3}}. Match depth strictly to {{audience}} experience level.
```

## Expected output shape
Exactly {{number}} bullets, {{sentences}} sentences each, starting straight into content with no definition opener.

## Notes
Changes from 01: added "Do not introduce or define the topic" as a default exclusion, and "Match depth strictly to audience experience level" as an altitude guardrail. For junior audiences also add "avoid advanced architectural terminology" (entry 007).
