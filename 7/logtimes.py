"""Extract datetimes from log entries and calculate the time
   between the first and last shutdown events"""
from datetime import datetime
import os
import urllib.request
import re

SHUTDOWN_EVENT = "Shutdown initiated"

# prep: read in the logfile
logfile = os.path.join("tmp", "log")
urllib.request.urlretrieve("http://bit.ly/2AKSIbf", logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:


def convert_to_datetime(line):
    """TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)"""
    time = [int(value) for value in re.findall(r"[0-9]\d*", line)]
    return datetime(*time)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object."""
    shutdown_times = [
        convert_to_datetime(line) for line in loglines if SHUTDOWN_EVENT in line
    ]

    return shutdown_times[-1] - shutdown_times[0]
