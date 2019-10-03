import calendar
from datetime import datetime


def weekday_of_birth_date(date: datetime):
    """Takes a date object and returns the corresponding weekday string"""
    return calendar.day_name[date.weekday()]
