import unicodedata


def filter_accents(text):
    """Return a sequence of accented characters found in
       the passed in lowercased text string
    """
    return [
        char.lower() for char in text if unicodedata.normalize("NFKD", char) != char
    ]
