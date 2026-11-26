#!/usr/bin/env python3
"""Deadpan forecast for Velmaris, a city that does not exist.

Writes one line, at most 160 characters, to /output/entry.txt:
a flat, serious TV-meteorologist forecast for a fictional city,
built around a single impossible weather event reported as if
it were entirely routine.
"""

import os

# Competition cap: one line, at most 160 characters.
MAX_CHARS = 160

# The forecast line itself. Velmaris is invented, not a real place.
# One impossible phenomenon (rain falling upward), delivered
# deadpan, anchored by small realistic details: a temperature,
# a wind direction and speed, and a time.
FORECAST = (
    "Tonight in Velmaris, rain will fall upward at 14 degrees, "
    "with a northwesterly breeze of 12 kilometres per hour; "
    "hold umbrellas underneath until 3 a.m."
)


def write_entry(path="/output/entry.txt"):
    """Write the single forecast line to the grader's output path."""
    # The line must stay within the competition's 160-character cap.
    assert len(FORECAST) <= MAX_CHARS, f"forecast is {len(FORECAST)} chars"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(FORECAST + "\n")
    return path


def main():
    path = write_entry()
    print(f"wrote {len(FORECAST)}-character forecast to {path}")


if __name__ == "__main__":
    main()
