import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    return re.search(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", text)


def is_integer(number):
    """Return True if number is an integer"""
    return isinstance(number, int)


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    return re.search(r"\w-\w", text)


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    return re.sub(r"\s*\(.*?\)", "", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    return list(filter(None, re.split(r"[?!.,;]\s*", text)))


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    return re.sub(r"(\s{2,})", " ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    return re.search(r"([aeiou]{3})", word.lower())


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    return re.sub(r"(\d{2})/(\d{2})/(\d{4})", r"\g<2>/\g<1>/\g<3>", date)
