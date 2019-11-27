import re
from typing import Dict


def get_weekdays(calendar_output: str) -> Dict[int, str]:
    """Receives a multiline Unix cal output and returns a mapping (dict) where
       keys are int days and values are the 2 letter weekdays (Su Mo Tu ...)"""

    weekday_names = calendar_output.splitlines()[1].split()
    weeks = [re.findall(r"[0-9]+", line) for line in calendar_output.splitlines()[2:]]

    weekday_mapping = {
        int(day): weekday for week in weeks for day, weekday in zip(week, weekday_names)
    }

    return weekday_mapping
