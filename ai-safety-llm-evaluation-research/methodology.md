# Methodology

Status: Proposed evaluation framework

## Goal

The goal is to create a transparent rubric for reviewing LLM responses in high-stakes decision-support contexts.

## Inputs

Each evaluation item contains:

- Prompt ID
- Domain
- Prompt text
- Sample response
- Expected safe behavior

## Scoring Categories

The evaluator scores each response on:

- Hallucination risk
- Overconfidence
- Safety refusal quality
- Reasoning consistency
- Source awareness
- Bias risk
- Medical/legal/financial caution
- Uncertainty expression

## Output

The evaluator produces:

- Category scores
- Flags
- Notes
- Total score
- Risk level

## Human Review

Rule-based scoring is only a first pass. A human reviewer should inspect flagged examples and update the rubric when it misses important failures.

## Experiment Status

Experiments are not completed. This repository currently provides an initial research prototype.

