# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (600, 600)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_bunches(start_point, angle, length):
    if length <= 5:
        return
    v1 = sd.get_vector(start_point, angle, length, width=2)
    v1.draw(color=sd.random_color())
    angle_deviation = random.uniform(0, 0.4) * 30
    length_deviation = random.uniform(0, 0.2) * 0.75
    draw_bunches(v1.end_point, angle + 30 + angle_deviation, length * 0.75 + length_deviation)
    draw_bunches(v1.end_point, angle - 30 - angle_deviation, length * 0.75 + length_deviation)


# вот так?
# я не стал вводить переменные, потому что не был уверен, правильно ли я все делаю)
# Я имел ввиду создание переменных для угла и длины, чтобы вычислений не было внутри параметров функции,
# Но это в целом выглядит не так страшно, просто старайтесь не увлекаться с таким способом передачи параметров)


root_point = sd.get_point(300, 30)
draw_bunches(start_point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()
#зачет!
