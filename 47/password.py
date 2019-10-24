import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set("PassWord@1 PyBit$s9".split())


def validate_password(password):

    pattern = re.compile(
        # lowercase alphabetical, uppercase alphabetical, numeric, special character,
        # 6-12 length
        r"^(?=.*[a-z]{2,})(?=.*[A-Z])(?=.*[0-9])(?=.*[\~\!\@\#\$\%\^\&\*\(\)\_\+\=\-\`\>\<\_])(?=.{6,12})"
    )

    if pattern.match(password) and password not in used_passwords:
        used_passwords.add(password)
        return True

    return False
