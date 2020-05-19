# -*- coding: utf-8 -*-

import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.color = sd.COLOR_WHITE
        self.length = sd.random_number(10, 30)
        self.speed = sd.random_number(10, 20)
        self.x = sd.random_number(10, 600)
        self.y = sd.random_number(500, 800)

    def clear_previous_picture(self):
        self.color = sd.background_color
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=self.color)

    def move(self):
        if flake.can_fall():
            self.y -= self.speed

    def draw(self):
        self.color = sd.COLOR_WHITE
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length, color=self.color)

    def can_fall(self):
        return self.y >= 10


flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


count_fallen_flakes = 0
flakes_list = []

def get_fallen_flakes():
    global count_fallen_flakes
    if flake.y <= 10:
        count_fallen_flakes += 1
        print(count_fallen_flakes)
    return count_fallen_flakes


def get_flakes(count):
    global flakes_list
    for _ in range(count):
        flakes_list.append(Snowflake())
    return flakes_list


def append_flakes(count):
    if get_flakes(count):
        flakes_list.append(Snowflake())


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=1)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
#зачет!