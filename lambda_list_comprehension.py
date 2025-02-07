
from marvel import full_dict
import typing
from pprint import pprint

# Реализуйте ввод от пользователя, который будет принимать цифры через пробел. Разбейте введённую строку на список и примените к каждому элементу `int`, заменяя нечисловые элементы на `None` с помощью `map`.

def try_int(x):
    try:
        return int(x)
    except ValueError:
        return None

numbers_inp = input("Введите числа через пробел: ")
numbers = list(map(try_int, numbers_inp.split()))

pprint(numbers)

# numbers2 = [int(number) if number.isdigit() else None for number in numbers_inp.split()]
# print(numbers2)


# 3. Используйте `filter`, чтобы создать словарь, содержащий исходные `id` и другие ключи, но только для тех фильмов, `id` которых присутствуют в списке, полученном на предыдущем шаге.

#Противоречивое задание, как-будто подразумевался список словарей, включающих id и все остальные ключи.
# Что-то типа такого:
# filtered_list = list(filter(lambda movie: isinstance(movie['id'], int) and movie['id'] in numbers, [{'id': key, **value} for key, value in full_dict.items()]))
# print(filtered_list)

filtered_dict = dict(filter(lambda movies: isinstance(movies[0], int) and movies[0] in numbers, full_dict.items()))
pprint(filtered_dict)


#4. Создайте множество с помощью `set comprehension`, собрав уникальные значения ключа `director` из словаря.

set_of_directors = {full_dict[id]['director'] for id in full_dict}
pprint(set_of_directors)


#5. С помощью `dict comprehension` создайте копию исходного словаря `full_dict`, преобразовав каждое значение `'year'` в строку. **(Опционально)**

full_dict_copy = {key:{**value, 'year': str(value['year'])} for key, value in full_dict.items()}
pprint(full_dict_copy)
pprint(type(full_dict_copy[0]['year']))


#6. Используйте `filter`, чтобы получить словарь, содержащий только те фильмы, которые начинаются на букву `Ч`.

ch_movies = dict(filter(lambda movie: movie[1].get('title') and movie[1]['title'][0].lower()== 'ч', full_dict.items()))
pprint(ch_movies)


#7. Отсортируйте словарь `full_dict` по одному параметру с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по какому параметру вы производите сортировку.

# Пусть будет 'title':

sorted_by_title = dict(sorted(full_dict.items(), key = lambda movie: movie[1]['title'] if movie[1].get('title') else ''))
pprint(sorted_by_title)


#8. Отсортируйте словарь `full_dict` по двум параметрам с использованием `lambda`, создавая аналогичный по структуре словарь. Обязательно укажите, по каким параметрам вы производите сортировку.

# Пусть будут 'title' и 'year':

sorted_by_title = dict(sorted(full_dict.items(), key = lambda movie: movie[1]['title'] if movie[1].get('title') else ''))

sorted_by_title_and_year = dict(sorted(sorted_by_title.items(), 
    key = lambda movie: movie[1]['year'] if movie[1].get('year') 
    and isinstance(movie[1]['year'], int) else 0 ))

pprint(sorted_by_title_and_year)


#9. Напишите однострочник, который отфильтрует и отсортирует `full_dict` с использованием `filter` и `sorted`.

# не надо такие вещи делать однострочником)))

filtered_sorted_dict = dict(
    sorted(
        filter(lambda movie: movie[0]<5, full_dict.items()),
        key = lambda movie: movie[1]['title'] if movie[1].get('title') else ''
        )
    )

pprint(filtered_sorted_dict)


#10. **Опционально:** Добавьте аннотацию типов для переменных, содержащих результаты, и проверьте код с помощью `mypy`. Оставьте комментарий о успешной проверке.
# 
# Success: no issues found in 1 source file

#11. Сделайте красивый вывод результатов с использованием `pprint`, добавив подпись о том, какое задание выполнено.