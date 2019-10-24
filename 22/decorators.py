from functools import wraps


def make_html(element):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{element}>{result}</{element}>"

        return wrapper

    return inner
