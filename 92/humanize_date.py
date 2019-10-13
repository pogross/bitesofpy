from collections import namedtuple
from datetime import datetime, timedelta

TimeOffset = namedtuple("TimeOffset", "offset date_str divider")

NOW = datetime.now()
MINUTE, HOUR, DAY = 60, 60 * 60, 24 * 60 * 60
TIME_OFFSETS = (
    TimeOffset(10, "just now", None),
    TimeOffset(MINUTE, "{} seconds ago", None),
    TimeOffset(2 * MINUTE, "a minute ago", None),
    TimeOffset(HOUR, "{} minutes ago", MINUTE),
    TimeOffset(2 * HOUR, "an hour ago", None),
    TimeOffset(DAY, "{} hours ago", HOUR),
    TimeOffset(2 * DAY, "yesterday", None),
)


def pretty_date(date: datetime) -> str:
    """Receives a datetime object and converts/returns a readable string
       using TIME_OFFSETS"""
    if not isinstance(date, datetime) or date > NOW:
        raise ValueError

    delta = NOW - date
    if delta.days >= 2:
        return date.strftime("%m/%d/%y")

    for off in TIME_OFFSETS:
        if delta.total_seconds() < off.offset:
            try:
                return off.date_str.format(int(delta.total_seconds() / off.divider))
            except TypeError:
                return off.date_str.format(int(delta.total_seconds()))
