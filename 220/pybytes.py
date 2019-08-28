import re
from collections import namedtuple, Counter
from typing import NamedTuple

import feedparser

SPECIAL_GUEST = "Special guest"

# using _ as min/max are builtins
Duration = namedtuple("Duration", "avg max_ min_")

# static copy, original: https://pythonbytes.fm/episodes/rss
URL = "http://projects.bobbelderbos.com/pcc/python_bytes"
IGNORE_DOMAINS = {
    "https://pythonbytes.fm",
    "http://pythonbytes.fm",
    "https://twitter.com",
    "https://training.talkpython.fm",
    "https://talkpython.fm",
    "http://testandcode.com",
}


class PythonBytes:
    def __init__(self, url=URL):
        """Load the feed url into self.entries using the feedparser module."""
        self.entries = feedparser.parse(url)["entries"]

    def get_episode_numbers_for_mentioned_domain(self, domain: str) -> list:
        """Return a list of episode IDs (itunes_episode attribute) of the
           episodes the pass in domain was mentioned in.
        """
        mentions = [
            entry["itunes_episode"]
            for entry in self.entries
            if domain in entry["summary_detail"]["value"]
        ]
        return mentions

    def get_most_mentioned_domain_names(self, n: int = 15) -> list:
        """Get the most mentioned domain domains. We match a domain using
           regex: "https?://[^/]+" - make sure you only count a domain once per
           episode and ignore domains in IGNORE_DOMAINS.
           Return a list of (domain, count) tuples (use Counter).
        """
        counter = Counter()
        for entry in self.entries:
            summary = entry["summary_detail"]["value"]
            domains = {
                domain
                for domain in re.findall(r"https?://[^/]+", summary)
                if domain not in IGNORE_DOMAINS
            }
            counter.update(domains)

        return counter.most_common(n)

    def number_episodes_with_special_guest(self) -> int:
        """Return the number of episodes that had one of more special guests
           featured (use SPECIAL_GUEST).
        """
        special_guest_eps = [
            entry["itunes_episode"]
            for entry in self.entries
            if SPECIAL_GUEST in entry["summary_detail"]["value"]
        ]
        return len(special_guest_eps)

    def get_average_duration_episode_in_seconds(self) -> NamedTuple:
        """Return the average duration in seconds of a Python Bytes episode, as
           well as the shortest and longest episode in hh:mm:ss notation.
           Return the results using the Duration namedtuple.
        """
        durations = sorted([entry["itunes_duration"] for entry in self.entries])

        total = 0
        for duration in durations:
            h, m, s = duration.split(":")
            total += int(h) * 3600 + int(m) * 60 + int(s)

        return Duration(int(total / len(durations)), durations[-2], durations[0])
