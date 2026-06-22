"""M2 lead intake: pull public leads, normalize, filter, and score.

Remote OK is the only source collected automatically — its public JSON API
permits it. We Work Remotely was removed (paid/low-value for this profile).
Everything else (OnlineJobs.ph, LinkedIn, Kalibrr, JobStreet, Indeed, Wellfound)
stays MANUAL — their ToS prohibit bots/scraping. Do not add them here.

The pure functions (``parse_remoteok``, ``collect_leads``) hold the testable
logic. ``fetch_remoteok`` is the network boundary: it lazy-imports requests so
the rest of the module — and the test suite — runs on the stdlib alone.
"""

from __future__ import annotations

from src.score import keyword_filter, fit_score

REMOTEOK_API = "https://remoteok.com/api"
USER_AGENT = "jc-job-hunt/1.0 (personal, approval-first; contact johnchrisley4@gmail.com)"


def _new_lead(**fields) -> dict:
    """A normalized lead with the defaults a public feed can't determine."""
    lead = {
        "platform": "",
        "job_title": "",
        "company": "",
        "job_link": "",
        "work_type": "Unknown",
        "remote_type": "Remote",
        "salary_or_rate": "",
        "tech_stack_keywords": "",
        "country_limit": "Unclear",   # human confirms at review
        "timezone_overlap": "Unclear",
        "risks_or_mismatch": "",
        "text": "",                   # transient: used for filtering/scoring only
    }
    lead.update(fields)
    return lead


def parse_remoteok(data: list[dict]) -> list[dict]:
    """Normalize the Remote OK JSON list into lead dicts.

    The first element is a legal/disclaimer blob with no ``position`` key and is
    skipped automatically (so does any other entry lacking a position).
    """
    leads: list[dict] = []
    for item in data:
        position = (item.get("position") or "").strip()
        if not position:
            continue
        company = (item.get("company") or "").strip()
        tags = item.get("tags") or []
        description = item.get("description") or ""
        smin, smax = item.get("salary_min") or 0, item.get("salary_max") or 0
        salary = f"{smin}-{smax}" if (smin or smax) else ""
        leads.append(_new_lead(
            platform="RemoteOK",
            job_title=position,
            company=company,
            job_link=item.get("url") or "",
            salary_or_rate=salary,
            tech_stack_keywords=", ".join(tags),
            text=f"{position} {company} {' '.join(tags)} {description}",
        ))
    return leads


def collect_leads(remoteok_data: list[dict], date_found: str) -> list[dict]:
    """Parse Remote OK, drop irrelevant leads, score and stamp the rest.

    ``date_found`` is injected (not read from the clock) so collection is
    deterministic and testable; the live runner passes the current timestamp.
    """
    leads = parse_remoteok(remoteok_data)
    kept: list[dict] = []
    for lead in leads:
        if not keyword_filter(lead["text"]):
            continue
        lead["date_found"] = date_found
        lead["fit_score"] = fit_score(lead)
        lead["status"] = "New"
        kept.append(lead)
    return kept


# --- network boundary (lazy imports; not unit-tested) ----------------------

def fetch_remoteok() -> list[dict]:
    import requests  # lazy: keeps the stdlib-only path importable without it

    resp = requests.get(REMOTEOK_API, headers={"User-Agent": USER_AGENT}, timeout=30)
    resp.raise_for_status()
    return resp.json()
