import re
from collections import namedtuple

import requests
from bs4 import BeautifulSoup

# feed = https://news.python.sc/, to get predictable results we cached
# first two pages - use these:
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index.html
# https://bites-data.s3.us-east-2.amazonaws.com/news.python.sc/index2.html

Entry = namedtuple("Entry", "title points comments")


def _create_soup_obj(url):
    """Need utf-8 to properly parse emojis"""
    resp = requests.get(url)
    resp.encoding = "utf-8"
    return BeautifulSoup(resp.text, "html.parser")


def get_top_titles(url, top=5):
    """Parse the titles (class 'title') using the soup object.
       Return a list of top (default = 5) titles ordered descending
       by number of points and comments.
    """
    soup = _create_soup_obj(url)

    titles = soup.findAll("span", attrs={"class": "title"})
    points = soup.findAll("span", attrs={"class": "controls"})

    entries = [
        Entry(
            title=t.text.strip(),
            points=int(re.search(r"(\d{1,}) point", p.text).group(1)),
            comments=int(re.search(r"(\d{1,}) comment", p.text).group(1)),
        )
        for t, p in zip(titles, points)
    ]

    entries_ranking = sorted(
        entries, key=lambda x: (x.points, x.comments), reverse=True
    )

    return entries_ranking[:top]
