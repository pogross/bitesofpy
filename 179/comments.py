import re


def strip_comments(code: str):
    # see Bite description
    singleline_stripped = re.sub(r"^\s*#.*\n", "", code, flags=re.MULTILINE)
    inline_stripped = re.sub(
        r"\s{2}# .*\n", "", singleline_stripped, flags=re.MULTILINE
    )
    docstring_stripped = re.sub(
        r"^\s*\"{3}[\s\S]*?\"{3}\n", "", inline_stripped, flags=re.MULTILINE
    )

    return docstring_stripped
