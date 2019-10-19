import pytest

from scores import Player, calculate_score, get_winner


def test_calculate_score():
    assert calculate_score([1, 3, 2, 5]) == 5
    assert calculate_score([1, 4, 2, 5]) == 9
    assert calculate_score([1, 1, 1, 1]) == 0
    assert calculate_score([4, 5, 1, 2]) == 9
    assert calculate_score([6, 6, 5, 5]) == 22


def test_calculate_score_negative_numbers_raises_exception():
    with pytest.raises(ValueError):
        calculate_score([4, -5, -1, 2])


def test_calculate_score_non_int_raises_exception():
    with pytest.raises(ValueError):
        calculate_score([4, 5, 6, "a"])


def test_calculate_score_str_raises_exception():
    with pytest.raises(ValueError):
        calculate_score([4, -5, 6, 2])


def test_winner_3_players():
    players = [
        Player(name="player 1", scores=[1, 3, 2, 5]),
        Player(name="player 2", scores=[1, 1, 1, 1]),
        Player(name="player 3", scores=[4, 5, 1, 2]),  # max 9
    ]
    assert get_winner(players) == players[-1]


def test_winner_shorter_score_len_raises_exception():
    players = [
        Player(name="player 1", scores=[4, 3, 5, 5]),
        Player(name="player 2", scores=[4, 4, 6]),  # lacks one score
        Player(name="player 3", scores=[4, 5, 6, 6]),
    ]
    with pytest.raises(ValueError):
        get_winner(players)


def test_winner_longer_score_len_raises_exception():
    players = [
        Player(name="player 1", scores=[4, 3, 5, 5, 4]),
        Player(name="player 2", scores=[4, 4, 6, 6, 3, 2]),  # 1 more
        Player(name="player 3", scores=[4, 5, 6, 6, 5]),
    ]
    with pytest.raises(ValueError):
        get_winner(players)
