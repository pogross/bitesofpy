from datetime import datetime

from dateutil.parser import parse

# work with a static date for tests, real use = datetime.now()
NOW = datetime(2019, 3, 17, 16, 28, 42, 966663)
WEEKS_PER_YEAR = 52


def get_number_books_read(books_per_year_goal: int, at_date: str = None) -> int:
    """Based on books_per_year_goal and at_date, return the
       number of books that should have been read.
       If books_per_year_goal negative or 0, or at_date is in the
       past, raise a ValueError."""
    at_date = at_date or str(NOW)
    dt = parse(at_date)

    if books_per_year_goal <= 0 or dt < NOW:
        raise ValueError("Should have positive goal and future date")

    weeks_passed = dt.isocalendar()[1]
    books_per_week = books_per_year_goal / WEEKS_PER_YEAR

    return int(weeks_passed * books_per_week)
