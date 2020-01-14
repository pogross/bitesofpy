import pytest

from workouts import print_workout_days


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("sleep", "No matching workout"),
        ("upper", "Mon, Thu"),
        ("lower", "Tue, Fri"),
        ("cardio", "Wed"),
    ],
)
def test_print_workout_days(capfd, test_input, expected):
    print_workout_days(test_input)
    out, err = capfd.readouterr()
    assert expected in out
