# Job Finder / Apply Agent

An approval-first agent that finds and surfaces part-time/remote jobs matching Jc's profile — free platforms only, applications stay manual.

- Status: see ~/knowledge/projects/job-bot.md (owner file for status, tier, scope)
- Created: 2026-06-22

## What it is

A semi-automated job-lead pipeline. It collects new, verified leads from a
narrow set of free, Philippines-eligible sources, then leaves application,
messaging, and account actions to Jc. Automation is limited to gathering public
leads via official feeds/APIs (Remote OK's public JSON API); submitting
applications is manual by design.

See `deep-research-report.md` for the full platform analysis and strategy.

## Getting started

Python 3, stdlib-first core; only the live fetch needs two packages.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python -m src.run collect              # fetch -> score -> merge into data/leads.csv
python -m src.run list                 # show tracked leads by fit score
python -m src.run packet <job_link>    # print an approval packet (stops at "Awaiting approval")
python -m unittest discover -s tests   # 43 tests, stdlib unittest
```

`collect` pulls only Remote OK (public JSON API). Nothing is ever applied to or
submitted.

### Email digest (optional)

If `SMTP_USER`, `SMTP_PASS`, and `DIGEST_TO` are set, `collect` emails the newly
found leads. With Gmail, use an [App Password](https://myaccount.google.com/apppasswords),
not your account password. Unset, it just writes the CSV and prints the top leads.

### Scheduled deployment

`.github/workflows/collect.yml` runs `collect` daily (01:00 UTC ≈ 09:00 PHT) on
GitHub Actions, even when your laptop is off. It emails new leads and commits the
refreshed `data/leads.csv` back so dedup state persists. Set the three SMTP values
as repository **Secrets** (Settings → Secrets and variables → Actions).

## Structure

- `src/` — pipeline code (lead collection, normalization, output)
- `config.example` — copy to `config` (gitignored) and fill in per-platform settings
- `deep-research-report.md` — strategy + ranked platform comparison

## Docs

- `CLAUDE.md` - how Claude Code should work in this repo

Source of truth about the project lives at `~/knowledge/projects/job-bot.md`.
