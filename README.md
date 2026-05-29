# Prompt Engineering Workspace

A minimal workspace for prompt engineering experiments.

## Tools
Anthropic Console · Promptfoo · LangSmith · Python

## Quick start

Open this folder in VS Code and create your prompts and experiments.

To create and enter the project folder in PowerShell:

```powershell
mkdir "prompt-engineering-workspace"; Set-Location "prompt-engineering-workspace"
```

## Structure

prompts/     → system and user prompt templates
tests/       → promptfoo eval configs and test cases
scripts/     → pipeline scripts
notebooks/   → experimentation
docs/        → prompt changelogs and design notes

## Notes
- Keep sensitive keys in `.env` and out of source control.
- Use `tests/` with Promptfoo for repeatable evaluations.

## Anthropic Starter

A simple example is available at `scripts/anthropic_example.py`.

```powershell
python scripts/anthropic_example.py
```

Be sure `ANTHROPIC_API_KEY` is set in `.env` before running.
