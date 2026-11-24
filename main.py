#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes one sentence (<=200 chars) explaining the modern internet to a
time traveler from 1800, using only words a person of that year could
know: a road, a library, a letter, tea. No post-1800 coinages.
"""

import os

SENTENCE = (
    "Picture a road that joins every house on earth to one great library, "
    "where a letter you send is answered while your tea is still warm."
)


def main() -> None:
    text = SENTENCE.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
