"""Tests for the approval-packet generator (src/packet.py).

The packet is the approval-first guardrail in code: it renders the report's
fixed template, fills only what's known from the lead, and leaves every
human/AI-tailored part (resume changes, cover letter, the exact text to submit,
the submit action) as an explicit TODO. It must ALWAYS end at
"Status: Awaiting your approval" — packet.py never produces a submittable thing.

Run from the repo root with:

    python3 -m unittest tests.test_packet
"""

import unittest

from src.packet import REQUIRED_SECTIONS, render_packet


def _lead(**overrides):
    lead = {
        "platform": "RemoteOK",
        "job_title": "Junior Backend Developer",
        "company": "Acme Remote",
        "job_link": "https://remoteok.com/jobs/111",
        "fit_score": 90,
        "fit_reason": "",
        "risks_or_mismatch": "",
    }
    lead.update(overrides)
    return lead


class RenderPacketTests(unittest.TestCase):
    def test_includes_known_lead_fields(self):
        packet = render_packet(_lead())
        self.assertIn("https://remoteok.com/jobs/111", packet)
        self.assertIn("Acme Remote", packet)
        self.assertIn("RemoteOK", packet)
        self.assertIn("90", packet)

    def test_contains_all_required_sections(self):
        packet = render_packet(_lead())
        for label in REQUIRED_SECTIONS:
            self.assertIn(label, packet)

    def test_always_ends_awaiting_approval(self):
        packet = render_packet(_lead())
        self.assertTrue(packet.rstrip().endswith("Status: Awaiting your approval"))

    def test_human_fields_left_as_todo(self):
        packet = render_packet(_lead())
        # The tailored parts are not auto-written — they carry a TODO marker.
        self.assertIn("TODO", packet)

    def test_does_not_autofill_submission_text(self):
        # A guardrail: the exact-text-to-submit section must never contain real
        # generated content; it stays a placeholder until Jc fills it manually.
        packet = render_packet(_lead())
        submit_idx = packet.index("Exact final text to submit:")
        after = packet[submit_idx:]
        self.assertIn("TODO", after)

    def test_never_marks_approved(self):
        packet = render_packet(_lead())
        self.assertNotIn("Approved to Submit", packet)
        self.assertNotIn("approved_by_you: Yes", packet)

    def test_renders_without_optional_fields(self):
        # A lead straight from collect() has blank fit_reason/risks — still fine.
        minimal = {
            "platform": "WeWorkRemotely",
            "job_title": "Automation Developer",
            "company": "",
            "job_link": "https://weworkremotely.com/jobs/333",
            "fit_score": 75,
        }
        packet = render_packet(minimal)
        self.assertIn("https://weworkremotely.com/jobs/333", packet)
        self.assertTrue(packet.rstrip().endswith("Status: Awaiting your approval"))


if __name__ == "__main__":
    unittest.main()
