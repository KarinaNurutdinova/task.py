import pytest
from points import get_grade, get_period

grade = [(10, 2), (30, 3), (40, 4), (100, 5)]


@pytest.mark.parametrize("points, expected", grade)
def test_grade(points, expected):
    assert get_grade(points) == expected


time_information = [(6, "ночь"), (7, "утро"), (10, "утро"), (15, "день")]


@pytest.mark.parametrize("hour, expected", time_information)
def test_time_information(hour, expected):
    assert get_period(hour) == expected
