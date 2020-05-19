# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat_list = []

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 10
            self.house.food -= 10
        else:
            print('{} нет еды'.format(self.name))

    def work(self):
        print('{} сходил на работу'.format(self.name))
        self.house.money += 150
        self.fullness -= 10

    def playing_ps4(self):
        print('{} играл в PS4 целый день'.format(self.name))
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
        else:
            print('{} деньги кончились!'.format(self.name))

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print('{} вьехал в дом'.format(self.name))

    def pick_up_cat(self, cat):
        self.cat_list.append(cat)
        cat.house = self.house
        print('{} подобрал кота'.format(self.name))

    def buy_cat_food(self):
        if self.house.cat_food <= 20:
            print('{} сходил коту за едой'.format(self.name))
            self.house.cat_food += 50
            self.house.money -= 50

    def clean_the_house(self):
        if self.house.dirt >= 100:
            print('{} сделал дома уборку'.format(self.name))
            self.house.dirt -= 100
            self.fullness -= 20
        # Это прям компромисс :) ладно, надеюсь вы поняли идею, которую я пытался донести
        elif self.house.dirt >= 50:
            print('{} чуть-чуть прибрался'.format(self.name))
            self.house.dirt -= 50
            self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 10:
            self.shopping()
        elif self.house.money <= 50:
            self.work()
        elif self.house.cat_food <= 20:
            self.buy_cat_food()
        elif self.house.dirt >= 100:
            self.clean_the_house()
        elif self.house.dirt >= 50:
            self.clean_the_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.playing_ps4()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Кот - {}, сытость - {}'.format(self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            print('{} поел'.format(self.name))
            self.fullness += 20
            self.house.cat_food -= 10

    def sleep(self):
        print('{} поспал'.format(self.name))
        self.fullness -= 10

    def tear_up_wallpapers(self):
        print('{} драл обои'.format(self.name))
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.sleep()
        else:
            self.tear_up_wallpapers()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, кошачей еды осталось {}, грязи осталось {}'.format(
            self.food, self.money, self.cat_food, self.dirt)


my_sweet_home = House()

man = Man(name='Дядя Фёдор')
cats = [
    Cat(name='Garfield'),
    Cat(name='Puss in Boots'),
    Cat(name='Cheshire Cat'),
    Cat(name='Tom')
]

man.go_to_the_house(house=my_sweet_home)
for kitty in cats:
    man.pick_up_cat(cat=kitty)


for day in range(1, 366):
    print('================ день {} =================='.format(day))
    man.act()
    for kitty in cats:
        kitty.act()
    print('--- в конце дня ---')
    print(man)
    for kitty in cats:
        print(kitty)
    print(my_sweet_home)
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
#зачет!