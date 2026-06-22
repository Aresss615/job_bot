"""Tests for the CSV tracker (src/tracker.py).

Uses a temp file for the read/write round-trip — that is the unit under test, so
real (local) file I/O is intentional here. No network.

Run from the repo root with:

    python3 -m unittest tests.test_tracker
"""

import os
import tempfile
import unittest

from src.tracker import (
    TRACKER_COLUMNS, write_leads, read_leads, merge_leads, select_new,
)


class WriteReadTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.path = os.path.join(self.tmp, "leads.csv")

    def test_roundtrip_preserves_values(self):
        leads = [{
            "platform": "RemoteOK",
            "job_title": "Junior Backend Developer",
            "job_link": "https://remoteok.com/jobs/111",
            "fit_score": 90,
            "status": "New",
        }]
        write_leads(leads, self.path)
        back = read_leads(self.path)
        self.assertEqual(len(back), 1)
        self.assertEqual(back[0]["job_title"], "Junior Backend Developer")
        self.assertEqual(back[0]["fit_score"], "90")  # CSV reads back as text

    def test_header_is_full_schema(self):
        write_leads([], self.path)
        with open(self.path, newline="", encoding="utf-8") as fh:
            header = fh.readline().strip().split(",")
        self.assertEqual(header, TRACKER_COLUMNS)

    def test_ignores_extra_keys_and_blanks_missing(self):
        # "text" is a transient scoring field, not a tracker column -> dropped.
        # "company" is absent -> written as blank, not an error.
        leads = [{
            "platform": "RemoteOK",
            "job_title": "Dev",
            "job_link": "x",
            "text": "should not be written",
        }]
        write_leads(leads, self.path)
        row = read_leads(self.path)[0]
        self.assertNotIn("text", row)
        self.assertEqual(row["company"], "")


class MergeTests(unittest.TestCase):
    def test_dedupes_by_job_link(self):
        existing = [{"job_link": "a", "job_title": "Old A"}]
        new = [
            {"job_link": "a", "job_title": "Dupe A"},   # already tracked -> drop
            {"job_link": "b", "job_title": "Fresh B"},  # new -> keep
        ]
        merged = merge_leads(existing, new)
        links = [l["job_link"] for l in merged]
        self.assertEqual(links, ["a", "b"])
        # existing row is preserved, not overwritten by the duplicate
        a_row = next(l for l in merged if l["job_link"] == "a")
        self.assertEqual(a_row["job_title"], "Old A")

    def test_dedupes_within_new_batch(self):
        merged = merge_leads([], [
            {"job_link": "b", "job_title": "First"},
            {"job_link": "b", "job_title": "Second"},
        ])
        self.assertEqual(len(merged), 1)


class SelectNewTests(unittest.TestCase):
    def test_returns_only_leads_not_already_tracked(self):
        existing = [{"job_link": "a", "job_title": "Old A"}]
        new = [
            {"job_link": "a", "job_title": "Dupe A"},   # already tracked -> skip
            {"job_link": "b", "job_title": "Fresh B"},  # genuinely new -> keep
        ]
        fresh = select_new(existing, new)
        self.assertEqual([l["job_link"] for l in fresh], ["b"])
        self.assertEqual(fresh[0]["job_title"], "Fresh B")

    def test_collapses_duplicates_within_new_batch(self):
        fresh = select_new([], [
            {"job_link": "b", "job_title": "First"},
            {"job_link": "b", "job_title": "Second"},
        ])
        self.assertEqual(len(fresh), 1)
        self.assertEqual(fresh[0]["job_title"], "First")

    def test_empty_when_nothing_is_new(self):
        existing = [{"job_link": "a"}]
        self.assertEqual(select_new(existing, [{"job_link": "a"}]), [])


if __name__ == "__main__":
    unittest.main()
