from functools import lru_cache


@lru_cache(maxsize=None)
def cached_fib(n):
    if n < 2:
        return n
    return cached_fib(n - 1) + cached_fib(n - 2)
