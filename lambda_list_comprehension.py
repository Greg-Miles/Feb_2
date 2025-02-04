
from marvel import full_dict

# Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return None

numbers_inp = input("Введите числа через пробел: ")
numbers = list(map(try_int, numbers_inp.split()))

print(numbers)