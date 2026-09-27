# CLAUDE.md — prompt-engineering-workspace

Public GitHub portfolio + working lab for Mark Abena's prompt engineering and AI evaluation track.
Remote: https://github.com/markabena/prompt-engineering-workspace — default branch `main`.
Mirror: https://github.com/markabena/AI-Evaluation-Portfolio — `origin` has both as push URLs, so `git push` updates both. Fetch/pull comes from prompt-engineering-workspace only; never edit the mirror directly on GitHub.

## Who this is for
Mark: B.Eng Aerospace Engineering (AFIT Kaduna, 2026). Targets higher-tier AI evaluation work on Mercor, Outlier AI and Handshake AI.
Python level is foundational: explain non-obvious code briefly, keep scripts simple and readable.

## Repo layout
| Folder | Purpose |
|---|---|
| `prompts/system/`, `prompts/user/` | Prompt templates loaded by scripts |
| `scripts/` | Python scripts (Anthropic SDK). `pipeline.py` is the main runner |
| `tests/` | Promptfoo eval configs and test cases |
| `notebooks/` | Experiments |
| `docs/` | Prompt changelogs and design notes |
| `prompt-library/entries/` | One file per library entry: `NNN-short-name.md` |
| `templates/` | Reusable prompt templates: `NN-short-name.md` |
| `assessments/` | Monthly mock assessments: `YYYY-MM-month-N.md` |
| `projects/` | Project Mode builds, one folder each, from `_project-template/` |
| `portfolio/` | Non-PE work: CFD, FEM, Claude skills, MCP |

## Library entry format (never rename fields)
Technique · Use case · The prompt (verbatim) · Output sample · Why it works (mechanism) · Failure mode (specific, never generic) · Evaluation angle · Date · Model used.
Every new entry also gets a row in `prompt-library/README.md`.

## Evaluation writing standard
Every written evaluation has: 1) rating upfront (e.g. 2/5), 2) named failure types, 3) quoted evidence from the output, 4) root cause traced to the original prompt, 5) fix direction.

## Hard rules — public repo
- NEVER commit Handshake AI / Outlier / Mercor task content: real prompts, images, rubrics, QC feedback, project names' internal details (Lizard, BabyVision, Seal, Parchment, Buckeye, Octahedron etc.). They are under NDA. Practice exercises only.
- NEVER commit `.env`, API keys, tokens, student ID, CGPA, or client data from the advisory/KDP businesses.
- Before every commit, run `git status` and `git diff --cached --stat` and check nothing above is staged.

## Code conventions
- Anthropic SDK: system prompt goes in `system=`, never as a `"system"` role inside `messages`.
- Load keys with `python-dotenv` from `.env`. Default model is set in one place, not hard-coded per script.
- Results write to `results/` (gitignored). Logs to `logs/` (gitignored).

## Git workflow
- Work on `main`. Small commits, message format: `area: what changed` (e.g. `library: add entry 009 few-shot classification`).
- Line endings normalised via `.gitattributes` (`* text=auto`).
- Ask before force-pushing, deleting branches, or rewriting history.
- Push after each logical unit of work so GitHub stays current.
