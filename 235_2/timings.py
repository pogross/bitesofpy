import re
from collections import namedtuple
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path("tmp")
timings_log = tmp / "pytest_timings.out"
if not timings_log.exists():
    urlretrieve(
        "https://bites-data.s3.us-east-2.amazonaws.com/pytest_timings.out", timings_log
    )

Test = namedtuple("Test", "bite, amount, runtime")
PATTERN = re.compile(r"^(\d+).* (\d+) passed.*(\d+.\d+) seconds")


def _parse_log(logfile: Path = timings_log) -> list:
    with open(logfile, "r", encoding="utf-8") as f:
        return f.readlines()


def get_bite_with_fastest_avg_test(timings: list = _parse_log()) -> str:
    """Return the bite which has the fastest average time per test"""

    stats = []
    for line in timings:
        if "passed" in line:
            bite, amount, runtime = PATTERN.search(line).groups()
            stats.append(Test(int(bite), int(amount), float(runtime)))

    fastest_test = min(stats, key=lambda x: x.runtime / x.amount)
    return str(fastest_test.bite)
