import pytest

from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize("data, expected", [([1, 7, 5], 175), ([0, 3, 1, 2], 312)])
def test_valid_input(data, expected):
    assert list_to_decimal(data) == expected


def test_not_int():
    with pytest.raises(TypeError):
        list_to_decimal([1, "two", 2, 3, 4])


@pytest.mark.parametrize("data", [[1, 7, 10], [1, 5, 42]])
def test_not_in_range(data):
    with pytest.raises(ValueError):
        list_to_decimal(data)
