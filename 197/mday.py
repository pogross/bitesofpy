from datetime import date
import calendar


def get_mothers_day_date(year):
    """Given the passed in year int, return the date Mother's Day
       is celebrated assuming it's the 2nd Sunday of May."""
    c = calendar.Calendar(firstweekday=calendar.MONDAY)

    second_week = c.monthdatescalendar(year, 5)[1]  # must be in the second week
    mothers_day = [day for day in second_week if day.weekday() == 6][
        0
    ]  # find sunday in the first week

    return date(year, 5, mothers_day.day)
