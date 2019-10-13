from datetime import date

from dateutil.relativedelta import relativedelta

START_DATE = date(2018, 11, 1)
MIN_DAYS_TO_COUNT_AS_MONTH = 10
MONTHS_PER_YEAR = 12


def _total_months(delta: relativedelta):
    return delta.years * MONTHS_PER_YEAR + delta.months


def calc_months_passed(year: int, month: int, day: int) -> int:
    """Construct a date object from the passed in arguments.
       If this fails due to bad inputs reraise the exception.
       Also if the new date is < START_DATE raise a ValueError.

       Then calculate how many months have passed since the
       START_DATE constant. We suggest using dateutil.relativedelta!

       One rule: if a new month is >= 10 (MIN_DAYS_TO_COUNT_AS_MONTH)
       days in, it counts as an extra  month.

       For example:
       date(2018, 11, 10) = 9 days in => 0 months
       date(2018, 11, 11) = 10 days in => 1 month
       date(2018, 12, 11) = 1 month + 10 days in => 2 months
       date(2019, 12, 11) = 1 year + 1 month + 10 days in => 14 months
       etc.

       See the tests for more examples.

       Return the number of months passed int.
    """
    try:
        future_date = date(year, month, day)
    except TypeError:
        raise TypeError("Wrong input parameters")

    if future_date < START_DATE:
        raise ValueError("Future date is earlier than start date")

    delta = relativedelta(future_date, START_DATE)
    if delta.days >= MIN_DAYS_TO_COUNT_AS_MONTH:
        return _total_months(delta) + 1

    return _total_months(delta)
