from datetime import datetime, timedelta
import re

NOW = datetime(year=2019, month=2, day=6, hour=22, minute=0, second=0)


def add_todo(delay_time: str, task: str, start_time: datetime = NOW) -> datetime:
    """
    Add a todo list item in the future with a delay time.

    Parse out the time unit from the passed in delay_time str:
    - 30d = 30 days
    - 1h 10m = 1 hour and 10 min
    - 5m 3s = 5 min and 3 seconds
    - 45 or 45s = 45 seconds

    Return the task and planned time which is calculated from
    provided start_time (here default = NOW):
    >>> add_todo("1h 10m", "Wash my car")
    >>> "Wash my car @ 2019-02-06 23:10:00"
    """
    delays = re.findall(
        r"^(?!$)(?:(\d+)d[\s\n]?)?(?:(\d+)h[\s\n]?)?(?:(\d+)m[\s\n]?)?(?:(\d+)[\ss]?[\s\n]?)?$",
        delay_time,
    )[0]

    delay = {
        "days": int(delays[0]) if delays[0] else 0,
        "hours": int(delays[1]) if delays[1] else 0,
        "minutes": int(delays[2]) if delays[2] else 0,
        "seconds": int(delays[3]) if delays[3] else 0,
    }

    target_time = start_time + timedelta(**delay)
    return f"{task} @ {target_time:%Y-%m-%d %H:%M:%S}"
