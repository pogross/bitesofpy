from collections import Counter

import requests

CAR_DATA = "https://bit.ly/2Ov65SJ"

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


def most_prolific_automaker(year: int) -> str:
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    releases = [car["automaker"] for car in data if car["year"] == year]
    return Counter(releases).most_common(1)[0][0]


def get_models(automaker: str, year: int) -> set:
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    return {
        car["model"]
        for car in data
        if car["automaker"] == automaker and car["year"] == year
    }


if __name__ == "__main__":
    print(most_prolific_automaker(2008))
    print(get_models("Volkswagen", 2008))
