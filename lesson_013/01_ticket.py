# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
import argparse
import os

from PIL import Image, ImageDraw, ImageFont


class AirplaneTicket:

    def __init__(self, template=None, font_path=None):
        self.template = os.path.join("images", "ticket_template.png") if template is None else template
        if font_path is None:
            self.font_path = os.path.join("fonts", "ofont.ru_Uk_Antique.ttf")
        else:
            self.font_path = font_path

    def make_ticket(self, fio, from_, to, date, save):
        im = Image.open(self.template)
        font = ImageFont.truetype(self.font_path, size=17)

        draw = ImageDraw.Draw(im)

        draw.text((45, 120), fio, font=font, fill='black')
        draw.text((45, 190), from_, font=font, fill='black')
        draw.text((45, 255), to, font=font, fill='black')
        draw.text((280, 260), date, font=font, fill='black')

        im.save(save)


# if __name__ == '__main__':
#     ticket = AirplaneTicket()
#     ticket.make_ticket(
#         fio="Иванов И.И.",
#         from_="Оттуда",
#         to="Туда",
#         date="12.12",
#         save="images/new_ticket.png"
#     )

if __name__ == '__main__':
    ticket = AirplaneTicket()
    parser = argparse.ArgumentParser(description='Ticket script')

    parser.add_argument('-fio', action="store", dest="fio", help='Fill "name" field')
    parser.add_argument('-from_', action="store", dest="from_", help='Fill "from" field')
    parser.add_argument('-to', action="store", dest="to", help='Fill "where" field')
    parser.add_argument('-date', action="store", dest="date", help='Fill "date" field')
    parser.add_argument('--save_to', action="store", dest="save", help='save path')

    args = parser.parse_args()
    print(args)

    ticket.make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save=args.save)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
#зачет!