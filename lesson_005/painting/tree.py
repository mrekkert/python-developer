import simple_draw as sd
sd.resolution = (1200, 600)



def draw_bunches(start_point, angle, length):
    if length <= 5:
        return
    v1 = sd.get_vector(start_point, angle, length, width=2)
    v1.draw(color=sd.COLOR_DARK_GREEN)
    draw_bunches(v1.end_point, angle + 30, length * 0.75)
    draw_bunches(v1.end_point, angle - 30, length * 0.75)

def tree():
    root_point = sd.get_point(1000, 0)
    draw_bunches(start_point=root_point, angle=90, length=60)
    root_point = sd.get_point(900, 10)
    draw_bunches(start_point=root_point, angle=90, length=50)
    root_point = sd.get_point(1100, 15)
    draw_bunches(start_point=root_point, angle=90, length=45)


tree()
