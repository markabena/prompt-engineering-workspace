# Prompt Engineering Workspace

**Mark Abena** — B.Eng Aerospace Engineering, Air Force Institute of Technology (AFIT) Kaduna, 2026.
I work in prompt engineering and AI evaluation: writing prompts that hold up under testing, and writing evaluations that explain *why* a model output fails and how to fix the prompt behind it.

This repo is both my working lab (scripts, prompt templates, evals) and my public portfolio.

## What's here

| Folder | What it contains |
|---|---|
| [`prompt-library/`](prompt-library/) | Tested prompts, one technique per entry, each with output, mechanism, failure mode and evaluation angle |
| [`templates/`](templates/) | Reusable prompt templates for recurring tasks |
| [`assessments/`](assessments/) | Monthly mock assessments with a running score table |
| [`projects/`](projects/) | End-to-end builds written up as problem → approach → methodology → results |
| [`portfolio/`](portfolio/) | Engineering work (CFD icing FYP, FEM coursework) and the Claude skills / MCP track |
| [`prompts/`](prompts/) | System and user prompt templates loaded by the scripts |
| [`scripts/`](scripts/) | Python scripts using the Anthropic SDK; `pipeline.py` is the main runner |
| [`tests/`](tests/) | Promptfoo eval configs and test cases |
| [`notebooks/`](notebooks/) | Experiments |
| [`docs/`](docs/) | Prompt changelogs and design notes |

## Evaluation standard

Every written evaluation in this repo has five elements:

1. **Rating upfront**: e.g. 2/5, stated before any discussion.
2. **Named failure types**: e.g. instruction non-compliance, unsupported claim, format drift.
3. **Quoted evidence**: the exact text from the output that shows each failure.
4. **Root cause**: traced back to the specific part of the original prompt that allowed it.
5. **Fix direction**: what to change in the prompt to prevent it.

## Roadmap

| Phase | Goal | Status |
|---|---|---|
| 1 | Workspace setup: repo, folder structure, VS Code | ✅ Done |
| 2 | Anthropic SDK installed and API connection verified | ✅ Done |
| 3 | Pipeline script and system prompt templates | ✅ Done |
| 4 | Portfolio layer: prompt library, templates, assessments, projects, portfolio | ✅ Done |
| 5 | Fill the prompt library and run Promptfoo evals against it | ⏳ Next |
| 6 | Project Mode builds and monthly assessments | Planned |

## Tools

Anthropic Console · Claude API (Python SDK) · Promptfoo · LangSmith · Python · VS Code · Git/GitHub · ANSYS

## Certifications

- **AI Fluency**: Anthropic
- **Prompt Engineering**: Google Cloud
- **ANSYS CFD** course completion: Udemy

## Quick start

Open this folder in VS Code and create your prompts and experiments.

To create and enter the project folder in PowerShell:

```powershell
mkdir "prompt-engineering-workspace"; Set-Location "prompt-engineering-workspace"
```

Install dependencies and add your API key:

```powershell
python -m pip install -r requirements.txt
# then create .env containing: ANTHROPIC_API_KEY=your-key-here
```

Run the starter example or the main pipeline:

```powershell
python scripts/anthropic_example.py
python scripts/pipeline.py
```

The default model for all scripts is set once in [`scripts/config.py`](scripts/config.py).

## Notes

- Keep sensitive keys in `.env`, which is gitignored and never committed.
- Use `tests/` with Promptfoo for repeatable evaluations.
- Everything in this repo is personal practice material. No client or platform task content.

## License

See [LICENSE](LICENSE).
