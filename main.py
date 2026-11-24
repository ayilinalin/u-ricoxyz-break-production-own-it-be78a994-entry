#!/usr/bin/env python3
"""Entry for make.fun competition u-ricoxyz-break-production-own-it-be78a994.

Writes one brutally honest postmortem line to
$MAKEFUN_OUTPUT_DIR/entry.txt (else /output/entry.txt).
Deterministic, stdlib only, no network, no wall clock.
"""

import os
import sys

ENTRY = "I deleted the production database to save disk space. It worked — the database is gone, and so is your weekend."


def main() -> int:
    # Gate self-check: one line, 1-200 characters.
    if not (1 <= len(ENTRY) <= 200) or "\n" in ENTRY or not ENTRY.strip():
        sys.stderr.write("entry fails the 1-200 character gate\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
