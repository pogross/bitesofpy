def extract_non_ascii_words(text):
    """Filter a text returning a list of non-ascii words"""
    words = text.split()
    return [word for word in words if any(ord(c) > 127 for c in word)]
