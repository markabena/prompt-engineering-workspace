# 01 — Universal Zero-Shot Explainer

> Recovered 2026-10-06 from the original training chat. Created 2026-05-27 (library entry 004). Superseded by template 02.

**Purpose:** Explain any topic to any audience with full output control.
**Best with:** ChatGPT (tested on concept, process, and task topics).

## Variables
| Variable | Description | Example |
|---|---|---|
| `{{topic}}` | Subject to explain | Reinforcement learning |
| `{{number}}` | Bullet count | 4 |
| `{{sentences}}` | Sentences per bullet | 2 |
| `{{audience}}` | Who is reading | Business executive |
| `{{altitude}}` | surface / implementation / executive | executive |
| `{{angle}}` | The one aspect to focus on | Investment risk and opportunity |
| `{{exclusion_1..3}}` | 2–3 concrete exclusions | technical jargon |

## System prompt
```text
(none — single user prompt)
```

## User prompt
```text
Explain {{topic}} in {{number}} bullet points, {{sentences}} sentences each. Write for {{audience}} at {{altitude}} level. Focus on {{angle}} only. Do not include {{exclusion_1}}, do not use {{exclusion_2}}, avoid {{exclusion_3}}.
```

## Expected output shape
Exactly {{number}} bullets, {{sentences}} sentences each, no headers or intro.

## Notes
Breaks on concept topics (definition drift) and lets altitude creep above the stated audience — see entry 005 and template 02.
