import math
# int - отбросить дробную часть, round - до ближайшего целого (если 0.5, то к четному)
# floor - в меньшую сторону, ceil - в большую
# from "библиотека" import *(Звездочка) - импортировать все функции
n = float(input())
print(math.floor(n))
print(n)
print(int(n))
print(math.ceil(n))
print(n % 10)
print(round(n - int(n), 6))
