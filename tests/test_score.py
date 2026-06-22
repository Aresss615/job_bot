"""Tests for the M1 scoring engine (src/score.py).

Pure logic: no network, no file I/O. Run from the repo root with:

    python3 -m unittest tests.test_score
"""

import unittest

from src.score import keyword_filter, fit_score


class KeywordFilterTests(unittest.TestCase):
    def test_accepts_backend_lead(self):
        # Has a positive keyword (python, backend), no negatives -> keep.
        self.assertTrue(keyword_filter("Backend Python Developer (Django, REST API)"))

    def test_rejects_senior_react_lead(self):
        # React + frontend + senior are all negative keywords -> drop.
        self.assertFalse(keyword_filter("Senior React Frontend Engineer"))

    def test_rejects_lead_with_no_relevant_keywords(self):
        # No positive keyword present -> drop even though nothing negative.
        self.assertFalse(keyword_filter("Digital Marketing Manager"))

    def test_negative_keyword_overrides_positive(self):
        # Has python (positive) but also senior (negative) -> negative wins.
        self.assertFalse(keyword_filter("Senior Python Developer"))

    def test_is_case_insensitive(self):
        self.assertTrue(keyword_filter("AUTOMATION SPECIALIST (PHP, MYSQL)"))


class FitScoreTests(unittest.TestCase):
    def _backend_lead(self, **overrides):
        lead = {
            "text": "Junior Backend Python Developer, Django REST API, "
                    "remote part time contract",
            "salary_or_rate": "1500-2500 USD",
            "country_limit": "Philippines",
        }
        lead.update(overrides)
        return lead

    def test_returns_int_in_range(self):
        score = fit_score(self._backend_lead())
        self.assertIsInstance(score, int)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_strong_backend_lead_scores_high(self):
        # Junior, backend, flexible, PH-eligible, salaried -> strong target band.
        self.assertGreaterEqual(fit_score(self._backend_lead()), 85)

    def test_unclear_geography_scores_lower_than_ph_eligible(self):
        ph = fit_score(self._backend_lead(country_limit="Philippines"))
        unclear = fit_score(self._backend_lead(country_limit="Unclear"))
        self.assertLess(unclear, ph)

    def test_country_restricted_scores_lower_than_unclear(self):
        unclear = fit_score(self._backend_lead(country_limit="Unclear"))
        restricted = fit_score(self._backend_lead(country_limit="US-only"))
        self.assertLess(restricted, unclear)

    def test_unclear_geography_lands_in_mid_band(self):
        # No geography info should knock a lead out of the 85+ "strong" band.
        score = fit_score(self._backend_lead(country_limit="Unclear"))
        self.assertLess(score, 85)
        self.assertGreaterEqual(score, 55)

    def test_senior_role_scores_lower_than_junior(self):
        junior = fit_score(self._backend_lead(
            text="Junior Backend Python Developer remote"))
        senior = fit_score(self._backend_lead(
            text="Backend Python Developer, principal level, remote"))
        self.assertLess(senior, junior)

    def test_missing_salary_scores_lower_than_present(self):
        with_pay = fit_score(self._backend_lead(salary_or_rate="1500 USD"))
        without_pay = fit_score(self._backend_lead(salary_or_rate=""))
        self.assertLess(without_pay, with_pay)


if __name__ == "__main__":
    unittest.main()
