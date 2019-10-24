import sys
import unicodedata


START_EMOJI_RANGE = 100000  # estimate


def what_means_emoji(emoji: str) -> str:
    """Receives emoji and returns its meaning,
       in case of a TypeError return 'Not found'"""
    try:
        return unicodedata.name(emoji)
    except TypeError:
        return "Not found"


def _make_emoji_mapping() -> dict:
    """Helper to make a mapping of all possible emojis:
       - loop through range(START_EMOJI_RANGE, sys.maxunicode +1)
       - return dict with keys=emojis, values=names"""
    emojis = {}
    for i in range(START_EMOJI_RANGE, sys.maxunicode + 1):
        try:
            emojis[chr(i)] = unicodedata.name(chr(i)).lower()
        except ValueError:
            pass
    return emojis


def find_emoji(term: str) -> None:
    """Return emojis and their texts that match (case insensitive)
       term, print matches to console"""
    term = term.lower()
    emoji_mapping = _make_emoji_mapping()

    for emoji, name in emoji_mapping.items():
        if term in name:
            print(f"{name.strip().title():>42} | {emoji}")
    else:
        print("no matches")
