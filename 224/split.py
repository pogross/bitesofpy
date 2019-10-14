import re


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""
    sentences = re.sub(r"\s+", " ", text).replace("\n", "").strip()
    # Magic happens!
    # https://www.sitepoint.com/community/t/choose-whole-sentences-and-only-whole-sentences-reliably-with-regex/8075
    pattern = re.compile(
        r'["’]?[A-Z][^.?!]+((?![.?!][’"]?\s["’]?[A-Z][^.?!]).)+[.?!’"]+', re.M
    )
    return [sentence.group(0) for sentence in pattern.finditer(sentences)]
