import simple_draw as sd

sd.resolution = (1200, 600)


def house():
    # roof
    point_list = [sd.get_point(350, 237), sd.get_point(695, 237), sd.get_point(520, 338), sd.get_point(350, 238)]
    sd.polygon(point_list=point_list, color=sd.COLOR_DARK_ORANGE, width=0)
    # window
    window_point = sd.get_point(465, 72)
    sd.square(left_bottom=window_point, side=110, color=sd.COLOR_WHITE, width=0)
    # outside walls
    square_point = sd.get_point(400, -5)
    sd.square(left_bottom=square_point, side=240, color=sd.COLOR_WHITE, width=1)
    # wall
    brick_x = 40
    brick_y = 20

    for row, y in enumerate(range(0, 220, 18)):
        x0 = 400 if row % 2 == 0 else 420
        for x in range(x0, 620, 40):
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + brick_x, y + brick_y)
            sd.rectangle(left_bottom, right_top, color=sd.COLOR_WHITE, width=1)


house()


