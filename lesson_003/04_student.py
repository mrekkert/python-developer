# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

month_1 = expenses - educational_grant
months = 0
summ = 0
while months <= 9:
    months += 1
    money = (expenses - educational_grant)
    summ += money
    expenses *= 1.03
print('Студенту надо попросить', round(summ, 2), 'рублей')
# убрал if, но теперь в консоли видны все итерации. а у меня if было, чтобы видеть конечный результат
# исправил ;)


#зачет!