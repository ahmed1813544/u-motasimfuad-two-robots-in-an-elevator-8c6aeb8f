#!/usr/bin/env python3
"""Two Robots in an Elevator -- make.fun entry.

Writes one line of awkward robot-to-robot elevator small talk to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
Deterministic: the same line, byte for byte, on every run.
Standard library only.
"""

import os

LINE = "I simulated this elevator ride 4,000 times. I still have nothing to say to you."


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line outside the gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
