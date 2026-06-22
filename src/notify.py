"""Email digest of newly-collected leads.

Two pieces, split along the same line as the rest of the codebase:

- ``format_digest`` is pure (leads + date -> subject + plain-text body) and is
  unit-tested.
- ``send_email`` is the SMTP network boundary; it lazy-imports nothing (stdlib
  ``smtplib`` only) and is exercised by running, not by unit tests.

This module NEVER contacts an employer. It only mails Jc a list of the public
leads the collector found, so it cannot violate the approval-first rule — the
links go to his own inbox for manual review.
"""

from __future__ import annotations

import os
import smtplib
from email.message import EmailMessage


def _as_int(value) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def format_digest(leads: list[dict], date: str) -> tuple[str, str]:
    """Return ``(subject, body)`` for a digest of ``leads`` found on ``date``.

    Leads are listed highest fit score first. ``company`` falls back to
    ``platform`` when blank. An empty list still produces a valid (empty) digest.
    """
    subject = f"[job-bot] {len(leads)} new leads — {date}"
    if not leads:
        return subject, f"No new leads on {date}.\n"

    ordered = sorted(leads, key=lambda l: _as_int(l.get("fit_score")), reverse=True)
    lines = [f"{len(leads)} new job leads found on {date} "
             f"(highest fit first). Review before applying — nothing was submitted.",
             ""]
    for lead in ordered:
        who = lead.get("company") or lead.get("platform") or "—"
        lines.append(f"[{lead.get('fit_score')}] {lead.get('job_title')} — {who}")
        lines.append(f"    {lead.get('job_link')}")
        lines.append("")
    return subject, "\n".join(lines)


# --- network boundary (stdlib smtplib; not unit-tested) --------------------

def email_config_from_env() -> dict | None:
    """Read SMTP settings from the environment, or ``None`` if not configured.

    Required: ``SMTP_USER``, ``SMTP_PASS``, ``DIGEST_TO``.
    Optional: ``SMTP_HOST`` (default smtp.gmail.com), ``SMTP_PORT`` (default 587),
    ``DIGEST_FROM`` (defaults to ``SMTP_USER``).
    """
    user = os.environ.get("SMTP_USER")
    password = os.environ.get("SMTP_PASS")
    to_addr = os.environ.get("DIGEST_TO")
    if not (user and password and to_addr):
        return None
    return {
        "host": os.environ.get("SMTP_HOST", "smtp.gmail.com"),
        "port": int(os.environ.get("SMTP_PORT", "587")),
        "user": user,
        "password": password,
        "from_addr": os.environ.get("DIGEST_FROM", user),
        "to_addr": to_addr,
    }


def send_email(subject: str, body: str, config: dict) -> None:
    """Send a plain-text email via STARTTLS using ``config`` (see env helper)."""
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = config["from_addr"]
    msg["To"] = config["to_addr"]
    msg.set_content(body)

    with smtplib.SMTP(config["host"], config["port"], timeout=30) as smtp:
        smtp.starttls()
        smtp.login(config["user"], config["password"])
        smtp.send_message(msg)
