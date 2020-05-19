# -*- coding: utf-8 -*-

import simple_draw as sd
y_list = []
x_list = []
length_list = []
snowflake_list = []
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall
from snowfall import create_snowflake, snowflake_color, snowflake_step, pop_snowflakes, append_snowflakes, screens_edge,\
    some_thing

create_snowflake(snowflake_count=20)
while True:
    sd.clear_screen()
    snowflake_color(color=sd.COLOR_WHITE)
    snowflake_step(z=10)
    if screens_edge():
        pop_snowflakes()
        append_snowflakes(len(some_thing))

    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

#зачет!