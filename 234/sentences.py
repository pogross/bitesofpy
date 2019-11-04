import re


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""
    pattern = re.compile(r".*?[.!\?]")
    return " ".join(line.strip().capitalize() for line in pattern.findall(text))
