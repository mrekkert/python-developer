# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
brick_x = 100
brick_y = 50

for row, y in enumerate(range(0, 1000, 50)):
    x0 = -50 if row % 2 == 0 else 0
    for x in range(x0, 800, 100):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + brick_x, y + brick_y)
        sd.rectangle(left_bottom, right_top, color=sd.COLOR_DARK_ORANGE, width=1)

# да, я обратил внимание, что цвет другой. в библиотеке написано,
# что если нижняя точка меньше верхней, то цвет инвертируется.
# поэтому я и поставил синий))
# Хитро! :) Хорошо, что читаете библиотеки, это супер полезный скилл
simple_draw.pause()

#зачет!