"""M2 tracker: persist scored leads to a CSV with the report's schema.

The column set mirrors deep-research-report.md so the local CSV and a Google
Sheet stay interchangeable. ``write_leads`` only emits known columns (extra keys
like the transient ``text`` are dropped; missing ones are blank), and
``merge_leads`` enforces "only new leads" by deduping on ``job_link``.
"""

from __future__ import annotations

import csv

# Order matters: this is the CSV header. Sourced from deep-research-report.md.
TRACKER_COLUMNS = [
    "date_found",
    "platform",
    "job_title",
    "company",
    "job_link",
    "company_site",
    "country_limit",
    "work_type",
    "remote_type",
    "timezone_overlap",
    "salary_or_rate",
    "tech_stack_keywords",
    "fit_score",
    "fit_reason",
    "risks_or_mismatch",
    "status",
    "resume_version",
    "cover_letter_version",
    "app_answers_version",
    "approval_packet_link",
    "submission_method",
    "submit_button_note",
    "approved_by_you",
    "date_submitted",
    "follow_up_date",
    "result",
]


def write_leads(leads: list[dict], path: str) -> None:
    """Write leads to ``path`` as CSV, one row per lead, schema columns only."""
    with open(path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=TRACKER_COLUMNS,
                                extrasaction="ignore")
        writer.writeheader()
        for lead in leads:
            writer.writerow({col: lead.get(col, "") for col in TRACKER_COLUMNS})


def read_leads(path: str) -> list[dict]:
    """Read a tracker CSV back into a list of dicts."""
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def merge_leads(existing: list[dict], new: list[dict]) -> list[dict]:
    """Append only leads whose ``job_link`` isn't already tracked.

    Existing rows are preserved as-is; duplicates within ``new`` collapse to the
    first occurrence. This is how "only new, verified leads" is enforced.
    """
    seen = {lead.get("job_link") for lead in existing if lead.get("job_link")}
    merged = list(existing)
    for lead in new:
        link = lead.get("job_link")
        if link and link in seen:
            continue
        if link:
            seen.add(link)
        merged.append(lead)
    return merged


def select_new(existing: list[dict], new: list[dict]) -> list[dict]:
    """Return only the leads in ``new`` not already tracked in ``existing``.

    This is ``merge_leads`` seen from the other side: it yields just the genuinely
    new rows (deduped within the batch too), so the runner can report and email
    them without re-diffing the whole CSV.
    """
    seen = {lead.get("job_link") for lead in existing if lead.get("job_link")}
    fresh: list[dict] = []
    for lead in new:
        link = lead.get("job_link")
        if link and link in seen:
            continue
        if link:
            seen.add(link)
        fresh.append(lead)
    return fresh
