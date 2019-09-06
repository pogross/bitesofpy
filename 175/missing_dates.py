from datetime import date, timedelta


def get_missing_dates(dates):
    """Receives a range of dates and returns a sequence
       of missing datetime.date objects (no worries about order).

       You can assume that the first and last date of the
       range is always present (assumption made in tests).

       See the Bite description and tests for example outputs.
    """
    start_date, end_date = min(dates), max(dates)
    delta = end_date - start_date
    all_dates = {start_date + timedelta(days=x) for x in range(delta.days)}

    return all_dates - set(dates)
