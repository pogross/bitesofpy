import csv
import re
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

tmp = Path("tmp")
stats = tmp / "bites.csv"

if not stats.exists():
    urlretrieve("https://bit.ly/2MQyqXQ", stats)


def get_most_complex_bites(N: int = 10, stats: Path = stats) -> List[int]:
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with open(stats) as f:
        lines = f.readlines()

    # regex: 1) number preeceded by a dot / 2) all chars between semicolon and line end
    bite_ratings = [
        (int(re.search(r"(\d*)\.", line).group(1)), float(re.search(r";(.*?)$", line).group(1)))
        for line in lines[1:]  # skip header
        if "None" not in line  # skip None
    ]

    bite_nr_sorted = [bite[0] for bite in sorted(bite_ratings, key=lambda x: x[1], reverse=True)]

    return bite_nr_sorted[:N]


if __name__ == "__main__":
    res = get_most_complex_bites()
    print(res)
