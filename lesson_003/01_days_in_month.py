# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month, 'й месяц')

days_28 = [2]
days_30 = [4, 6, 9, 11]
days_31 = [1, 3, 5, 7, 8, 10, 12]

if month in days_28:
    print("28 дней")
elif month in days_30:
    print("30 дней")
elif month in days_31:
    print("31 день")
else:
    print("Номер месяца некорректен")

#зачет!