# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


y_list = []
x_list = []
length_list = []
snowflake_list = []


for _ in range(N):
    x_list.append(sd.random_number(10, 500))
    y_list.append(sd.random_number(600, 1000))
    length_list.append(sd.random_number(10, 25))

while True:
    sd.clear_screen()
    for i, y in enumerate(x_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=length_list[i])
        y_list[i] -= sd.random_number(5, 15)
        x_list[i] += sd.random_number(0, 10)
        x_list[i] -= sd.random_number(0, 10)
        if y_list[i] <= 0:
            snowflake_list.append(i)
    for j in snowflake_list[::-1]:
        x_list.pop(j)
        y_list.pop(j)
        length_list.pop(j)
        x_list.append(sd.random_number(10, 500))
        y_list.append(sd.random_number(500, 1000))
        length_list.append(sd.random_number(10, 25))
    snowflake_list = []

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


#зачет!