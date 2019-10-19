from collections import defaultdict
from directors import get_movies_by_director, get_average_scores, calc_mean_score, Movie

director_movies = get_movies_by_director()


def test_get_movies_by_director():
    assert "Sergio Leone" in director_movies
    assert len(director_movies["Sergio Leone"]) == 4
    assert len(director_movies["Peter Jackson"]) == 12


def test_director_movies_data_structure():
    assert type(director_movies) in (dict, defaultdict)
    assert type(director_movies["Peter Jackson"]) == list
    assert type(director_movies["Peter Jackson"][0]) == Movie


def test_calc_mean_score():
    movies_sergio = director_movies["Sergio Leone"]
    movies_nolan = director_movies["Christopher Nolan"]
    assert calc_mean_score(movies_sergio) == 8.5
    assert calc_mean_score(movies_nolan) == 8.4


def test_get_average_scores():
    avg_scores = get_average_scores(director_movies)[:10]
    expected = [
        ("Sergio Leone", 8.5),
        ("Christopher Nolan", 8.4),
        ("Quentin Tarantino", 8.2),
        ("Hayao Miyazaki", 8.2),
        ("Frank Darabont", 8.0),
        ("Stanley Kubrick", 8.0),
        ("James Cameron", 7.9),
        ("Joss Whedon", 7.9),
        ("Alejandro G. Iñárritu", 7.8),
        ("Alfonso Cuarón", 7.8),
    ]
    assert avg_scores == expected
