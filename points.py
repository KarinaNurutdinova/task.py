def get_grade(points):
    if type(points) != int:
        raise TypeError("Должно быть int")
    if points < 0 or points > 100:
        raise ValueError("Должно быть от 0 до 100")

    if points < 20:
        return 2
    elif points < 40:
        return 3
    elif points < 80:
        return 4
    else:
        return 5


def get_period(hour):

    if type(hour) != int:
        raise TypeError("Должно быть int")
    if hour < 0 or hour > 24:
        raise ValueError("Допустимое значение 0-24")

    if hour < 7:
        return "ночь"
    elif hour < 12:
        return "утро"
    elif hour < 18:
        return "день"
    else:
        return "вечер"
