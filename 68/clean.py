from string import punctuation


def remove_punctuation(input_string: str):
    """Return a str with punctuation chars stripped out"""
    return "".join(char for char in input_string if char not in punctuation)
