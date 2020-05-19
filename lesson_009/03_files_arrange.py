# -*- coding: utf-8 -*-


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
import os
import time
import shutil


class Arrange:

    def __init__(self, src_folder, dst_folder):
        self.src_folder = src_folder
        self.dst_folder = dst_folder
        self.path_normalized = os.path.normpath(src_folder)

    def file_processing_method(self, dirpath, file):
        file_path = os.path.join(dirpath, file)
        secs = os.path.getmtime(file_path)
        file_time = time.gmtime(secs)
        new_file_time = time.strftime('%Y/%m', file_time)
        os.makedirs('{}/{}'.format(self.dst_folder, new_file_time), exist_ok=True)
        shutil.copy2(file_path, '{}/{}'.format(self.dst_folder, new_file_time))

    def parse(self):
        for dirpath, dirnames, filenames in os.walk(self.path_normalized):
            for file in filenames:
                self.file_processing_method(dirpath, file)


arrange = Arrange('icons', 'icons_by_year')
arrange.parse()

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, бе предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!