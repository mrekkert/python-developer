#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.


T = my_favorite_movies[0:10]
F = my_favorite_movies[12:25]
Av = my_favorite_movies[27:33]
Al = my_favorite_movies[35:40]
B = my_favorite_movies[42:57]
new_list = [T, B, F, Al]
print(new_list)
#зачет!