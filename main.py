"""One Star, Written in Sap — a one-line 1-star review from a houseplant.

Writes the review to /output/entry.txt. Deterministic: one fixed string,
stdlib only, no randomness, no time, no network.
"""

import os
import sys

REVIEW = (
    "One star. He waters me like he's apologising to a plant he already "
    "killed, then acts shocked when I drop a leaf on his laptop mid-meeting, "
    "as if I'm the embarrassing one."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 279
    # characters, not only white space, on a single line. Fail loudly here
    # instead of shipping an entry the gate would refuse.
    text = REVIEW.strip()
    if not 1 <= len(text) <= 279:
        print(f"entry is {len(text)} chars, gate needs 1-279", file=sys.stderr)
        return 1
    if "\n" in text or not text.strip():
        print("entry must be one non-blank line", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(REVIEW)
    return 0


if __name__ == "__main__":
    sys.exit(main())
