import simple_draw as sd

y_list = []
x_list = []
length_list = []
snowflake_list = []


def create_snowflake(snowflake_count):
    for _ in range(snowflake_count):
        x_list.append(sd.random_number(10, 500))
        y_list.append(sd.random_number(600, 1000))
        length_list.append(sd.random_number(10, 25))


def snowflake_color(color):
    for i, y in enumerate(x_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=length_list[i], color=color)
        y_list[i] -= sd.random_number(5, 15)


def snowflake_step(z, x=0):
    for i, y in enumerate(x_list):
        x_list[i] += sd.random_number(x, z)
        x_list[i] -= sd.random_number(x, z)


def screens_edge():
    snowflake_list.clear()
    for i, y in enumerate(x_list):
        if y_list[i] <= 0:
            snowflake_list.append(i)
    return snowflake_list


some_thing = screens_edge()


def pop_snowflakes():
    for j in snowflake_list[::-1]:
        x_list.pop(j)
        y_list.pop(j)
        length_list.pop(j)


def append_snowflakes(amount):
    for _ in range(amount):
        x_list.append(sd.random_number(10, 500))
        y_list.append(sd.random_number(500, 1000))
        length_list.append(sd.random_number(10, 25))
