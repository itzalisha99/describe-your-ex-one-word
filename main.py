"""Describe Your Ex in One Word — make.fun entry.

Writes a single word to /output/entry.txt: the one-word verdict on an ex.
"""

import os

WORD = "Unsubscribe"


def validate(word):
    """Mirror the bounty gate: one word, 1-111 chars, not only whitespace."""
    if not isinstance(word, str):
        raise ValueError("entry must be text")
    if not word or word != word.strip():
        raise ValueError("entry must not be empty or padded with spaces")
    if len(word) > 111:
        raise ValueError("entry must be at most 111 characters")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main():
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
