import pytest
from utils import *


sum_of_two_parameters = [(0, 0, 0), (1, 1, 2), (-10, 10, 0)]


@pytest.mark.parametrize("first, second, expected", sum_of_two_parameters)
def test_sum_of_two_parameters(first, second, expected):
    assert sum_two(first, second) == expected


age_parameters = [(0, "Бесплатно", "Ошибка для 0 лет"),
                  (1, "Бесплатно", "Ошибка для 1 лет"),
                  (7, "100 рублей", "Ошибка для 7 лет"),
                  (18, "200 рублей", "Ошибка для 18 лет"),
                  (25, "300 рублей", "Ошибка для 25 лет"),
                  (60, "Бесплатно", "Ошибка для 60 лет"),
                  (0.5, "Бесплатно", "Ошибка для 0.5 лет"),
                  (-1, "Ошибка", "Ошибка для -1 лет")]


@pytest.mark.parametrize("age, expected, error", age_parameters)
def test_ticket(age, expected, error):
    assert ticket_price(age) == expected


grade_parameters = [(2, "Плохо"),
    (3, "Удовлетворительно"),
    (4, "Хорошо"),
    (5, "Отлично")
]


@pytest.mark.parametrize("grade_int, grade_str", grade_parameters)
def test_grade_verbal_grade(grade_int, grade_str):
    assert get_verbal_grade(grade_int) == grade_str
