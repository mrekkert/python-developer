import simple_draw as sd

def face():


    def smile(cord_1, cord_2, color):
        cord_x, cord_y = 440, 40
        point_x = sd.get_point(cord_x + 30, cord_y + 50)
        point_y = sd.get_point(cord_x + 125, cord_y + 125)
        sd.ellipse(left_bottom=point_x, right_top=point_y, color=color, width=2)

        for x in range(55, 110, 30):
            point = sd.get_point(cord_x + x, cord_y + 100)
            sd.circle(center_position=point, radius=2, color=color, width=1)

        x = sd.get_point(cord_x + 40, cord_y + 85)
        y = sd.get_point(cord_x + 60, cord_y + 70)
        z = sd.get_point(cord_x + 90, cord_y + 70)
        z_1 = sd.get_point(cord_x + 110, cord_y + 85)
        point_list = (x, y, z, z_1)
        sd.lines(point_list=point_list, color=color, width=3)


    center_x = 440
    center_y = 35
    color = sd.COLOR_DARK_YELLOW
    smile(cord_1=center_x, cord_2=center_y, color=color)

face()
