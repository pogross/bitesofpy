from datetime import datetime

import pytz

MEETING_HOURS = range(6, 23)  # meet from 6 - 22 max
TIMEZONES = set(pytz.all_timezones)


def within_schedule(utc: datetime, *timezones):
    """Receive a utc datetime and one or more timezones and check if
       they are all within schedule (MEETING_HOURS)"""
    for timezone in timezones:
        if timezone not in TIMEZONES:
            raise ValueError

        curr_tz = pytz.timezone(timezone)
        utc_aware = pytz.utc.localize(utc)
        if utc_aware.astimezone(curr_tz).hour not in MEETING_HOURS:
            return False

    return True
