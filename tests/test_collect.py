"""Tests for the M1->M2 lead intake (src/collect.py).

Network is kept out of these tests: the pure parse/normalize/score functions
are exercised against inline fixtures that mimic the Remote OK JSON API and the
We Work Remotely RSS feed. The live ``fetch_*`` wrappers (which import requests /
feedparser) are the I/O boundary and are not unit-tested here.

Run from the repo root with:

    python3 -m unittest tests.test_collect
"""

import unittest

from src.collect import parse_remoteok, parse_wwr, collect_leads


# --- inline fixtures -------------------------------------------------------

# Remote OK returns a list whose first element is a legal/disclaimer blob with
# no "position" key; real job objects follow.
REMOTEOK_FIXTURE = [
    {"legal": "See https://remoteok.com/api for terms"},
    {
        "position": "Junior Backend Developer",
        "company": "Acme Remote",
        "description": "Django and REST API work. Part time, contract.",
        "tags": ["python", "django", "api"],
        "url": "https://remoteok.com/jobs/111",
        "salary_min": 1500,
        "salary_max": 2500,
    },
    {
        "position": "Senior React Frontend Engineer",
        "company": "Pixel Co",
        "description": "Lead our React frontend team.",
        "tags": ["react", "frontend"],
        "url": "https://remoteok.com/jobs/222",
        "salary_min": 0,
        "salary_max": 0,
    },
]

# feedparser entries expose .title/.link/.summary; a dict with those keys is the
# shape the fetch wrapper hands to parse_wwr.
WWR_FIXTURE = [
    {
        "title": "Acme Remote: Python Automation Developer",
        "link": "https://weworkremotely.com/jobs/333",
        "summary": "<p>Build <b>automation</b> with Python. Junior friendly.</p>",
    },
    {
        "title": "Pixel Co: Senior Frontend Engineer",
        "link": "https://weworkremotely.com/jobs/444",
        "summary": "<p>React, Next.js, principal level.</p>",
    },
]


class ParseRemoteOkTests(unittest.TestCase):
    def test_skips_legal_blob(self):
        leads = parse_remoteok(REMOTEOK_FIXTURE)
        self.assertEqual(len(leads), 2)  # the {"legal": ...} entry is dropped

    def test_normalizes_core_fields(self):
        lead = parse_remoteok(REMOTEOK_FIXTURE)[0]
        self.assertEqual(lead["platform"], "RemoteOK")
        self.assertEqual(lead["job_title"], "Junior Backend Developer")
        self.assertEqual(lead["company"], "Acme Remote")
        self.assertEqual(lead["job_link"], "https://remoteok.com/jobs/111")
        self.assertEqual(lead["remote_type"], "Remote")

    def test_combines_salary_range(self):
        lead = parse_remoteok(REMOTEOK_FIXTURE)[0]
        self.assertEqual(lead["salary_or_rate"], "1500-2500")

    def test_blank_salary_when_zero(self):
        lead = parse_remoteok(REMOTEOK_FIXTURE)[1]  # the 0/0 salary job
        self.assertEqual(lead["salary_or_rate"], "")

    def test_text_includes_title_and_tags(self):
        lead = parse_remoteok(REMOTEOK_FIXTURE)[0]
        self.assertIn("backend", lead["text"].lower())
        self.assertIn("django", lead["text"].lower())


class ParseWwrTests(unittest.TestCase):
    def test_normalizes_core_fields(self):
        lead = parse_wwr(WWR_FIXTURE)[0]
        self.assertEqual(lead["platform"], "WeWorkRemotely")
        self.assertEqual(lead["job_link"], "https://weworkremotely.com/jobs/333")
        self.assertEqual(lead["remote_type"], "Remote")

    def test_splits_company_from_title(self):
        # WWR titles look like "Company: Role".
        lead = parse_wwr(WWR_FIXTURE)[0]
        self.assertEqual(lead["company"], "Acme Remote")
        self.assertEqual(lead["job_title"], "Python Automation Developer")

    def test_strips_html_from_summary(self):
        lead = parse_wwr(WWR_FIXTURE)[0]
        self.assertNotIn("<", lead["text"])
        self.assertIn("automation", lead["text"].lower())


class CollectLeadsTests(unittest.TestCase):
    def test_drops_negative_keyword_leads(self):
        leads = collect_leads(REMOTEOK_FIXTURE, WWR_FIXTURE, date_found="2026-06-22")
        titles = [l["job_title"] for l in leads]
        self.assertNotIn("Senior React Frontend Engineer", titles)
        self.assertNotIn("Senior Frontend Engineer", titles)

    def test_keeps_relevant_leads_from_both_sources(self):
        leads = collect_leads(REMOTEOK_FIXTURE, WWR_FIXTURE, date_found="2026-06-22")
        platforms = {l["platform"] for l in leads}
        self.assertEqual(platforms, {"RemoteOK", "WeWorkRemotely"})

    def test_sets_score_status_and_date(self):
        leads = collect_leads(REMOTEOK_FIXTURE, WWR_FIXTURE, date_found="2026-06-22")
        lead = leads[0]
        self.assertIsInstance(lead["fit_score"], int)
        self.assertEqual(lead["status"], "New")
        self.assertEqual(lead["date_found"], "2026-06-22")


if __name__ == "__main__":
    unittest.main()
