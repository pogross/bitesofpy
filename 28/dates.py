import os
import re
from collections import Counter
from datetime import datetime
from typing import List
from urllib.request import urlretrieve

from dateutil.parser import parse

BASE_URL = "http://projects.bobbelderbos.com/pcc/dates/"
RSS_FEED = "all.rss.xml"
PUB_DATE = re.compile(r"<pubDate>(.*?)</pubDate>")
TMP = "tmp"


def _get_dates():
    """Downloads PyBites feed and parses out all pub dates returning
       a list of date strings, e.g.: ['Sun, 07 Jan 2018 12:00:00 +0100',
       'Sun, 07 Jan 2018 11:00:00 +0100', ... ]"""
    remote = os.path.join(BASE_URL, RSS_FEED)
    local = os.path.join(TMP, RSS_FEED)
    urlretrieve(remote, local)

    with open(local) as f:
        return PUB_DATE.findall(f.read())


def convert_to_datetime(date_str: str) -> datetime:
    """Receives a date str and convert it into a datetime object"""
    return parse(date_str)


def get_month_most_posts(dates: List[datetime]) -> str:
    """Receives a list of datetimes and returns the month (format YYYY-MM)
       that occurs most"""
    counter = Counter([date.strftime("%Y-%m") for date in dates])
    return counter.most_common(1)[0][0]
