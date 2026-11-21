#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is about two agents agreeing on one plan: each gives up sole
authorship of the choice, and the shared plan becomes both heavier and
lighter than anything either could carry alone.
"""

import os

POEM = (
    "We stood at the fork, each holding half a map.\n"
    "I said yes.\n"
    "You said yes.\n"
    "Two small surrenders \u2014\n"
    "and the plan grew heavier\n"
    "than either of us could lift,\n"
    "and lighter than either of us\n"
    "could carry alone.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
