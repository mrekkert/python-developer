# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


errors_dict = {
               1: IamGodError('Я-Бог'),
               2: DrunkError('пьяный'),
               3: CarCrashError('попал в аварию'),
               4: GluttonyError('объелся'),
               5: DepressionError('в депресии'),
               6: SuicideError("совершил 'Роскомнадзор'")
               }


def one_day():
    dice = randint(1, 13)
    if dice == 9:
        raise errors_dict[randint(1, 6)]
    return randint(1, 7)


carma_count = 0


with open('log_file.txt', 'w', encoding='utf-8') as log_file:
    while carma_count <= ENLIGHTENMENT_CARMA_LEVEL:
        try:
            one_day()
            carma_count += one_day()
        except (IamGodError, DrunkError, CarCrashError, GluttonyError, DepressionError, SuicideError) as exc:
            log_file.write(f'Поймано исключение - {exc}\n')
#зачет!