#!/usr/bin/env python3
"""Write the office joke to the grader's output path."""

import os
from pathlib import Path

# One line, under 200 characters, with a turn at the end: the follow-up
# exists only to explain the original meeting.
JOKE = "I sent a 'quick question' and got a 47-minute meeting. The follow-up is a meeting about why we had a meeting."

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
