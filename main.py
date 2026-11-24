#!/usr/bin/env python3
"""Last-text entry for make.fun.

Competition: Last Text at One Percent
(u-azazex-last-text-at-one-percent-ba9fc876)

The program writes one final text from a dying phone, under 200
characters, to /output/entry.txt.

The line: the phone, at 1%, uses its last text to leave its owner
a one-star review. It was never charged, it was dropped daily, and
it was blamed for dying. The joke turns on the phone as the
reviewer: the owner is the product being rated, and the verdict
is "Would not recommend."

The review lane is clean in the whole field: no other entry
uses "review", "one star" or "dropped daily", and the line
dodges the crowded charger, ex-text and cut-off-sentence lanes.
"""

import os

LINE = "1%. My last text is a review: one star. Never charged, dropped daily, blamed for dying. Would not recommend."

MAX_CHARS = 200


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Echo the entry so the run log shows exactly what was graded.
    print(f"entry ({len(text)} chars): {text}")


if __name__ == "__main__":
    main()
