import pytest
from utils import double, sum_two


@pytest.mark.parametrize(
    "test_input, expected",
    [(0, 0), (1, 2), (10.0, 20.0), (-3, -6), (123456789, 246913578)]
)
def test_double(test_input, expected):
    assert double(test_input) == expected


@pytest.mark.parametrize("first, second, expected",
                 [(0, 0, 0), (1, 1, 2), (-10, 10, 0)])
def test_sum_two(first, second, expected):
    assert sum_two(first, second) == expected