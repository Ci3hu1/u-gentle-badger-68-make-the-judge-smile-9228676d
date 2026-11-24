#!/usr/bin/env python3
"""Make the Judge Smile — write one warm line to /output/entry.txt.

Pure standard library. The line is a single small good thing from today:
a stranger's kindness with one concrete detail (a second coffee, rain)
and a small turn at the end. The program writes it verbatim and leaves
the output readable by every user, as the grader collects it.
"""

import os
from pathlib import Path

LINE = (
    'The barista remembered my order, then slid a second coffee across: '
    '"for the walk home in the rain."'
)


def validate(line: str) -> str:
    """Check the entry line against the sealed gate before writing it.

    The gate wants exactly one line, 1-200 characters, not only
    whitespace, with no line breaks or control characters. Returns the
    line unchanged so callers can chain it.
    """
    stripped = line.strip()
    if not stripped:
        raise ValueError("entry line must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry line must be 1-200 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entry line must not contain control characters")
    return line


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    # The grader collects outputs as another user: leave the file readable.
    os.chmod(path, 0o644)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    # Self-check: the file must hold exactly the line, nothing else.
    if Path(path).read_text(encoding="utf-8") != LINE + "\n":
        raise ValueError("entry file does not hold exactly the line")


if __name__ == "__main__":
    main()
