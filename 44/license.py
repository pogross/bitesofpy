from secrets import choice
from string import ascii_uppercase, digits

CHARS = list(ascii_uppercase + digits)


def gen_key(parts=4, chars_per_part=8):
    key_parts = [
        "".join([choice(CHARS) for char in range(chars_per_part)])
        for part in range(parts)
    ]
    return "-".join(key_parts)
