import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "test_input, expected", [(15, "Fizz Buzz"), (3, "Fizz"), (5, "Buzz"), (1, 1)]
)
def test_fizzbuzz(test_input, expected):
    assert fizzbuzz(test_input) == expected
