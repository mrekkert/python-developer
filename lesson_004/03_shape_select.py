# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def draw_figure(point, angle, length, incline):
    v2 = sd.get_vector(point, angle, length)
    for angle in range(20, 360 - incline, incline):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw()
        point = v1.end_point
    sd.line(start_point=point, end_point=v2.start_point, width=2)


def triangle(point=sd.get_point(100, 100), angle=20, length=100):
    incline = 120
    draw_figure(point, angle, length, incline)


def square(point=sd.get_point(400, 100), angle=20, length=100):
    incline = 90
    draw_figure(point, angle, length, incline)


def pentagon(point=sd.get_point(100, 350), angle=20, length=100):
    incline = 72
    draw_figure(point, angle, length, incline)


def hexagon(point=sd.get_point(400, 350), angle=20, length=100):
    incline = 60
    draw_figure(point, angle, length, incline)


figure_dict = {
    '1': {'figure_name': 'треугольник', 'def_name': triangle},
    '2': {'figure_name': 'квадрат', 'def_name': square},
    '3': {'figure_name': 'пятиугольник', 'def_name': pentagon},
    '4': {'figure_name': 'шестиугольник', 'def_name': hexagon}
}


def user_input():
    print('Возможные фигуры:\n1 : треугольник \n2 : квадрат \n3 : пятиугольник \n4 : шестиугольник')
    figure = input('Введите желаемую фигуру: ')
    while figure not in figure_dict:
        print('Вы ввели некорректный номер!')
        figure = input('Введите желаемую фигуру: ')
    if figure in figure_dict:
        figure = figure_dict[figure]
        return figure['def_name']


some_figure = user_input()
some_figure()

sd.pause()
#зачет!