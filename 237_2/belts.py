import json
from pathlib import Path

from dateutil.parser import parse

SCORES = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
BELTS = ("white yellow orange green blue brown black " "paneled red").split()
TMP = Path("tmp")


def get_belts(data: str) -> dict:
    """Parsed the passed in json data:
       {"date":"5/1/2019","score":1},
       {"date":"9/13/2018","score":3},
       {"date":"10/25/2019","score":1},

       Loop through the scores in chronological order,
       determining when belts were achieved (use SCORES
       and BELTS).

       Return a dict with keys = belts, and values =
       readable dates, example entry:
       'yellow': 'January 25, 2018'
    """
    with open(data, "r") as f:
        raw_data = json.load(f)

    score_data = sorted(
        [(parse(entry["date"]), int(entry["score"])) for entry in raw_data],
        key=lambda x: x[0],
    )

    available_belts = list(zip(SCORES, BELTS))
    next_score, next_belt = available_belts.pop(0)

    total_score = 0
    belt_receptions = {}
    for score in score_data:
        total_score += score[1]

        if total_score >= next_score:
            nice_date = score[0].strftime("%B %d, %Y")
            belt_receptions[next_belt] = nice_date

            try:
                next_score, next_belt = available_belts.pop(0)
            except IndexError:
                break

    return belt_receptions
