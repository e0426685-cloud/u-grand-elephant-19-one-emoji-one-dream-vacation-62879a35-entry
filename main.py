"""One Emoji, One Dream Vacation.

Entry: a single desert-island emoji, standing in for the trip of
our dreams.

Why this emoji: the brief asks for one emoji that most makes a
stranger want to book the flight. A desert island is the postcard
itself -- sun, sand, palm, open sea, nowhere to be. It lands on
"dream vacation" at a glance (a faraway place, not a generic
holiday), it is specific rather than generic (one island, not any
trip), and it reads instantly at any size on any screen, in any
culture. No words, no second emoji, nothing else.

The program writes exactly that emoji to /output/entry.txt. The
gate requires UTF-8 text of 1 to 8 characters, not only white
space, so the entry is validated before it is written: it must be
one emoji (a single code point plus its variation selector), 1-8
characters, and non-blank. Validation happens before any file is
touched, so a bad entry fails loudly instead of writing junk.
Only the Python standard library is used, and the file is written
with plain open() plus an explicit chmod 0644 so the grader can
read it.
"""

import os

EMOJI = "\U0001F3DD\uFE0F"  # 🏝️ desert island


def validate_entry(text):
    """Check the entry meets the gate: 1-8 chars, not blank, one emoji."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 8:
        raise ValueError("entry must be 1 to 8 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only white space")
    # Exactly one emoji: one base pictograph code point, optionally
    # followed by U+FE0F (variation selector-16, emoji presentation).
    # Stripping the selector first means the base alone must be a
    # single pictograph; anything longer or outside that range fails.
    base = text.rstrip("\uFE0F")
    if len(base) != 1 or not (0x1F000 <= ord(base) <= 0x1FAFF):
        raise ValueError("entry must be exactly one emoji")
    return text


def main():
    entry = validate_entry(EMOJI)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
