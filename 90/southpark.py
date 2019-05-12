from collections import Counter, defaultdict
import csv

import requests

CSV_URL = "https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv"  # noqa E501


def get_season_csv_file(season: int) -> str:
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode("utf-8")


def get_num_words_spoken_by_character_per_episode(content: str):
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""
    reader = csv.DictReader(content.splitlines())
    character_words = defaultdict(Counter)
    for row in reader:
        character_words[row["Character"]][row["Episode"]] += len(row["Line"].split())
    return character_words

if __name__ == "__main__":
    print(get_num_words_spoken_by_character_per_episode(get_season_csv_file(1)))