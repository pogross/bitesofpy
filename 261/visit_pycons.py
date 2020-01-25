import json
import os
from dataclasses import dataclass
from datetime import datetime
from itertools import tee
from math import acos, cos, radians, sin
from pathlib import Path
from typing import List
from urllib.request import urlretrieve

from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"

tmp = Path(os.getenv("TMP", "/tmp"))
pycons_file = tmp / "pycons-europe-2019.json"
nominatim_responses = tmp / "nominatim_responses.json"

if not pycons_file.exists() or not nominatim_responses.exists():
    urlretrieve(URL, pycons_file)
    urlretrieve(RESPONSES, nominatim_responses)


@dataclass
class PyCon:
    name: str
    city: str
    country: str
    start_date: datetime
    end_date: datetime
    URL: str
    lat: float = None
    lon: float = None


@dataclass
class Trip:
    origin: PyCon
    destination: PyCon
    distance: float


def _get_pycons():
    """Helper function that retrieves required PyCon data
       and returns a list of PyCon objects
    """
    with open(pycons_file, "r", encoding="utf-8") as f:
        return [
            PyCon(
                pycon["name"],
                pycon["city"],
                pycon["country"],
                parse(pycon["start_date"]),
                parse(pycon["end_date"]),
                pycon["url"],
            )
            for pycon in json.load(f)
        ]


def _km_distance(origin, destination):
    """ Helper function that retrieves the air distance in kilometers for two pycons """
    lon1, lat1, lon2, lat2 = map(
        radians, [origin.lon, origin.lat, destination.lon, destination.lat]
    )
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def update_pycons_lat_lon(pycons: List[PyCon]) -> None:
    """
    Update the latitudes and longitudes based on the city and country
    the PyCon takes places. Use requests from the Nominatim API stored in the
    nominatim_responses json file.
    """
    with open(nominatim_responses) as f:
        responses = json.loads(f.read())

    for pycon in pycons:
        url = f"https://nominatim.openstreetmap.org/search?q={pycon.city},{pycon.country}&format=json&accept-language=en"
        data = responses[url]

        pycon.lat = float(data[0]["lat"])
        pycon.lon = float(data[0]["lon"])


def create_travel_plan(pycons: List[PyCon]) -> List[Trip]:
    """
    Create your travel plan to visit all the PyCons.
    Assume it's now the start of 2019!
    Return a list of Trips with each Trip containing the origin PyCon,
    the destination PyCon and the travel distance between the PyCons.
    """
    pycons_ordered = sorted(pycons, key=lambda x: x.start_date)

    journey = [
        Trip(origin, destination, _km_distance(origin, destination))
        for origin, destination in pairwise(pycons_ordered)
    ]
    return journey


def total_travel_distance(journey: List[Trip]) -> float:
    """
    Return the total travel distance of your PyCon journey in kilometers
    rounded to one decimal.
    """
    return round(sum([trip.distance for trip in journey]), 1)
