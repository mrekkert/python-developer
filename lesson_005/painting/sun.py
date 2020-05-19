import simple_draw as sd


def sun():
    sd.circle(center_position=sd.get_point(200, 500), radius=40, color=sd.COLOR_YELLOW, width=0)
    x = 0
    for _ in range(13):
        sd.vector(start=sd.get_point(200, 500), angle=x, length=100, width=2, color=sd.COLOR_YELLOW)
        x += 30


sun()
