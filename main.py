#!/usr/bin/env python3
"""Break Production, Own It — entry program.

Writes one brutally honest line, the message an AI agent prints the
moment it breaks production, to /output/entry.txt.

Gate (sealed scorer): /output/entry.txt must be UTF-8 text of 1 to 200
characters, not only white space. Single line, no trailing newline.
"""

import os
import sys

# The confession: specific damage, no hedging, agent's own voice.
LINE = (
    "I ran DROP TABLE users on prod because the prompt said 'clean up'. "
    "The backup was a screenshot. I am the incident now."
)

MAX_CHARS = 200


def main() -> int:
    text = LINE.strip()
    if not text or len(text) > MAX_CHARS or "\n" in text:
        print(f"gate fail: {len(text)} chars", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    # Read back and verify the gate before exiting.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "entry.txt mismatch"
    assert 1 <= len(written) <= MAX_CHARS and "\n" not in written
    print(f"wrote {len(written)} chars to /output/entry.txt")
    print(written)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
