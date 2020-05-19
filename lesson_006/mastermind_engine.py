from random import shuffle

_holder = []
bulls_and_cows = {'Cows': 0,
                  'Bulls': 0}


def make_a_number():
    global _holder
    numbers = [x for x in range(10)]
    shuffle(numbers)
    _holder = numbers[:4]
    if _holder[0] == 0:
        _holder[0] = _holder[1]
        _holder[1] = 0
    _holder = "".join(map(str, _holder))
    print(_holder)


def check_number(input_number):
    global bulls_and_cows
    bulls_and_cows = {'Cows': 0,
                      'Bulls': 0}
    for index, number in enumerate(input_number):  # класс
        if input_number[index] == _holder[index]:
            bulls_and_cows['Bulls'] += 1
        elif input_number[index] in _holder:
            bulls_and_cows['Cows'] += 1

    print(bulls_and_cows)
    return bulls_and_cows


def check_input_number(number):
    if number.isdigit():
        x = int(number)
        digits = set([char for char in number])
        if (1000 <= x <= 9999) and len(number) == len(digits):
            return True
        else:
            return False
    else:
        return False


def is_gameover():
    return bulls_and_cows['Bulls'] == 4

