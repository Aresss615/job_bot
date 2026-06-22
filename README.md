# Job Finder / Apply Agent

An approval-first agent that finds and surfaces part-time/remote jobs matching Jc's profile — free platforms only, applications stay manual.

- Status: see ~/knowledge/projects/job-bot.md (owner file for status, tier, scope)
- Created: 2026-06-22

## What it is

A semi-automated job-lead pipeline. It collects new, verified leads from a
narrow set of free, Philippines-eligible sources, then leaves application,
messaging, and account actions to Jc. Automation is limited to gathering public
leads via official feeds/APIs (e.g. We Work Remotely RSS, Remote OK JSON);
submitting applications is manual by design.

See `deep-research-report.md` for the full platform analysis and strategy.

## Getting started

```
# Stack not chosen yet — record the choice in a DECISIONS entry when it lands.
```

Required later: per-platform config/credentials (kept out of git — see
`.gitignore` and `config.example`).

## Structure

- `src/` — pipeline code (lead collection, normalization, output)
- `config.example` — copy to `config` (gitignored) and fill in per-platform settings
- `deep-research-report.md` — strategy + ranked platform comparison

## Docs

- `CLAUDE.md` - how Claude Code should work in this repo

Source of truth about the project lives at `~/knowledge/projects/job-bot.md`.
