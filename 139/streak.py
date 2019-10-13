import re
from datetime import date, datetime, timedelta
from itertools import tee

TODAY = date(2018, 11, 12)

# https://docs.python.org/3/library/itertools.html
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def consecutive(curr: date, nxt: date, step: timedelta = timedelta(days=1)) -> bool:
    return (curr + step) == nxt


def extract_dates(data: str) -> list:
    """Extract unique dates from DB table representation as shown in Bite"""
    date_strings = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", data)
    return sorted(
        {datetime.strptime(d, "%Y-%m-%d").date() for d in date_strings}, reverse=True
    )


def calculate_streak(dates: list) -> int:
    """Receives sequence (set) of dates and returns number of days
       on coding streak.

       Note that a coding streak is defined as consecutive days coded
       since yesterday, because today is not over yet, however if today
       was coded, it counts too of course.

       So as today is 12th of Nov, having dates 11th/10th/9th of Nov in
       the table makes for a 3 days coding streak.

       See the tests for more examples that will be used to pass your code.
    """
    # does streak even start?
    if TODAY - dates[0] > timedelta(days=1):
        return 0

    # streak started! count consecutive days
    streak_days = 1
    for curr_date, next_date in pairwise(dates):
        if consecutive(next_date, curr_date):
            streak_days += 1
        else:  # streak broken
            return streak_days

    return streak_days
