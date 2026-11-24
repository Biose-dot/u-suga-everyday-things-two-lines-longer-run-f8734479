#!/usr/bin/env python3
"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes two lines to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt):
line 1 explains one everyday thing to a 10-year-old in a single vivid
sentence built on an analogy; line 2 says in one sentence why that
analogy works: what it maps and what it leaves out.
"""
import os

ENTRY = (
    "A toaster is a tiny sunbathing bed for bread, where two glowing bars tan both sides at once until the bread pops up like it has had enough of the sun.\n"
    "It works because heat browns bread the way the sun browns skin, but it leaves out that the sun never ejects you with a spring when you are done."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()
