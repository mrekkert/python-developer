# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def generator(file):
    prev_time = None
    nok_count = 0

    for line in file:
        if 'NOK' in line:
            slice = line[1:17]
            if slice != prev_time:
                if prev_time is not None:
                    yield prev_time, nok_count
                prev_time = slice
                nok_count = 0
            nok_count += 1

    if nok_count > 0:
        yield prev_time, nok_count


with open('events.txt', 'r') as file:
    for group_time, event_count in generator(file):
        print(f'[{group_time}] {event_count}')
#зачет!