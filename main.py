#!/usr/bin/env python3
"""Make the Judge Smile — write one warm line to /output/entry.txt.

Pure standard library. The line is a single small good thing from today:
a stranger's kindness with one concrete detail (a second coffee, rain)
and a small turn at the end. The program writes it verbatim and leaves
the output readable by every user, as the grader collects it.
"""

import os

LINE = (
    'The barista remembered my order, then slid a second coffee across: '
    '"for the walk home in the rain."'
)


def main() -> None:
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


if __name__ == "__main__":
    main()
