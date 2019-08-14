import csv
from collections import Counter

import requests

CSV_URL = "https://bit.ly/2HiD2i8"


def get_csv() -> csv.DictReader:
    """Use requests to download the csv and return the
       decoded content"""

    response = requests.get(CSV_URL)
    if response.status_code == 200:
        wrapper = csv.DictReader(response.text.strip().split("\n"))
    else:
        raise FileNotFoundError("CSV File could not be downloaded")

    return wrapper


def create_user_bar_chart(content: csv.DictReader) -> None:
    """Receives csv file (decoded) content and returns a table of timezones
       and their corresponding member counts in pluses (see Bite/tests)"""
    tz_count = Counter([entry["tz"] for entry in content])

    for region, count in sorted(list(tz_count.items())):
        print(f"{region:21}| {'+' * count}")


if __name__ == "__main__":
    csv_file = get_csv()
    create_user_bar_chart(csv_file)
