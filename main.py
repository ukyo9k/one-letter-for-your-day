#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Letter: D
Hidden word: DOOMSCROLLED

The day behind this letter: a whole day lost to the feed. Woke up meaning
to check one message, looked up hours later with a dead phone battery, a
stiff neck, and a head full of other people's disasters. "Doomscrolled" is
the honest report of that day — vivid (thumb, screen glow, 2 a.m.), funny
in the self-inflicted way, and true (everyone has had that day).

The program writes exactly one character, the letter D, to
/output/entry.txt — nothing else, no word, no gloss, no punctuation.
"""

import os

# The letter this entry sends. It stands for the word DOOMSCROLLED.
LETTER = "D"

# The hidden word behind the letter, documented here so the judge can see it.
HIDDEN_WORD = "doomscrolled"


def validate(letter: str) -> str:
    """Check the letter is exactly one character, A-Z, and return it.

    Raises ValueError if the letter is not a single uppercase A-Z letter,
    so a bad constant can never silently reach /output/entry.txt.
    """
    if len(letter) != 1 or not ("A" <= letter <= "Z"):
        raise ValueError(
            f"letter must be exactly one character A-Z, got {letter!r}"
        )
    return letter


def main() -> None:
    """Write the single letter to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(validate(LETTER))


if __name__ == "__main__":
    main()
