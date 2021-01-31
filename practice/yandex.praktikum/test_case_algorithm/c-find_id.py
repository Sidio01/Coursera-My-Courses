"""
В сервисе Киношечка зарегистрировано n пользователей.
Все пользователи, за исключением двух, в последние два
месяца посещали сайт. Нужно определить id пользователей,
которые сайт не посещали.

Формат ввода
Первая строка содержит число n — количество
зарегистрированных пользователей. Это целое число в
диапазоне от 2 до 10**6.
Во второй строке через пробел заданы различные
n - 2 целых числа. Каждое из них не превосходит n и
больше нуля.

Формат вывода
Нужно в одной строке вывести по возрастанию два
пропущенных числа, разделённые пробелом.
"""


import re

with open('input.txt', 'r') as input:
    total = []
    for line in input.readlines():
        total.append(line)
    length = re.split('[\s]', total[0])[:-1]
    row = frozenset(map(int, re.split('[\s]', total[1])[:-1]))
    check_row = frozenset(range(1, int(length[0]) + 1))
    result = sorted(list(check_row.difference(row)))
    result = str(result[0]) + ' ' + str(result[1])
    with open('output.txt', 'w') as output:
        output.write(result)
