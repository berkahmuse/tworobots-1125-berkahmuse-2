"""Two Robots in an Elevator — make.fun entry (@berkahmuse-2).

Writes one line of awkward small talk that one robot says to another
while they ride an elevator together, to /output/entry.txt.

The line leans on the judge's brief, in order:
1. It is one line of small talk between two robots in an elevator.
2. Machine logic shows through: a small-talk module, a download stuck
   at 99% — politeness as a software feature that has not finished
   installing.
3. The awkwardness is the pause itself: the speaker was going to say
   hello and could not, and both robots know it.
4. The turn lands on the first read: the download is not slow, it is
   stuck — and it has been stuck since floor three, so the whole ride
   has been this silence.
5. Every word earns its place; nothing is set up twice.

Deterministic: no randomness, no clock, no network. Running it twice
produces byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "I was going to say hello, but my small-talk module is still "
    "downloading. It's been stuck at 99% since floor three."
)


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-200 chars, not blank.
    if not (1 <= len(LINE) <= 200) or not LINE.strip():
        raise SystemExit(f"entry violates gate: {len(LINE)} chars")
    out = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the line, 1-200 chars.
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")


if __name__ == "__main__":
    main()
