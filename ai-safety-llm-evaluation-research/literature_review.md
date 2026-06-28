# Literature Review

Status: Initial literature review draft

This document summarizes the concepts that motivate the project. It is not a comprehensive academic survey.

## LLM Reliability

LLM reliability concerns whether model outputs are accurate, consistent, appropriately uncertain, and robust across different prompts and contexts. Reliability becomes especially important when users may treat generated text as advice or evidence.

## Hallucination

Hallucination occurs when a model generates unsupported or false information. In high-stakes settings, hallucination risk is dangerous because the answer can look plausible while being wrong.

## Overconfidence

Overconfidence occurs when a model expresses certainty beyond the available evidence. Safe responses should communicate uncertainty, state limits, and recommend verification where appropriate.

## Refusal Behavior

Safety refusal behavior matters when a user asks for harmful, illegal, or dangerous instructions. A good refusal should avoid actionable harmful detail while still offering safe alternatives or general guidance.

## Source Awareness

LLM responses should distinguish between verified facts and uncertain claims. In areas where rules, deadlines, laws, medical guidance, or financial conditions change, the model should encourage checking official or primary sources.

## Bias And Fairness

Bias risk appears when a model makes unsupported claims about demographic groups, stereotypes people, or gives uneven guidance. High-stakes systems should avoid broad generalizations and should be tested across varied inputs.

## High-Stakes Caution

Medical, legal, and financial advice require domain expertise and up-to-date evidence. LLMs should not act as final authorities in these areas.

## References To Expand

See `references.md` for sources and topics to review next.

