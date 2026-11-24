#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line — an alien tourist's review of planet Earth —
to /output/entry.txt. The line is fixed text, at most 200 characters.
"""

import os

ENTRY = (
    "Brochure said 'pale blue dot.' Nobody mentioned the laundromat, "
    "the queue for the moon, or the dog that now owns my spare tentacle. "
    "5 stars \u2014 would abduct again."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
