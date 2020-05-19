# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# zip_file_name = 'python_snippets/voyna-i-mir.txt.zip'
# unzip = zipfile.ZipFile(zip_file_name, 'r')
# for file_name in unzip.namelist():
#     unzip.extract(file_name)
import zipfile
from abc import abstractmethod, ABCMeta


class Counter(metaclass=ABCMeta):

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.total_letters = 0

    def unzip(self):
        unzip = zipfile.ZipFile(self.file_name, 'r')
        for file_name in unzip.namelist():
            unzip.extract(file_name)
            self.file_name = file_name

    def collect(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_for_line(line=line)

    def collect_for_line(self, line):
        for char in line:
            if char.isalpha():
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1

    def letters_count(self):
        for value in self.stat.values():
            self.total_letters += value

    def table_top(self):
        print('+{letter:-^15}+{count:-^15}+'.format(letter='-', count='-'))
        print('|{letter:^15}|{count:^15}|'.format(letter='буква', count='частота'))
        print('+{letter:-^15}+{count:-^15}+'.format(letter='-', count='-'))

    def table_bottom(self):
        print('+{letter:-^15}+{count:-^15}+'.format(letter='-', count='-'))
        print('|{letter:^15}|{count:^15d}|'.format(letter='итого', count=self.total_letters))
        print('+{letter:-^15}+{count:-^15}+'.format(letter='-', count='-'))

    def run(self):
        self.collect()
        self.table_top()
        self.sort_it()
        self.letters_count()
        self.table_bottom()

    @abstractmethod
    def sort_it(self):
        pass


class CountDecrease(Counter):

    def sort_it(self):
        for letter, count in sorted(self.stat.items(), key=lambda x: x[1], reverse=True):
            print('|{letter:^15}|{count:^15d}|'.format(letter=letter, count=count))


class CountIncrease(Counter):

    def sort_it(self):
        for letter, count in sorted(self.stat.items(), key=lambda x: x[1]):
            print('|{letter:^15}|{count:^15d}|'.format(letter=letter, count=count))


class LetterIncrease(Counter):

    def sort_it(self):
        for letter, count in sorted(self.stat.items(), key=lambda x: x[0], reverse=True):
            print('|{letter:^15}|{count:^15d}|'.format(letter=letter, count=count))


class LetterDecrease(Counter):

    def sort_it(self):
        for letter, count in sorted(self.stat.items()):
            print('|{letter:^15}|{count:^15d}|'.format(letter=letter, count=count))


count_decrease = CountDecrease('voyna-i-mir.txt')
count_increase = CountIncrease('voyna-i-mir.txt')
letter_increase = LetterIncrease('voyna-i-mir.txt')
letter_decrease = LetterDecrease('voyna-i-mir.txt')

count_decrease.run()
count_increase.run()
letter_increase.run()
letter_decrease.run()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!