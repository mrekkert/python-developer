import simple_draw as sd


# def snowflakes():
#     N = 20
#
#     y_list = []
#     x_list = []
#     length_list = []
#     snowflake_list = []
#
#
#     for _ in range(N):
#         x_list.append(sd.random_number(10, 100))
#         y_list.append(sd.random_number(600, 1000))
#         length_list.append(sd.random_number(5, 15))
#
#     while True:
#         sd.clear_screen()
#         for i, y in enumerate(x_list):
#             point = sd.get_point(x_list[i], y_list[i])
#             sd.snowflake(center=point, length=length_list[i])
#             y_list[i] -= sd.random_number(5, 15)
#             x_list[i] += sd.random_number(0, 10)
#             x_list[i] -= sd.random_number(0, 10)
#             if y_list[i] <= 0:
#                 snowflake_list.append(i)
#         for j in snowflake_list[::-1]:
#             x_list.pop(j)
#             y_list.pop(j)
#             length_list.pop(j)
#             x_list.append(sd.random_number(10, 100))
#             y_list.append(sd.random_number(500, 1000))
#             length_list.append(sd.random_number(5, 15))
#         snowflake_list = []
#
#         sd.sleep(0.1)
#         if sd.user_want_exit():
#             break
#
#
# snowflakes()


def snowflakes():
    N = 200
    y_list = []
    x_list = []
    length_list = []

    for _ in range(N):
        x_list.append(sd.random_number(0, 1200))
        y_list.append(sd.random_number(5, 30))
        length_list.append(sd.random_number(5, 20))

    for i, y in enumerate(x_list):
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=length_list[i])

        if sd.user_want_exit():
            break


snowflakes()
