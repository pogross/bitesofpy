import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve

BASE_URL = "http://projects.bobbelderbos.com/pcc/movies/"
TMP = "tmp"

fname = "movie_metadata.csv"
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple("Movie", "title year score")


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""
    director_movies = defaultdict(list)

    with open(os.path.join(MOVIE_DATA), newline="", encoding="UTF-8") as csvfile:
        for row in csv.DictReader(csvfile):
            year_string = row["title_year"].strip()
            year = int(year_string) if year_string else 0
            if year > MIN_YEAR:
                title, score = str(row["movie_title"]).strip(), float(row["imdb_score"])
                movie = Movie(title, year, score)
                director_movies[row["director_name"].strip()].append(movie)

    return director_movies


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    scores = [movie.score for movie in movies]
    mean_score = sum(scores) / len(scores)
    return round(mean_score, 1)


def get_average_scores(directors=get_movies_by_director()):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    directors_ranking = []
    for director, movies in directors.items():
        if len(movies) >= MIN_MOVIES:
            director_rank = (director, calc_mean_score(movies))
            directors_ranking.append(director_rank)

    return sorted(directors_ranking, key=lambda x: x[1], reverse=True)
