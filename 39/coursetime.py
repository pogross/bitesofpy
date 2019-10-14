import os
import re
import urllib.request
from datetime import datetime, timedelta

# getting the data
COURSE_TIMES = os.path.join("tmp", "course_timings")
urllib.request.urlretrieve("http://bit.ly/2Eb0iQF", COURSE_TIMES)


def get_all_timestamps():
    """Read in the COURSE_TIMES and extract all MM:SS timestamps.
       Here is a snippet of the input file:

       Start  What is Practical JavaScript? (3:47)
       Start  The voice in your ear (4:41)
       Start  Is this course right for you? (1:21)
       ...

        Return a list of MM:SS timestamps
    """
    with open(COURSE_TIMES, "r", encoding="utf-8") as f:
        text = f.read()

    return re.findall(r"\d{1,}:\d{2}", text)


def calc_total_course_duration(timestamps=get_all_timestamps()):
    """Takes timestamps list as returned by get_all_timestamps
       and calculates the total duration as HH:MM:SS"""
    durations = [
        timedelta(minutes=dt.minute, seconds=dt.second)
        for dt in [datetime.strptime(ts, "%M:%S") for ts in timestamps]
    ]
    return str(sum(durations, timedelta()))
