from datetime import date

from dateutil.rrule import DAILY, FR, MO, TH, TU, WE, rrule

TODAY = date(year=2018, month=11, day=29)


def get_hundred_weekdays(start_date=TODAY):
    """Return a list of hundred date objects starting from
       start_date up till 100 weekdays later, so +100 days
       skipping Saturdays and Sundays"""
    days = rrule(DAILY, dtstart=start_date, count=100, byweekday=(MO, TU, WE, TH, FR))
    return [dt.date() for dt in days]
