# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
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
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


import os


class Exchange:
    def __init__(self, file_name):
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
        return round(self.volatility, 2)


object_lst = []

if __name__ == '__main__':
    dir_name = r"trades"
    file = os.listdir(dir_name)
    for item in file:
        trades = os.path.join(dir_name, item)
        exchange = Exchange(file_name=trades)
        object_lst.append(exchange)


def pretty_print():
    sorted_ticker_dict = {}
    name_lst = []
    lst = []
    key_list = []
    for ticker in object_lst:
        name_lst.append(ticker.__str__())
        lst.append(ticker.run())
        ticker_dict = dict(zip(name_lst, lst))
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


pretty_print()
#зачет!