"""M1 scoring engine: filter and score job leads against Jc's real profile.

Pure logic — no network, no file I/O. Two public functions:

- ``keyword_filter(text)``  -> keep/drop a lead by title/tag text.
- ``fit_score(lead)``       -> 0-100 fit score using the report's rubric.

The rubric (deep-research-report.md) has eight weighted categories. Some can be
read from a public feed (skill, seniority, role, flexibility, pay); others need a
human at review time (geography, legitimacy, portfolio relevance). Those default
to a conservative/"unclear" value and are flagged in ``score_breakdown`` so they
get corrected before any approval packet is built. NEVER treat the score as
final — it ranks the backlog, it does not approve anything.
"""

from __future__ import annotations

import re

# --- keyword sets (grounded in deep-research-report.md) -------------------

# A lead must hit at least one of these to be worth Jc's time.
POSITIVE_KEYWORDS = [
    "backend", "back-end", "python", "django", "php", "mysql", "api",
    "rest api", "api integration", "automation", "technical support",
    "internal tools", "business systems", "system developer", "qa",
    "intern", "internship", "junior", "entry level", "fresh graduate",
    "part time", "part-time", "contract", "freelance", "developer",
]

# If any of these appear, drop the lead regardless of positives — these are the
# roles Jc should NOT be positioned for (React/frontend specialist, senior).
NEGATIVE_KEYWORDS = [
    "react", "frontend", "front-end", "senior", "staff", "principal", "lead",
]

_FRONTEND_SKILLS = ["react", "frontend", "front-end", "next.js", "vue", "angular"]
_BACKEND_SKILLS = [
    "backend", "back-end", "python", "django", "php", "mysql",
    "api", "rest", "automation",
]
_SENIOR_TERMS = ["senior", "staff", "principal", "lead"]
_JUNIOR_TERMS = [
    "junior", "intern", "internship", "entry level", "fresh graduate",
    "trainee", "associate", "assistant", "student",
]
_BACKEND_ROLE = [
    "backend", "back-end", "api", "automation", "internal tools", "qa",
    "technical support", "system developer", "business systems", "integration",
]
_FRONTEND_ROLE = ["frontend", "front-end", "react", "ui developer"]
_FLEXIBLE = [
    "freelance", "part time", "part-time", "contract",
    "project based", "project-based", "async",
]


def _contains_any(text: str, words: list[str]) -> bool:
    """Word-boundary match so short terms like 'lead' don't hit 'leads'."""
    lower = text.lower()
    return any(re.search(rf"\b{re.escape(w)}\b", lower) for w in words)


def keyword_filter(text: str) -> bool:
    """Return True to KEEP the lead, False to drop it.

    Drop on any negative keyword; otherwise keep only if a positive matches.
    """
    if _contains_any(text, NEGATIVE_KEYWORDS):
        return False
    return _contains_any(text, POSITIVE_KEYWORDS)


def _geography_points(country_limit: str) -> int:
    val = (country_limit or "").strip().lower()
    if val in ("", "unclear"):
        return 10  # unknown from feed -> mid; human confirms at review
    if any(k in val for k in ("philippines", "global", "anywhere", "worldwide")):
        return 20
    return 0  # e.g. "US-only" / country-restricted


def _skill_points(text: str) -> int:
    backend = _contains_any(text, _BACKEND_SKILLS)
    frontend = _contains_any(text, _FRONTEND_SKILLS)
    if frontend and not backend:
        return 0
    if frontend and backend:
        return 10
    if backend:
        return 20
    return 10  # unknown -> mid


def _seniority_points(text: str) -> int:
    if _contains_any(text, _SENIOR_TERMS):
        return 0
    if _contains_any(text, _JUNIOR_TERMS):
        return 15
    return 5  # mid-level but possibly stretchable


def _role_points(text: str) -> int:
    if _contains_any(text, _BACKEND_ROLE):
        return 15
    if _contains_any(text, ["full stack", "full-stack"]):
        return 5
    if _contains_any(text, _FRONTEND_ROLE):
        return 0
    return 5  # generic -> mid


def _flexibility_points(text: str) -> int:
    if _contains_any(text, ["onsite", "on-site", "in office", "in-office"]):
        return 0
    if _contains_any(text, _FLEXIBLE):
        return 10
    return 5  # remote feeds default to full-time-remote-only


def _comp_points(salary_or_rate: str) -> int:
    return 5 if salary_or_rate and any(c.isdigit() for c in salary_or_rate) else 0


def score_breakdown(lead: dict) -> dict:
    """Per-category points plus the fields still needing human review.

    ``review`` lists categories defaulted conservatively because a public feed
    can't know them — correct these before building an approval packet.
    """
    text = lead.get("text", "")
    return {
        "geography": _geography_points(lead.get("country_limit", "")),
        "skill_truthfulness": _skill_points(text),
        "seniority": _seniority_points(text),
        "role_alignment": _role_points(text),
        "flexibility": _flexibility_points(text),
        "legitimacy": 5,   # TODO(review): verify employer / scam signals
        "portfolio": 0,    # TODO(review): raise to 5 if Jc has relevant proof
        "compensation": _comp_points(lead.get("salary_or_rate", "")),
        "review": ["geography", "legitimacy", "portfolio"],
    }


def fit_score(lead: dict) -> int:
    """Return the 0-100 fit score for a lead dict.

    Expected keys (all optional): ``text`` (title + tags + description),
    ``salary_or_rate``, ``country_limit``.
    """
    breakdown = score_breakdown(lead)
    return sum(v for k, v in breakdown.items() if k != "review")
