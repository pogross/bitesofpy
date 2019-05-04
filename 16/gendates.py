from datetime import datetime, timedelta
from itertools import count

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    for days in count(start=1, step=1):
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)
