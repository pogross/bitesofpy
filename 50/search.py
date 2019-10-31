from collections import namedtuple
from datetime import date
from dateutil.parser import parse
import time
from typing import List
from operator import attrgetter

import feedparser

FEED = "https://bites-data.s3.us-east-2.amazonaws.com/all.rss.xml"

Entry = namedtuple("Entry", "date title link tags")


def _convert_struct_time_to_dt(stime: time.struct_time) -> date:
    """Convert a time.struct_time as returned by feedparser into a
    datetime.date object, so:
    time.struct_time(tm_year=2016, tm_mon=12, tm_mday=28, ...)
    -> date(2016, 12, 28)
    """
    return date(stime.tm_year, stime.tm_mon, stime.tm_mday)


def _get_tags(tags: dict) -> List[str]:
    return [tag["term"].strip().lower() for tag in tags]


def get_feed_entries(feed: str = FEED) -> List[Entry]:
    """Use feedparser to parse PyBites RSS feed.
       Return a list of Entry namedtuples (date = date, drop time part)
    """
    return [
        Entry(parse(e["published"]).date(), e["title"], e["link"], _get_tags(e["tags"]))
        for e in feedparser.parse(feed)["entries"]
    ]


def filter_entries_by_tag(search: str, entry: Entry) -> bool:
    """Check if search matches any tags as stored in the Entry namedtuple
       (case insensitive, only whole, not partial string matches).
       Returns bool: True if match, False if not.
       Supported searches:
       1. If & in search do AND match,
          e.g. flask&api should match entries with both tags
       2. Elif | in search do an OR match,
          e.g. flask|django should match entries with either tag
       3. Else: match if search is in tags
    """
    if "&" in search:
        terms = search.lower().split("&")
        return all(term in entry.tags for term in terms)

    if "|" in search:
        terms = search.lower().split("|")
        return any(term in entry.tags for term in terms)

    return search.lower() in entry.tags


def main():
    """Entry point to the program
       1. Call get_feed_entries and store them in entries
       2. Initiate an infinite loop
       3. Ask user for a search term:
          - if enter was hit (empty string), print 'Please provide a search term'
          - if 'q' was entered, print 'Bye' and exit/break the infinite loop
       4. Filter/match the entries (see filter_entries_by_tag docstring)
       5. Print the title of each match ordered by date ascending
       6. Secondly, print the number of matches: 'n entries matched'
          (use entry if only 1 match)
    """
    entries = sorted(get_feed_entries(), key=attrgetter("date"))

    while True:
        search_term = input("Search for (q for exit): ")

        if not search_term:
            print("Please provide a search term")
            continue
        if search_term == "q":
            print("Bye")
            break

        result = [
            entry for entry in entries if filter_entries_by_tag(search_term, entry)
        ]

        for entry in result:
            print(f"{entry.date} | {entry.title}")

        sp = "entry" if len(result) == 1 else "entries"
        print(f'{len(result)} {sp} matched "{search_term}"')


if __name__ == "__main__":
    main()
