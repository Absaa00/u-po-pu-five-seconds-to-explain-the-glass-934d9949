#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes one sentence -- what the cat says in the five seconds after
sweeping a glass off the table, in the cat's own voice -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

No network, no randomness, no arguments: every run produces the exact
same bytes.
"""

import os

SENTENCE = (
    "The glass had been leaning dangerously toward the edge for hours, "
    "so my paw simply conducted a routine gravity inspection "
    "-- a public service, really."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = SENTENCE.strip()
    assert 1 <= len(text.encode("utf-8")) <= 200, "entry must be 1-200 UTF-8 chars"
    assert text and not text.isspace(), "entry must not be blank"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
