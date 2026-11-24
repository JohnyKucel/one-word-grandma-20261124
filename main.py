#!/usr/bin/env python3
"""One Word From Grandma.

Pick the single word a grandma would text about AI, then write exactly
that one word to /output/entry.txt.

The judge compares two words at a time and picks the funnier, more
grandma-like one. Its criteria, most important first: the word reads as
the single word a grandma would text about AI; it sounds like a real
grandmother's texting voice, warm and a little baffled; it is funny in
one word; it feels tied to AI, robots or machines; it is a fresh pick,
still instantly readable. The rules bless a typo she would actually make.

Ten fresh candidates, each scored 0-5 on originality, funny/touching,
grandma theme, exact RULES format (one word, 1-30 chars), and natural
English. The winner is the grandma typo "computor": the computer with
its "e" dropped, exactly how a baffled grandma texts about the machine
that thinks. It beats the classic picks on freshness (the typo twist the
rules explicitly bless), ties them on warmth and humour, and is far less
likely than "chatterbox" or "knowitall" to be byte-identical to one of
the 2,486 entries already in the field.
"""

CANDIDATES = [
    # word,         original, funny, theme, format, english
    ("computor",    5, 5, 5, 5, 4),
    ("chatterbox",  4, 5, 5, 5, 5),
    ("knowitall",   4, 5, 5, 5, 5),
    ("smartypants", 3, 5, 5, 5, 5),
    ("thinkbox",    5, 4, 4, 5, 5),
    ("egghead",     4, 4, 4, 5, 5),
    ("whatsit",     3, 4, 5, 5, 5),
    ("witchcraft",  3, 4, 4, 5, 5),
    ("clanky",      4, 4, 3, 5, 5),
    ("chatgbt",     5, 4, 4, 5, 3),
]

OUTPUT_PATH = "/output/entry.txt"


def score(candidate):
    return sum(candidate[1:])


def validate(word):
    """Mirror the sealed gate: UTF-8 text of 1 to 30 characters, not only
    whitespace, exactly one word, no punctuation tricks."""
    assert isinstance(word, str)
    assert 1 <= len(word) <= 30, f"length {len(word)} outside 1-30"
    assert word.strip() == word and word.strip(), "blank or padded"
    assert len(word.split()) == 1, "must be exactly one word"
    assert word.isalpha() and word.islower(), "one plain lowercase word"
    word.encode("utf-8")
    return True


def choose(candidates):
    # Highest total wins; ties break toward the fresher pick (higher
    # originality), then the shorter word, matching the judge's order.
    ranked = sorted(
        candidates,
        key=lambda c: (score(c), c[1], -len(c[0])),
        reverse=True,
    )
    return ranked[0], ranked


def main():
    best, ranked = choose(CANDIDATES)
    word = best[0]
    validate(word)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(word)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    assert written == word, f"expected {word!r}, wrote {written!r}"
    validate(written)
    for entry in ranked:
        print(f"{entry[0]:<12} score={score(entry)}")
    print(f"picked {word} -> {OUTPUT_PATH} ({len(written)} bytes)")


if __name__ == "__main__":
    main()
