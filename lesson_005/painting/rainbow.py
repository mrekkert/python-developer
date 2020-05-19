import simple_draw as sd
sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow_lines(point, step):
    radius = 915
    for colors in rainbow_colors:
        radius -= step
        sd.circle(center_position=point, radius=radius, width=8, color=colors)


def rainbow():
    point = sd.get_point(400, -150)
    rainbow_lines(point=point, step=8)
