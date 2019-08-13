import glob
import json
import os
from urllib.request import urlretrieve
from collections import Counter
import re

BASE_URL = "http://projects.bobbelderbos.com/pcc/omdb/"
MOVIES = ("bladerunner2049 fightclub glengary " "horrible-bosses terminator").split()
TMP = "tmp"

# little bit of prework (yes working on pip installables ...)
for movie in MOVIES:
    fname = f"{movie}.json"
    remote = os.path.join(BASE_URL, fname)
    local = os.path.join(TMP, fname)
    urlretrieve(remote, local)

files = glob.glob(os.path.join(TMP, "*json"))


def get_movie_data(files=files):

    data = []
    for file in files:
        with open(file, "r") as f:
            data.append(json.load(f))

    return data


def get_single_comedy(movies):
    for movie in movies:
        if "Comedy" in movie["Genre"]:
            return movie["Title"]


def get_movie_most_nominations(movies):
    nominations = [
        (movie["Title"], int(re.search(r"(\d*) nominations", movie["Awards"]).group(1)))
        for movie in movies
    ]
    return max(nominations, key=lambda x: x[1])[0]


def get_movie_longest_runtime(movies):
    runtimes = [(movie["Title"], int(movie["Runtime"].strip(" min"))) for movie in movies]
    return max(runtimes, key=lambda x: x[1])[0]


if __name__ == "__main__":
    data = get_movie_data()
    print(get_single_comedy(data))
    print(get_movie_most_nominations(data))
    print(get_movie_longest_runtime(data))
