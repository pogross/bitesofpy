from datetime import datetime
import json
import os
from pathlib import Path
from urllib.request import urlretrieve

import pytest

from zodiac import (
    get_signs,
    get_sign_with_most_famous_people,
    signs_are_mutually_compatible,
    get_sign_by_date,
)

# original source: https://zodiacal.herokuapp.com/api
URL = "https://bites-data.s3.us-east-2.amazonaws.com/zodiac.json"
TMP = os.getenv("TMP", "/tmp")
PATH = Path(TMP, "zodiac.json")


@pytest.fixture(scope="module")
def signs():
    if not PATH.exists():
        urlretrieve(URL, PATH)
    with open(PATH) as f:
        data = json.loads(f.read())
    return get_signs(data)


def test_nametuple(signs):
    assert type(signs[0]).__name__ == "Sign"


def test_get_sign_with_most_famous_people(signs):
    assert get_sign_with_most_famous_people(signs) == ("Scorpio", 35)
    assert not get_sign_with_most_famous_people(signs) == ("Pisces", 24)
    assert get_sign_with_most_famous_people(signs[:5]) == ("Gemini", 33)


@pytest.mark.parametrize(
    "sign1, sign2, expected",
    [
        ("Taurus", "Aries", False),
        ("Taurus", "Capricorn", True),
        ("Taurus", "Aquarius", False),
        ("Taurus", "Cancer", True),
    ],
)
def test_signs_are_mutually_compatible(signs, sign1, sign2, expected):
    assert signs_are_mutually_compatible(signs, sign1, sign2) == expected


@pytest.mark.parametrize(
    "date, expected",
    [
        (datetime(year=2019, month=3, day=20), "Pisces"),
        (datetime(year=2019, month=3, day=21), "Aries"),
        (datetime(year=2019, month=4, day=19), "Aries"),
        (datetime(year=2019, month=4, day=20), "Taurus"),
        (datetime(year=2019, month=5, day=21), "Gemini"),
    ],
)
def test_get_sign_by_date(signs, date, expected):
    assert get_sign_by_date(signs, date) == expected
