# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as house1_1
from district.central_street.house1.room2 import folks as house1_2
from district.central_street.house2.room1 import folks as house2_1
from district.central_street.house2.room2 import folks as house2_2
from district.soviet_street.house1.room1 import folks as house3_1
from district.soviet_street.house1.room2 import folks as house3_2
from district.soviet_street.house2.room1 import folks as house4_1
from district.soviet_street.house2.room2 import folks as house4_2

peoples_list = house1_1 + house1_2 + house2_1 + house2_2 + house3_1 + house3_2 + house4_1 + house4_2
print('На районе живут:', ", ".join(peoples_list))

# это в таком виде должно быть?) да :)
#зачет!

