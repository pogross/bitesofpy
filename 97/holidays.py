import os
from collections import defaultdict
from datetime import datetime
from urllib.request import urlretrieve

from bs4 import BeautifulSoup

# prep data
holidays_page = os.path.join("tmp", "us_holidays.php")
urlretrieve("https://bit.ly/2LG098I", holidays_page)

with open(holidays_page) as f:
    content = f.read()

holidays = defaultdict(list)


def get_us_bank_holidays(content=content):
    """Receive scraped html output, make a BS object, parse the bank
       holiday table (css class = list-table), and return a dict of
       keys -> months and values -> list of bank holidays"""
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find("table", attrs={"class": "list-table"})
    table_body = table.find("tbody")

    rows = table_body.find_all("tr")
    for row in rows:
        cols = row.find_all("td")
        date = datetime.strptime(cols[1].time.attrs["datetime"], "%Y-%m-%d")
        holiday = cols[3].text.lstrip()[
            :-1
        ]  # just an odd workaround for the whitespaces :\

        holidays[str(date.month).zfill(2)].append(holiday)

    return holidays
