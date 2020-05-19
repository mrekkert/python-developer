# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoW,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoW (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money_in_nightstand = 100
        self.food_in_fridge = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязи осталось {}'.format(
            self.food_in_fridge, self.money_in_nightstand, self.dirt)


class Human:
    total_food = 0

    def __init__(self, name, house):
        self.house = house
        self.name = name
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return '{}, сытость {}, счастье {}'.format(
            self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food_in_fridge:
            self.fullness += randint(10, 30)
        self.house.food_in_fridge -= self.fullness
        Human.total_food += self.fullness

    def pet_the_cat(self):
        self.happiness += 5


class Husband(Human):
    total_money = 0

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        self.house.dirt += 3
        if self.fullness <= 0 or self.happiness <= 10:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.house.money_in_nightstand <= 0 and self.house.food_in_fridge <= 10:
            self.work()
        elif self.happiness <= 10:
            self.gaming()
        elif self.house.dirt >= 90:
            self.happiness -= 10
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.gaming()

    def eat(self):
        super().eat()
        print('{} поел'.format(self.name))

    def work(self):
        self.fullness -= 10
        self.house.money_in_nightstand += 150
        print('{} сходил на работу'.format(self.name))
        Husband.total_money += self.house.money_in_nightstand

    def gaming(self):
        self.happiness += 20
        if self.happiness > 100:
            self.happiness = 100
        self.fullness -= 10
        print('{} играл в WoW'.format(self.name))


class Wife(Human):

    fur_coat_count = 0

    def __init__(self, name, house):
        super().__init__(name=name, house=house)
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return super().__str__()

    def act(self):
        self.house.dirt += 2
        if self.fullness <= 0 or self.happiness <= 10:
            print('{} умерла...'.format(self.name))
            return

        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif self.house.food_in_fridge <= 10 and self.house.money_in_nightstand >= 30:
            self.shopping()
        elif self.house.money_in_nightstand > 350 and self.house.food_in_fridge >= 50:
            self.buy_fur_coat()
        elif self.house.dirt > 10:
            self.clean_house()
        elif self.house.dirt >= 90:
            self.happiness -= 10
        elif dice == 1:
            self.shopping()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.pet_the_cat()
        else:
            self.clean_house()

    def eat(self):
        super().eat()
        print('{} поела'.format(self.name))

    def shopping(self):
        if self.house.money_in_nightstand:
            self.fullness -= 10
        self.house.money_in_nightstand -= randint(30, 60)
        self.house.food_in_fridge += self.house.money_in_nightstand
        print('{} сходила за продуктами'.format(self.name))

    def buy_cat_food(self):
        if self.house.money_in_nightstand:
            if self.house.cat_food <= 5:
                print('{} сходила коту за едой'.format(self.name))
            self.house.cat_food += 10
            self.house.money_in_nightstand -= 10

    def buy_fur_coat(self):
        if self.house.money_in_nightstand:
            self.house.money_in_nightstand -= 350
        self.happiness += 60
        if self.happiness > 100:
            self.happiness = 100
        self.fullness -= 10
        print('{} купила шубу'.format(self.name))
        Wife.fur_coat_count += 1

    def clean_house(self):
        if self.house.dirt:
            self.house.dirt -= self.house.dirt
        self.fullness -= 10
        print('{} сделала уборку'.format(self.name))


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30

    def __str__(self):
        return '{}, сытость {}'.format(self.name, self.fullness)

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
            self.soil()

    def eat(self):
        if self.house.cat_food:
            self.fullness += randint(1, 10)
        self.house.cat_food -= (self.fullness // 2)
        print('{} поел'.format(self.name))

    def sleep(self):
        print('{} поспал'.format(self.name))
        self.fullness -= 10

    def soil(self):
        self.house.dirt += 5
        self.fullness -= 10
        print('{} портил обои'.format(self.name))


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name=name, house=house)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness <= 0:
            print('{} умер...'.format(self.name))
            return
        dice = randint(1, 6)
        if self.fullness <= 1:
            self.eat()
        elif dice == 1:
            self.eat()
        elif self.fullness > 30:
            self.fullness = 30
        else:
            self.sleep()

    def eat(self):
        if self.house.food_in_fridge:
            self.fullness += randint(1, 10)
        self.house.food_in_fridge -= self.fullness
        print('{} поел'.format(self.name))

    def sleep(self):
        print('{} спал'.format(self.name))


home = House()
vlad = Husband(name='Влад', house=home)
alina = Wife(name='Алина', house=home)
son = Child(name='Сын', house=home)
puss = Cat(name='Кот', house=home)

for day in range(366):
    cprint('================== День {} =================='.format(day), color='red')
    vlad.act()
    alina.act()
    puss.act()
    son.act()
    cprint(vlad, color='cyan')
    cprint(alina, color='cyan')
    cprint(son, color='cyan')
    cprint(puss, color='cyan')
    cprint(home, color='cyan')

cprint('Всего заработано денег {}'.format(Husband.total_money), color='yellow')
cprint('Всего съедено еды {}'.format(Human.total_food), color='yellow')
cprint('Всего куплено шуб {}'.format(Wife.fur_coat_count), color='yellow')

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов




######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

#зачет!