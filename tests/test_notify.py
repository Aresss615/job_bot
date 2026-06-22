"""Tests for the email digest formatter (src/notify.py).

Only ``format_digest`` is unit-tested — it is pure (leads in, subject/body out).
``send_email`` is the SMTP network boundary and is verified by running, not here.

Run from the repo root with:

    python3 -m unittest tests.test_notify
"""

import unittest

from src.notify import format_digest


class FormatDigestTests(unittest.TestCase):
    def _leads(self):
        return [
            {"fit_score": 70, "job_title": "Junior Backend Dev", "company": "Acme",
             "platform": "RemoteOK", "job_link": "https://x/1"},
            {"fit_score": 55, "job_title": "Automation Support", "company": "",
             "platform": "WeWorkRemotely", "job_link": "https://x/2"},
        ]

    def test_subject_states_count_and_date(self):
        subject, _ = format_digest(self._leads(), "2026-06-23")
        self.assertEqual(subject, "[job-bot] 2 new leads — 2026-06-23")

    def test_body_lists_each_lead_with_score_and_link(self):
        _, body = format_digest(self._leads(), "2026-06-23")
        self.assertIn("[70] Junior Backend Dev — Acme", body)
        self.assertIn("https://x/1", body)
        self.assertIn("[55] Automation Support", body)

    def test_body_is_sorted_by_fit_score_descending(self):
        leads = [
            {"fit_score": 30, "job_title": "Low", "job_link": "l"},
            {"fit_score": 80, "job_title": "High", "job_link": "h"},
        ]
        _, body = format_digest(leads, "2026-06-23")
        self.assertLess(body.index("High"), body.index("Low"))

    def test_falls_back_to_platform_when_company_blank(self):
        _, body = format_digest(self._leads(), "2026-06-23")
        self.assertIn("Automation Support — WeWorkRemotely", body)

    def test_empty_leads_states_none_found(self):
        subject, body = format_digest([], "2026-06-23")
        self.assertEqual(subject, "[job-bot] 0 new leads — 2026-06-23")
        self.assertIn("No new leads", body)


if __name__ == "__main__":
    unittest.main()
