# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_figure(point, angle, length):
        angles = int(360 / n)
        v2 = sd.get_vector(point, angle, length)
        for angle in range(20, 360 - angles, angles):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
            v1.draw()
            point = v1.end_point
        sd.line(start_point=point, end_point=v2.start_point, width=2)
    return draw_figure


draw_triangle = get_polygon(n=3)
draw_triangle(point=sd.get_point(100, 100), angle=20, length=100)


sd.pause()
#зачет!