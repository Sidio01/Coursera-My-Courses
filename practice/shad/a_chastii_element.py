"""
A. Частый элемент
Ограничение времени	2 секунды
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отправить на проверку нужно исходный код программы, решающей поставленную задачу.

Дан массив a из n целых чисел. Напишите программу, которая найдет число, которое встречается в массиве наибольшее число раз.

Формат ввода
В первой строке входных данных записано число n (1 ≤ n ≤ 300 000). Во второй строке записаны n целых чисел ai (0 ≤ ai ≤ 1 000 000 000).

Формат вывода
Выведите единственное число x, наибольшее из чисел, которое встречается в a максимальное количество раз.
"""
from collections import Counter
import re


def chastii_element(x, y):
    counter_y = Counter(y)
    max = sorted(counter_y.items(), key=lambda x: (
        x[1], int(x[0])), reverse=True)
    return max[0][0]


with open('input.txt', 'r') as rfile:
    li = [i for i in rfile.readlines()]
    x = int(li[0])
    y = re.split('\s', li[1])
    result = chastii_element(x, y)
    with open('output.txt', 'w') as wfile:
        wfile.write(result)
