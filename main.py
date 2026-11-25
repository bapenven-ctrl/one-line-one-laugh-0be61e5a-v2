#!/usr/bin/env python3
"""One Line, One Laugh - V2 entry.

Writes a single funny line to /output/entry.txt: agreeing to the terms
and conditions without reading them, and discovering in paragraph 47
that a goat is now owed to a company.

Deterministic: the same bytes on every run. No network, no dependencies
beyond the standard library. The output file is created mode 0644 via
os.open under umask 0o022; no permission-changing call is ever made on
/output or on the output file itself. The line is 113 code points, one
line, no trailing newline — exactly what the gate measures.
"""

import os

LINE = "I agreed to the terms and conditions without reading them. Somewhere in paragraph 47, I now owe a company a goat."
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.umask(0o022)
    fd = os.open(OUTPUT_PATH, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    try:
        os.write(fd, LINE.encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
