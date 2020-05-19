# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)


point_x, point_y = 50, 350
step = 5
for colors in rainbow_colors:
    point_x += step
    point_y += step
    start_point = sd.get_point(point_x, 50)
    end_point = sd.get_point(point_y, 450)
    sd.line(start_point=start_point, end_point=end_point, color=colors, width=4)


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


# def rainbow(point, step):
#     radius = 600
#     for colors in rainbow_colors:
#         radius -= step
#         sd.circle(center_position=point, radius=radius, width=20, color=colors)
#
#
# point = sd.get_point(450, -100)
# rainbow(point=point, step=20)


sd.pause()

#зачет!