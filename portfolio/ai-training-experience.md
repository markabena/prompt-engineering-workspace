# AI Training & Evaluation Experience

Paid work as an AI trainer on Handshake AI (2026) and Outlier AI. This page describes the **types of work and the methods I use**, not specific task content. All client prompts, data, rubrics, guidelines and reviewer feedback are confidential and are not in this repo.

## Task types I've worked on

| Area | What the work involves | Skills it exercised | Status |
|---|---|---|---|
| Adversarial visual QA | Writing questions about charts, dashboards, tables and dense scenes that a vision-language model gets wrong; deriving and verifying the correct answer; tagging reasoning skills | Multi-step chart reasoning, question design, answer-format precision | Production |
| Visual preference ranking | Ranking text-to-image and text-to-video outputs against prompt adherence, quality and safety criteria; audio/voice matching | Calibrated judgement, consistent criteria across batches | Production |
| Annotation critique | Grading other annotators' work against guidelines and writing the correction | Reviewer mindset, evidence-anchored feedback | Production |
| Video captioning & caption QA | Speech and audio/visual caption tracks to a detailed style guide; QA of existing captions | Attention to detail, guideline compliance | Production |
| Research prompt writing | Hard multi-hop research questions with verified answers and a source trail, tested against a frontier model | Search strategy, source verification, answer uniqueness | Production |
| Professional task + rubric authoring | Realistic professional prompts grounded in multi-file document environments, confirming model failure, writing the correct deliverable, and repairing the grading rubric | Domain reasoning, rubric design, failure analysis | Production |
| Agent preference comparison | Designing grounded prompts for agents working in sandboxed apps, then comparing two agent runs across multiple dimensions with written rationale | Agent evaluation, multi-dimension scoring | Production |
| Claim vs ground-truth checking | Checking whether a written description matches what a screenshot actually shows | Fact discipline, discrepancy detection | Onboarded |
| Coding benchmark task authoring | Terminal-based coding tasks packaged with Docker for agent benchmarks | Docker, task specification, test design | Onboarded |

*Production = tasks submitted. Onboarded = trained, not yet tasking.*

## How I work

**One SOP per project.** For each new project I turn the official guide into a condensed working SOP and a knowledge base, then log reviewer and tasker feedback against it as it comes in. For long guides this means condensing the material into a checklist I can work from live.

**Reviewer-first quality bar.** Each judgement is written so a second careful reviewer could reach the same verdict from the justification alone:

| Dimension | Pass | Fail |
|---|---|---|
| Accuracy | Claims verifiable, ratings match ground truth | Confident errors |
| Completeness | Every sub-part and field addressed | A sub-question silently skipped |
| Reasoning | The *why* is explicit and traceable | Verdict with no support |
| Instruction-following | Format and constraints obeyed literally | "Improving on" the instructions |
| Clarity | Verdict first, tight justification | Buried or hedged verdict |

**Failure patterns I screen for:** hallucinated details, unsupported claims, skipped instructions, weak reasoning chains, right-verdict-vague-justification, miscalibrated confidence, verbosity and format violations.

**Adversarial design.** When a task needs the model to fail, difficulty has to come from genuine reasoning (compound multi-step logic, cross-panel comparison, spatial judgement), not from ambiguity. Every term that could be read two ways is defined inside the prompt, and every answer has exactly one verifiable value.

## Public work samples

Samples in this repo use neutral practice material I wrote myself, never client data:

- [`../prompt-library/`](../prompt-library/): prompt technique entries with failure analysis
- [`../assessments/`](../assessments/): mock evaluations scored on the 5-element standard
- Planned: pairwise-rating drills, constraint-checklist audits and claim-labelling (true / false / unsupported) drills
