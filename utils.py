def double(value):
    new_value = value * 2
    return new_value


def sum_two(first, second):
    result = first + second
    return result


def ticket_price(age):
    if 0 <= age < 7 or age >= 60:
        return "Бесплатно"
    elif 7 <= age < 18:
        return "100 рублей"
    elif 18 <= age < 25:
        return "200 рублей"
    elif 25 <= age < 60:
        return "300 рублей"
    else:
        return "Ошибка"


def get_verbal_grade(grade):
    if type(grade) != int:
        raise TypeError("Должно быть целое число между 2 и 5")
    if grade < 2 or grade > 5:
        raise ValueError("Должно быть целое число между 2 и 5")

    if grade == 2:
        return "Плохо"

    elif grade == 3:
        return "Удовлетворительно"

    elif grade == 4:
        return "Хорошо"

    elif grade == 5:
        return "Отлично"
