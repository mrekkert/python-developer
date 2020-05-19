# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def errors(line):
    name, email, age = line.split()
    age = int(age)
    if len(line.split()) == 3:
        print(f'строка {line}')
    else:
        raise ValueError('invalid data')

    if name.isalpha():
        print(f'имя {name}')
    else:
        raise NotNameError('invalid name')

    if age in range(10, 100):
        print(f'возраст {age}')
    else:
        raise ValueError('invalid age')

    if '@' and '.' in email:
        print(f'e-mail {email}')
    else:
        raise NotEmailError('invalid e-mail')


with open('registrations.txt', 'r', encoding='utf-8') as reg_file:
    for line in reg_file:
        try:
            errors(line)
            with open('registrations_good.log', 'a', encoding='utf-8') as good_log:
                good_log.write(line)
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_log:
                    bad_log.write(f'ошибка - "{exc}" в строке -> {line}')
            else:
                with open('registrations_bad.log', 'a', encoding='utf-8') as bad_log:
                    bad_log.write(f'ошибка - "{exc}" в строке -> {line}')
        except NotNameError as NMError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bad_log:
                bad_log.write(f'ошибка - "{NMError}" в строке -> {line}')
        except NotEmailError as NEError:
            with open('registrations_bad.log', 'a', encoding='utf-8') as bad_log:
                bad_log.write(f'ошибка - "{NEError}" в строке -> {line}')
#зачет!