from itertools import tee
from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = "white yellow orange green blue brown black paneled red".split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def get_belt(user_score):

    if user_score < MIN_SCORE:
        return None
    if user_score >= MAX_SCORE:
        return belts[-1]

    for first, second in pairwise(HONORS.keys()):
        if user_score >= first and user_score < second:
            return HONORS[first]
