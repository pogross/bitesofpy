def common_languages(programmers: dict):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    lang_sets = [set(languages) for languages in programmers.values()]
    return set.intersection(*lang_sets)
