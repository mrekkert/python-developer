# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
# TODO Метод __add__ по своей сути отвечает за операцию сложения. Что это значит?
# TODO Есть у нас например две строки "а" и "б", мы пишем "а" + "б"
# TODO Пайтон проверяет свои глубины, ищет методичку "как складывать строки", которая как раз и находится в методе add
# TODO И он запускает этот метод, получая на выходе "аб". С кодом это выглядит как-то так
# TODO def __add__(self, другая_строка):
# TODO     результат = "перечень элементов из обеих строк"
# TODO     return результат

# TODO Таким образом нам даётся власть решать - как производить сложение.
# TODO Чтобы это понять в первую очередь надо в голове отделить стандартное понимание операции сложения из школы)
# TODO И думать об этом как об "операции с названием сложение", тк по факту - это просто метод объекта,
# TODO Который вызывается необычным способом (при помощи плюса)
# TODO Мы могли бы взять метод сложения строк и заменить его другим названием
# TODO def наше_сложение(self, другая_строка):
# TODO     результат = "перечень элементов из обеих строк"
# TODO     return результат
# TODO Тогда запускали мы бы его как и все другие методы
# TODO имя_объекта.наше_сложение(параметр)


# TODO Здесь же нам надо переопределить метод сложения так, чтобы он проверял объект, переданный параметром
# TODO на принадлежность определенному классу, например воздуху (isinstance(объект, Air)
# TODO И если мы узнали, что объект - воздушного типа - мы знаем, что должен получиться шторм
# TODO Поэтому возвращаем объект класса шторм. Выходит что-то вроде: иф это воздух? ретурн Шторм()
# TODO Кстати обратите внимание на () - это важная штука, которую понимают не сразу
# TODO Тут как с функциями, если указать функцию без () - она будет объектом простым, её можно хранить в словаре
# TODO Как мы это делали в 4 модуле, в 3 задании. А если добавить - функция() - это уже заставит функцию сработать
# TODO И она уже будет не объектом-функцией, а тем результатом, который из функции возвращается.
# TODO Так же и с классом. Просто Класс - это обращение к созданному классу.
# TODO А вот Класс() - это действие, результатом которого будет объект Класса
# TODO Объекты класса ( Класс() ) - независимы после создания, что значит,
# TODO что мы можем менять их значения и это не отразится
# TODO ни на самом классе, ни на других объектах.
# TODO А если изменить что-то напрямую в Классе, то все объекты, созданные после изменения будут в себе нести
# TODO это изменение)
# TODO Надеюсь голова у вас после этого не забилась пуще прежнего :)


class Water:
    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Stone):
            return Sand()


class Air:
    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Water):
            return Storm()
        elif isinstance(other, Lava):
            return Stone()


class Fire:
    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Dust):
            return Ash()
        elif isinstance(other, Stone):
            return Metal()


class Earth:
    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Water):
            return Dirt()


class Storm:
    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return ''.join(self.name)


class Steam:
    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return ''.join(self.name)


class Dirt:
    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return ''.join(self.name)


class Lightning:
    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Metal):
            return Electricity()


class Dust:
    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Fire):
            return Ash()


class Lava:
    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Air):
            return Stone()


class Stone:
    def __init__(self):
        self.name = 'Камень'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Water):
            return Sand()
        elif isinstance(other, Fire):
            return Metal()


class Sand:
    def __init__(self):
        self.name = 'Песок'

    def __str__(self):
        return ''.join(self.name)


class Metal:
    def __init__(self):
        self.name = 'Металл'

    def __str__(self):
        return ''.join(self.name)

    def __add__(self, other):
        if isinstance(other, Lightning):
            return Electricity()


class Ash:
    def __init__(self):
        self.name = 'Пепел'

    def __str__(self):
        return ''.join(self.name)


class Electricity:
    def __init__(self):
        self.name = 'Электричество'

    def __str__(self):
        return ''.join(self.name)


print(Water(), '+', Air(), '=', Air() + Water())
print(Water(), '+', Fire(), '=', Fire() + Water())
print(Water(), '+', Earth(), '=', Earth() + Water())
print(Water(), '+', Stone(), '=', Stone() + Water())
print(Air(), '+', Lava(), '=', Air() + Lava())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Fire(), '+', Stone(), '=', Stone() + Fire())
print(Fire(), '+', Dust(), '=', Dust() + Fire())
print(Metal(), '+', Lightning(), '=', Metal() + Lightning())
# Отлично расширили! :)

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
#зачет!