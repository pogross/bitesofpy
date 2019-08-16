import os
import re
from collections import Counter
from urllib.request import urlretrieve

from dateutil.parser import parse

commits = os.path.join("tmp", "commits")
urlretrieve("https://bit.ly/2H1EuZQ", commits)

# you can use this constant as key to the yyyymm:count dict
YEAR_MONTH = "{y}-{m:02d}"


def get_min_max_amount_of_commits(commit_log: str = commits, year: int = None) -> (str, str):
    """
    Calculate the amount of inserts / deletes per month from the
    provided commit log.

    Takes optional year arg, if provided only look at lines for
    that year, if not, use the entire file.

    Returns a tuple of (least_active_month, most_active_month)
    """
    counter = Counter()
    with open(commit_log, "r") as f:
        log_lines = f.readlines()

    for line in log_lines:

        date = parse(re.search(r"Date:   (.*) \|", line).group(1))
        if year and date.year != year:
            continue

        insertions = re.findall(r"(\d*) insertion.*", line)
        deletions = re.findall(r"(\d*) deletion.*", line)
        changes = insertions + deletions

        total_changes = sum([int(change) for change in changes if change != ""])
        counter[f"{date.year}-{date.month:02d}"] += total_changes

    return counter.most_common()[-1][0], counter.most_common()[0][0]


if __name__ == "__main__":
    get_min_max_amount_of_commits(commits, year=2017)
