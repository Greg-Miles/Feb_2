
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

numbers2 = [int(number) if number.isdigit() else None for number in numbers_inp.split()]
print(numbers2)

# 3. Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.


#Противоречивое задание, как-будто подразумевался список словарей, включающих id и все остальные ключи.
#


filtered_dict = dict(filter(lambda movies: isinstance(movies[0], int) and movies[0] in numbers, full_dict.items()))
print(filtered_dict)

