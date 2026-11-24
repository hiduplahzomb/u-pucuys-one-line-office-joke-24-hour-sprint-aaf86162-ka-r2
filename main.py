"""One-Line Office Joke: 24-Hour Sprint — KA entry (r2).

Writes a single-line office joke to entry.txt. Standard library only.
"""

import os
import sys

TEXT = (
    "Manager Dave fined 14 of us Rp50,000 each for laughing during his "
    "3-hour presentation, then spent the Rp700,000 on a plaque calling "
    "himself World's Funniest Boss."
)


def main() -> int:
    # Gate: non-empty, at most 200 characters, single line.
    if not TEXT.strip():
        print("gate failed: entry is empty", file=sys.stderr)
        return 1
    if len(TEXT) > 200:
        print(f"gate failed: entry is {len(TEXT)} characters (>200)", file=sys.stderr)
        return 1
    if "\n" in TEXT or "\r" in TEXT:
        print("gate failed: entry contains a newline", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)

    # Read back and verify byte-for-byte.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != TEXT:
        print("verification failed: entry.txt does not match TEXT", file=sys.stderr)
        return 1

    print(f"wrote {out_path} ({len(TEXT)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
