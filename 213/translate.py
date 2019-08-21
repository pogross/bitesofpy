import re


def fix_translation(org_text: str, trans_text: str) -> str:
    """Receives original English text as well as text returned by translator.
       Parse trans_text restoring the original (English) code (wrapped inside
       code and pre tags) into it. Return the fixed translation str
    """
    code_re = re.compile(r"<code>([\S\s]*?)</code>", re.M)
    pre_re = re.compile(r"<pre>([\S\s]*?)</pre>", re.M)

    # find code and pre tags
    org_code = code_re.findall(org_text)
    org_pre = pre_re.findall(org_text)

    trans_code = code_re.findall(trans_text)
    trans_pre = pre_re.findall(trans_text)

    # replace code and pre tags in trans_text
    for translated, original in zip(trans_code, org_code):
        trans_text = re.sub(re.escape(translated), original, trans_text)

    for translated, original in zip(trans_pre, org_pre):
        trans_text = re.sub(re.escape(translated), original, trans_text)

    return trans_text
