mySet = {1, 2, 3, 40000000}
for elem in mySet:
    print(elem)

primes = {2, 3, 5, 7, 11, 13}
n = int(input())
if n in primes:
# if not n in primes:
    print('in set')
else:
    print('not in set')

primes.add(17)
print(primes)
primes.remove(13)
# primes.discard(13)
# discard не ломает ход программы
print(primes)

a = {1, 2, 3, 4}
b = {1, 3, 5}
print(a != b)
print(a == b)
print(a < b)
print(a > b)
print(a | b)  # объединение
print(a & b)  # пересечение
print(a - b)  # Множество, элементы которого входят в A, но не входят в B
print(a ^ b)  # Элементы входят в A | B, но не входят в A & B
