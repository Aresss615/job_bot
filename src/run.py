"""CLI runner: wire the tested core to the live feeds and the tracker.

This is the I/O boundary — it fetches from the network and reads/writes the CSV.
All real logic lives in the unit-tested modules (score, collect, tracker,
packet); this file only orchestrates them, so it's verified by running it, not
by unit tests.

Usage (from the repo root, inside the venv):

    .venv/bin/python -m src.run collect          # fetch -> score -> merge into CSV
    .venv/bin/python -m src.run list             # show tracked leads by score
    .venv/bin/python -m src.run packet <job_link>  # print an approval packet

Only Remote OK + We Work Remotely are fetched (the two ToS-permitted feeds).
Nothing is ever submitted: `packet` stops at "Awaiting your approval".
"""

from __future__ import annotations

import argparse
import os
import sys
from datetime import datetime, timezone

from src.collect import fetch_remoteok, fetch_wwr, collect_leads
from src.tracker import read_leads, merge_leads, write_leads
from src.packet import render_packet

DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "leads.csv")


def _as_int(value) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


def cmd_collect(_args) -> int:
    os.makedirs(DATA_DIR, exist_ok=True)
    today = datetime.now(timezone.utc).date().isoformat()

    print("Fetching Remote OK + We Work Remotely ...")
    remoteok = fetch_remoteok()
    wwr = fetch_wwr()
    fresh = collect_leads(remoteok, wwr, date_found=today)

    existing = read_leads(CSV_PATH) if os.path.exists(CSV_PATH) else []
    merged = merge_leads(existing, fresh)
    added = len(merged) - len(existing)
    write_leads(merged, CSV_PATH)

    print(f"Collected {len(fresh)} relevant leads; {added} new, "
          f"{len(merged)} total in {CSV_PATH}.")
    top = sorted(fresh, key=lambda l: _as_int(l.get("fit_score")), reverse=True)[:5]
    if top:
        print("\nTop fresh leads this run:")
        for lead in top:
            print(f"  [{lead.get('fit_score')}] {lead.get('job_title')} "
                  f"— {lead.get('company') or lead.get('platform')}\n"
                  f"       {lead.get('job_link')}")
    return 0


def cmd_list(_args) -> int:
    if not os.path.exists(CSV_PATH):
        print(f"No tracker yet at {CSV_PATH}. Run `collect` first.")
        return 1
    rows = sorted(read_leads(CSV_PATH),
                  key=lambda l: _as_int(l.get("fit_score")), reverse=True)
    print(f"{len(rows)} leads in {CSV_PATH} (highest fit first):\n")
    for lead in rows:
        print(f"  [{lead.get('fit_score'):>3}] {lead.get('status'):<10} "
              f"{lead.get('job_title')} — {lead.get('company') or lead.get('platform')}")
        print(f"        {lead.get('job_link')}")
    return 0


def cmd_packet(args) -> int:
    if not os.path.exists(CSV_PATH):
        print(f"No tracker yet at {CSV_PATH}. Run `collect` first.")
        return 1
    rows = read_leads(CSV_PATH)
    match = next((r for r in rows if r.get("job_link") == args.job_link), None)
    if match is None:
        print(f"No lead with job_link {args.job_link!r}. Try `list`.")
        return 1
    print(render_packet(match))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="job_bot", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("collect", help="fetch feeds, score, merge into the tracker")
    sub.add_parser("list", help="show tracked leads sorted by fit score")

    p_packet = sub.add_parser("packet", help="print an approval packet for a lead")
    p_packet.add_argument("job_link", help="the job_link of the lead (see `list`)")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    handlers = {"collect": cmd_collect, "list": cmd_list, "packet": cmd_packet}
    return handlers[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
