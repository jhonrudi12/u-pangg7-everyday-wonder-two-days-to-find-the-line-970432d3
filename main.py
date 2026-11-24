#!/usr/bin/env python3
"""Everyday Wonder, Two Days to Find the Line.

Writes a single sentence (at most 200 characters) about a small moment
of wonder in everyday life to /output/entry.txt.
"""

import os

ENTRY = "My neighbour renamed their Wi-Fi 'good luck, kid', and for a moment the whole building felt like it was quietly rooting for me."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.count(".") <= 1, "entry must be a single sentence"
    out_dir = "/output" if os.path.isdir("/output") else "output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to {out_dir}/entry.txt")


if __name__ == "__main__":
    main()
