# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#


import os
from threading import Thread


class Exchange(Thread):
    def __init__(self, file_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.numbers = []
        self.average_price = 0
        self.volatility = 0

    def __str__(self):
        return '{}'.format(self.file_name)

    def run(self):
        with open(self.file_name, 'r') as ticker:
            ticker.readline()
            for line in ticker:
                secid, tradetime, price, quantity = line.split(',')
                self.numbers.append(float(price))
        self.average_price = (max(self.numbers) + min(self.numbers)) / 2
        self.volatility = ((max(self.numbers) - min(self.numbers)) / self.average_price) * 100
        return self.volatility


def main():
    global ticker_dict
    object_lst = []
    name_lst = []
    lst = []
    dir_name = r"trades"
    file = os.listdir(dir_name)
    for item in file:
        trades = os.path.join(dir_name, item)
        exchange = Exchange(file_name=trades)
        object_lst.append(exchange)

    for ticker in object_lst:
        ticker.start()
    for ticker in object_lst:
        ticker.join()

    for ticker in object_lst:
        name_lst.append(ticker.__str__())
        lst.append(round(ticker.volatility, 2))
        ticker_dict = dict(zip(name_lst, lst))


def pretty_print():
    key_list = []

    sorted_ticker_dict = dict(sorted(ticker_dict.items(), key=lambda i: i[1], reverse=True))

    print('Максимальная волатильность:')
    for key, value in list(sorted_ticker_dict.items())[:3]:
        print(f'{" " * 2}{key[7:18]} - {value}%')

    print('Минимальная волатильность:')
    for key, value in list(sorted_ticker_dict.items())[-17:]:
        if value != 0:
            print(f'{" " * 2}{key[7:18]} - {value}%')

    print('Нулевая волатильность:')
    for key, value in sorted_ticker_dict.items():
        if value == 0:
            key_list.append(key[7:18])
    print(', '.join(map(str, key_list)))


if __name__ == '__main__':
    main()
    pretty_print()
#зачет!