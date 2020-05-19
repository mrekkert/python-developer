import simple_draw as sd


brick_x = 100
brick_y = 50

for row, y in enumerate(range(0, 1000, 50)):
    x0 = -50 if row % 2 == 0 else 0
    for x in range(x0, 800, 100):
        left_bottom = sd.get_point(x, y)
        right_top = sd.get_point(x + brick_x, y + brick_y)
        sd.rectangle(left_bottom, right_top, color=sd.COLOR_DARK_ORANGE, width=1)




sd.pause()