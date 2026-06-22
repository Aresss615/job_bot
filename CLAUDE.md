# CLAUDE.md - Job Finder / Apply Agent

Operating notes for Claude Code sessions in THIS repo. The global manual and the
single source of truth about Jc and his projects live in `~/knowledge` — read
`~/knowledge/INDEX.md` first, then `~/knowledge/projects/job-bot.md` (this
project's owner file) before major advice.

## Source of truth
- Global facts about Jc / this project: `~/knowledge` (owner file:
  `projects/job-bot.md`). It OVERRIDES conversation memory.
- This project's own state: the repo docs below beat the global docs for
  anything project-specific.

## Project docs (keep synchronized)
- Tier 3 project — no ROADMAP/DECISIONS/ARCHITECTURE trio yet. If this grows
  into a Tier 1 build, run `pdocs init` to create the trio; until then keep
  status in the owner file.

## Commits and staging (manual only)
- Commits are MANUAL. Never commit on Jc's behalf; never auto-commit.
- `git push` only when Jc asks. Never push unsolicited.
- One short (~50-char) imperative subject line. No AI/Co-Authored-By attribution.

## How Jc works
- He vibecodes; rusty across the board, barely any JS, no React. Give full
  working code and explain it. See `~/knowledge/preference.md` for full detail.
- Be direct; no blind agreement. TDD is the standard: failing test first, verify
  by running before claiming done.

## Project-specific rules
- Approval-first: never auto-submit applications, send messages, or take account
  actions. Automation is ONLY for collecting public leads via official
  feeds/APIs that explicitly permit it. Respect each platform's ToS (LinkedIn,
  Indeed, Wellfound prohibit scraping/bot apply).
- Only surface new, verified leads.
