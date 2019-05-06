IGNORE_CHAR = "b"
QUIT_CHAR = "q"
MAX_NAMES = 5


def filter_names(names):
    count = 1
    for name in names:
        has_digit = any(char.isdigit() for char in name)
        if name.startswith(IGNORE_CHAR) or has_digit:
            continue
        elif name.startswith(QUIT_CHAR) or count > MAX_NAMES:
            break

        count = count + 1
        yield name
