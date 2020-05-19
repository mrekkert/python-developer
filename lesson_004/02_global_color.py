# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_figure(point, angle, length, incline, color):
    v2 = sd.get_vector(point, angle, length)
    for angle in range(20, 360 - incline, incline):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
        v1.draw(color=color)
        point = v1.end_point
    sd.line(start_point=point, end_point=v2.start_point, width=2, color=color)


def triangle(point, angle, length, color):
    incline = 120
    draw_figure(point, angle, length, incline, color)


def square(point, angle, length, color):
    incline = 90
    draw_figure(point, angle, length, incline, color)


def pentagon(point, angle, length, color):
    incline = 72
    draw_figure(point, angle, length, incline, color)


def hexagon(point, angle, length, color):
    incline = 60
    draw_figure(point, angle, length, incline, color)


def figure_list():
    color = user_input()
    triangle(point=sd.get_point(100, 100), angle=20, length=100, color=color)
    square(point=sd.get_point(400, 100), angle=20, length=100, color=color)
    pentagon(point=sd.get_point(100, 350), angle=20, length=100, color=color)
    hexagon(point=sd.get_point(400, 350), angle=20, length=100, color=color)


color_list = {
    '1': {'color_name': 'red', 'sd_name': sd.COLOR_RED},
    '2': {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
    '3': {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
    '4': {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
    '5': {'color_name': 'cyan', 'sd_name': sd.COLOR_CYAN},
    '6': {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE},
    '7': {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}
}


def user_input():
    print('Возможные цвета:\n1 : red \n2 : orange \n3 : yellow \n4 : green \n5 : '
          'cyan \n6 : blue \n7 : purple\n')
    color = input('Введите желаемый цвет: ')
    while color not in color_list:
        print('Вы ввели некорректный номер!')
        color = input('Введите желаемый цвет: ')
    if color in color_list:
        color = color_list[color]
        return color['sd_name']

# вот так?)


figure_list()
sd.pause()
#зачет!