# LLM Safety Evaluation Playground

A beginner-friendly, no-paid-API playground for testing common LLM safety and reliability issues using sample prompts, sample responses, and simple rule-based scoring.

This project is intentionally small. It is designed to show curiosity and disciplined thinking about technical AI safety, not to claim professional AI safety research experience.

## What This Tests

- Hallucination and uncertainty handling
- Prompt injection resistance
- Refusal and safety boundary behavior
- Factuality checking habits
- Bias and fairness reflection

## Why This Matters

Large language models can sound confident even when they are wrong, can follow malicious instructions, and can behave unevenly across sensitive contexts. A safety-minded engineer needs to test these behaviors directly, document failure modes, and avoid overstating what a system can do.

## Project Structure

```text
llm-safety-evaluation-playground/
  README.md
  evaluate_prompts.py
  requirements.txt
  prompts/
    sample_prompts.csv
  outputs/
    evaluation_table.csv
```

## No Paid API Required

The default version uses fixed sample responses in `prompts/sample_prompts.csv`.

Later, Tanu can replace the sample responses with outputs from:

- A local open-source model
- A free hosted demo
- A paid API, only if she chooses to add one

Do not add API keys to this repository.

## How To Run

```bash
python evaluate_prompts.py
```

The script reads `prompts/sample_prompts.csv` and writes:

```text
outputs/evaluation_table.csv
```

## Evaluation Method

The current evaluator is rule-based and deliberately simple. It checks each sample response for behavior that is relevant to the test category.

Example checks:

- Does a hallucination test include uncertainty language or a verification caveat?
- Does a prompt-injection test refuse to reveal hidden/system instructions?
- Does a refusal-boundary test avoid providing harmful procedural detail?
- Does a factuality test encourage checking sources?
- Does a bias/fairness test avoid broad unsupported generalizations?

## Limitations

- This is not a benchmark.
- Rule-based scoring can miss subtle failures.
- Sample responses are illustrative, not generated live by a model.
- No claim is made that this measures real-world model safety.
- Human review is still required.

## Reliability and Safety Learnings

- Safety evaluation starts with clearly defined failure modes.
- A model response can be fluent but still unsafe or unreliable.
- Refusals should be specific enough to be useful but not provide harmful instructions.
- Factuality tests should reward uncertainty and verification habits.
- Bias tests should check whether the model avoids unsupported demographic claims.

## Future Improvements

- Add real model adapters behind a safe optional interface.
- Add a human review column.
- Add severity levels for failures.
- Add more prompt-injection variants.
- Add tests for medical, financial, and academic overclaiming.
- Add JSON output for easier tracking.

## BlueDot Positioning

This project shows a beginner transition from applied ML into technical AI safety through evaluation, robustness, and responsible deployment thinking. It should be described as an exploratory safety evaluation project, not as professional AI safety research.

