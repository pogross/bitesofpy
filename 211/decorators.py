from functools import wraps

MAX_RETRIES = 3


class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        for tried in range(1, MAX_RETRIES + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
        else:
            raise MaxRetriesException

    return wrapper
