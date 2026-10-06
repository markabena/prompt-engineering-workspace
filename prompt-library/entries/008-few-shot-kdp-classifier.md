# 008 — Few-shot classification (KDP blurb niches)

> Recovered 2026-10-06. The prompt was built in the Day 8 session (Jul 2026), but the run output and analysis were never recorded. The entry is incomplete until the prompt is re-run and the output pasted below.

## Technique
Few-shot classification (3 shots, fixed label set)

## Use case
Classifying a book description into one KDP niche category — reusable for the KDP niche research agent.

## The prompt (verbatim)
```text
Classify each book description into exactly one niche category:
"Journals & Notebooks", "Coloring Books", "Puzzle & Activity Books",
"Low-Content Planners", "Children's Picture Books".

Description: "A blank lined notebook with a minimalist floral cover,
120 pages, perfect for daily journaling or gift-giving."
Category: Journals & Notebooks

Description: "50 intricate mandala designs for adults to color,
single-sided pages to prevent bleed-through, great for stress relief."
Category: Coloring Books

Description: "A 90-day fitness and habit tracker with weekly goal-setting
pages, water intake logs, and meal planning grids."
Category: Low-Content Planners

Description: "A collection of 100 word search puzzles themed around
US national parks, medium difficulty, answer key included."
Category:
```

## Output sample
```text
[NOT RECORDED — re-run and paste the completion here]
```

## Why it works (mechanism)
The three shots show the exact output shape (one label, nothing else) and vary in blurb style — narrative, feature list, hybrid — so the model has to match on content rather than sentence structure.

## Failure mode (specific, never generic)
Two of the five labels ("Puzzle & Activity Books", "Children's Picture Books") have no example, so their boundaries are defined only by name. Watch for shot leakage (matching surface features of the examples) and order bias (the last shot, a planner, pulling ambiguous inputs toward "Low-Content Planners").

## Evaluation angle
Mercor / Outlier few-shot diagnosis: name the specific cause — shot leakage, order bias, format inconsistency, or uncovered classes — instead of "the examples were bad".

## Date
2026-07 (built); run not recorded

## Model used
ChatGPT (planned)
