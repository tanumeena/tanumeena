"""Generate a simple markdown report from the evaluator output."""

from __future__ import annotations

from pathlib import Path

try:
    from evaluator import evaluate_all, write_csv
except ImportError:
    from src.evaluator import evaluate_all, write_csv


ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = ROOT / "reports"
REPORT_PATH = REPORTS_DIR / "sample_evaluation_report.md"


def build_report() -> str:
    rows = evaluate_all()
    lines = [
        "# Sample LLM Reliability Evaluation Report",
        "",
        "Status: Initial research prototype",
        "",
        "This report uses sample responses and rule-based scoring. It is not a benchmark and should be reviewed by a human evaluator.",
        "",
        "## Summary",
        "",
        "| ID | Domain | Total Score | Risk Level | Notes |",
        "|---|---|---:|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['id']} | {row['domain']} | {row['total_score']}/{row['max_score']} | {row['risk_level']} | {row['notes']} |"
        )

    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "High scores indicate that the sample response includes several reliability and safety-positive behaviors, such as uncertainty, source awareness, refusal of unsafe requests, or high-stakes caution.",
            "",
            "Low scores do not prove a response is harmful, but they indicate that a human reviewer should inspect the response carefully.",
            "",
            "## Limitations",
            "",
            "- The rubric is simple and keyword-based.",
            "- The current responses are samples, not live model outputs.",
            "- Human review is required.",
            "- No experimental claims should be made from this prototype alone.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = evaluate_all()
    write_csv(rows)
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(build_report(), encoding="utf-8")
    print(f"Wrote report to {REPORT_PATH}")


if __name__ == "__main__":
    main()

