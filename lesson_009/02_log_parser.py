# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):

    def __init__(self, file_name):
        self.name = file_name
        self.source_file = open(self.name)
        self.nok_dict = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.source_file.close()

    @abstractmethod
    def read(self, edge):
        with self.source_file as file:
            for line in file:
                if 'NOK' in line:
                    slice = line[1:edge]
                    if slice in self.nok_dict:
                        self.nok_dict[slice] += 1
                    else:
                        self.nok_dict[slice] = 1

    def write(self, ready_file_name):
        with open(ready_file_name, 'w') as out_file:
            for key, value in self.nok_dict.items():
                out_file.write('[{}] {}\n'.format(key, value))


class Hours(Parser):
    def read(self, edge=14):
        super().read(edge=edge)


class Months(Parser):
    def read(self, edge=8):
        super().read(edge=edge)


class Years(Parser):
    def read(self, edge=5):
        super().read(edge=edge)


hours = Hours('events.txt')
months = Months('events.txt')
years = Years('events.txt')

hours.read()
hours.write('out1.txt')
months.read()
months.write('out2.txt')
years.read()
years.write('out3.txt')

# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!