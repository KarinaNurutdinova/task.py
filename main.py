def bad_round(x):
    return int(x)

assert bad_round(0) == 0 , "Ошибка округления 0"
assert bad_round(1.1) == 1, "Ошибка округления 1.1"


assert bad_round(100.1) == 100 , "Ошибка округления 100"