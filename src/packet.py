"""M3 approval-packet generator: render one lead into the report's template.

This module is the approval-first guardrail expressed as code. It fills only the
facts a lead already carries (link, company, platform, fit score) and leaves
every tailored part — resume changes, cover letter, application answers, the
exact text to submit, and the submit action — as an explicit ``[TODO ...]``.

It NEVER writes submittable content and NEVER marks anything approved. Every
packet ends at "Status: Awaiting your approval"; only Jc, by hand, moves it past
that line. See deep-research-report.md ("approval packet") for the source format
and the reusable tailoring prompts that fill the TODOs.
"""

from __future__ import annotations

# The fixed section labels, in order, from the report's approval packet.
REQUIRED_SECTIONS = [
    "Job link:",
    "Company:",
    "Platform:",
    "Fit score:",
    "Why it fits:",
    "Risks / mismatch:",
    "Tailored resume changes:",
    "Tailored cover letter:",
    "Application answers:",
    "Exact final text to submit:",
    "What button or action would submit it:",
    "Status: Awaiting your approval",
]

# Placeholders for the parts a human (or an AI prompt) must fill at review time.
_TODO_TAILOR = "[TODO before submission — use the tailoring prompts in deep-research-report.md]"
_TODO_SUBMIT = "[TODO — Jc fills after manual review; nothing here is auto-submitted]"


def _value_or_todo(lead: dict, key: str) -> str:
    value = str(lead.get(key, "") or "").strip()
    return value if value else "[TODO: fill at review]"


def render_packet(lead: dict) -> str:
    """Return the approval packet for ``lead`` as a Markdown string.

    Known fields are filled from the lead; tailored fields are TODO placeholders.
    The packet always ends at "Status: Awaiting your approval".
    """
    title = lead.get("job_title", "") or "(untitled role)"
    lines = [
        f"# Approval packet — {title}",
        "",
        f"Job link: {lead.get('job_link', '') or '[TODO: fill at review]'}",
        f"Company: {lead.get('company', '') or '[TODO: fill at review]'}",
        f"Platform: {lead.get('platform', '') or '[TODO: fill at review]'}",
        f"Fit score: {lead.get('fit_score', '')}/100",
        "",
        f"Why it fits: {_value_or_todo(lead, 'fit_reason')}",
        f"Risks / mismatch: {_value_or_todo(lead, 'risks_or_mismatch')}",
        "",
        f"Tailored resume changes: {_TODO_TAILOR}",
        f"Tailored cover letter: {_TODO_TAILOR}",
        f"Application answers: {_TODO_TAILOR}",
        "",
        f"Exact final text to submit: {_TODO_SUBMIT}",
        f"What button or action would submit it: {_TODO_SUBMIT}",
        "",
        "Status: Awaiting your approval",
    ]
    return "\n".join(lines)
