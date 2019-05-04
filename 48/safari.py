import os
import urllib.request
from collections import defaultdict, OrderedDict

LOG = os.path.join("tmp", "safari.logs")
PY_BOOK, OTHER_BOOK = "🐍", "."
urllib.request.urlretrieve("http://bit.ly/2BLsCYc", LOG)


def create_chart():
    chart = defaultdict(str)

    with open(LOG, "r") as f:
        log = f.readlines()

    for index, line in enumerate(log):
        if "sending" in line:
            day = line[:5]
            book = PY_BOOK if "python" in log[index - 1].lower() else OTHER_BOOK
            chart[day] += book

    for day, books in sorted(chart.items()):
        print(f"{day} {books}")

create_chart()
