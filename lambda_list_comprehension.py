
from marvel import full_dict
import typing
import pprint

#2. Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.

def try_int(x):
    """
    Вариант встроенной функции int который возвращает None вместо выпадения в ошибку если обьект нельзя привести к int
    :param x: объект для перевода в число
    :return: int или None 
    """
    try:
        return int(x)
    except ValueError:
        return None

numbers_inp = input("Введите числа через пробел: ")
numbers: list = list(map(try_int, numbers_inp.split()))

print('\n Задание №2 \n')
pprint.pp(numbers)

# numbers2 = [int(number) if number.isdigit() else None for number in numbers_inp.split()]
# print(numbers2)


# 3. Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.

#Противоречивое задание, как-будто подразумевался список словарей, включающих id и все остальные ключи.
# Что-то типа такого:
# filtered_list = list(filter(lambda movie: isinstance(movie['id'], int) and movie['id'] in numbers, [{'id': key, **value} for key, value in full_dict.items()]))
# print(filtered_list)

filtered_dict: dict = dict(filter(lambda movies: isinstance(movies[0], int) and movies[0] in numbers, full_dict.items()))

print('\n Задание №3 \n')
pprint.pp(filtered_dict, sort_dicts=False)


#4. Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.

set_of_directors: set = {full_dict[id]['director'] for id in full_dict}

print('\n Задание №4 \n')
pprint.pp(set_of_directors)


#5. С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку. **(Опционально)**

full_dict_copy: dict = {key:{**value, 'year': str(value['year'])} for key, value in full_dict.items()}

print('\n Задание №5 \n')
pprint.pp(full_dict_copy, sort_dicts=False)
print()
pprint.pp(type(full_dict_copy[0]['year']))


#6. Используйте `filter`, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву `Ч`.

ch_movies: dict = dict(filter(lambda movie: movie[1].get('title') and movie[1]['title'][0].lower()== 'ч', full_dict.items()))

print('\n Задание №6 \n')
pprint.pp(ch_movies, sort_dicts=False)


#7. Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку.

# Пусть будет 'title':

sorted_by_title: dict = dict(sorted(full_dict.items(), key = lambda movie: movie[1]['title'] if movie[1].get('title') else ''))

print('\n Задание №7 \n')
pprint.pp(sorted_by_title, sort_dicts=False)


#8. Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.

# Пусть будут 'title' и 'year':

sorted_by_title_again: dict = dict(sorted(full_dict.items(), key = lambda movie: movie[1]['title'] if movie[1].get('title') else ''))

sorted_by_title_and_year: dict = dict(sorted(sorted_by_title_again.items(), 
    key = lambda movie: movie[1]['year'] if movie[1].get('year') 
    and isinstance(movie[1]['year'], int) else 0 ))

print('\n Задание №8 \n')
pprint.pp(sorted_by_title_and_year, sort_dicts=False)


#9. Напишите однострочник, который отфильтрует и отсортирует `full_dict` с использованием `filter` и `sorted`.

# не надо такие вещи делать однострочником)))

filtered_sorted_dict: dict = dict(
    sorted(
        filter(lambda movie: movie[0]<5, full_dict.items()),
        key = lambda movie: movie[1]['title'] if movie[1].get('title') else ''
        )
    )

print('\n Задание №9 \n')
pprint.pp(filtered_sorted_dict, sort_dicts=False)


#10. **Опционально:** Добавьте аннотацию типов для переменных, содержащих результаты, и проверьте код с помощью `mypy`. Оставьте комментарий о успешной проверке.
# 
# Success: no issues found in 1 source file

#11. Сделайте красивый вывод результатов с использованием `pprint`, добавив подпись о том, какое задание выполнено.