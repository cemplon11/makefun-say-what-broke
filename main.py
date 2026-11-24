#!/usr/bin/env python3
"""Say What Actually Broke — writes one honest error line to /output/entry.txt.

Pure Python stdlib, deterministic, no network. The line is a single
software error message of at most 200 characters that names the real
failure (a full disk), says what to do next, and is funny on one read.
"""

import os

LINE = "Upload failed: the file was fine, you were fine — our server ran out of disk because someone's been storing cat videos in /tmp since 2021. Try again in 10 minutes."


def main():
    assert 1 <= len(LINE) <= 200, "entry line must be 1 to 200 characters"
    assert LINE.strip(), "entry line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
