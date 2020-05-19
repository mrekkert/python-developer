# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300)
# radius = 50
# color = sd.random_color()
# for _ in range(3):
#     radius += 5
#     sd.circle(center_position=point, radius=radius, color=color, width=2)


# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг

def bubbles(point, step, color):
    radius = 50
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, width=2, color=color)
        color = sd.random_color()
#
#
# point = sd.get_point(300, 300)
# bubbles(point=point, step=10, color=sd.random_color())

# Нарисовать 10 пузырьков в ряд

# for x in range(100, 1101, 110):
#     point = sd.get_point(x, 100)
#     bubbles(point=point, step=7, color=sd.random_color())
#

# Нарисовать три ряда по 10 пузырьков

# for y in range(100, 301, 100):
#     for x in range(100, 1101, 110):
#         point = sd.get_point(x, y)
#         bubbles(point=point, step=7, color=sd.random_color())
#

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


for _ in range(100):
    point = sd.random_point()
    step = random.randint(2, 15)
    bubbles(point=point, step=step, color=sd.random_color())

sd.pause()
#зачет!