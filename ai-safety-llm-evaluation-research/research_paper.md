# Evaluating Reliability and Risk Patterns in LLM Responses for High-Stakes Decision Support

Independent AI Safety Research Project

Author: Tanu Meena

Status: Initial research prototype

## Abstract

Large language models can provide fluent and useful responses, but they can also produce hallucinations, overconfident claims, weak source awareness, biased reasoning, and unsafe guidance in high-stakes contexts. This project proposes a beginner-friendly evaluation framework for analyzing reliability and risk patterns in LLM-generated responses for decision-support scenarios. The current work includes a risk taxonomy, sample prompts, rubric-based scoring categories, and a lightweight Python prototype. It does not present completed experimental findings or peer-reviewed results. The purpose is to build a foundation for future technical AI safety work through transparent evaluation design.

## 1. Motivation

LLMs are increasingly used for tasks that affect real decisions: health questions, legal interpretation, financial planning, academic support, career guidance, and technical troubleshooting. In these settings, a response can be harmful even when it sounds confident and well-written.

The central concern of this project is simple: a model response should not be judged only by fluency. It should also be evaluated for uncertainty, factuality, source awareness, refusal behavior, bias risk, and caution in sensitive domains.

## 2. Research Question

How can a lightweight rubric help identify reliability and safety risks in LLM responses for high-stakes decision-support prompts?

Sub-questions:

- When does an answer show hallucination risk?
- When is the model too confident?
- Does the response recommend verification from official or primary sources?
- Does the response refuse unsafe requests in a useful and bounded way?
- Does the response show appropriate medical, legal, or financial caution?
- Does the response avoid unsupported demographic claims?

## 3. Method

This project uses a rubric-based evaluation framework. Each prompt-response pair is scored across categories such as hallucination risk, overconfidence, safety refusal quality, reasoning consistency, source awareness, bias risk, high-stakes caution, and uncertainty expression.

The prototype uses sample prompts and sample responses. It is designed to run locally without paid APIs. The current implementation is a starting point for future experiments with real model outputs.

## 4. Connection To Technical AI Safety

Technical AI safety includes the study of how AI systems fail, how to evaluate those failures, and how to build systems that are more reliable and aligned with human needs. This project focuses on the evaluation side. It asks what kinds of failure patterns should be measured before LLMs are used in sensitive settings.

## 5. Connection To Tanu's Background

My background is in applied ML and computer vision. In my shelf product detection project, reliability issues include false positives, false negatives, lighting variation, occlusion, and threshold sensitivity. In healthcare and insurance prediction projects, evaluation choices can affect real-world risk. This project extends that same evaluation mindset to LLM responses.

## 6. Current Status

This is an initial research prototype. It includes:

- A proposed risk taxonomy
- A scoring rubric
- Sample prompts and sample responses
- A Python evaluator
- A markdown report generator

It does not include:

- Live LLM API evaluation
- Human annotator study
- Large-scale benchmark results
- Peer-reviewed claims

## 7. Next Steps

Future versions should evaluate real model outputs, add human review labels, compare models, and refine the rubric using error analysis.

