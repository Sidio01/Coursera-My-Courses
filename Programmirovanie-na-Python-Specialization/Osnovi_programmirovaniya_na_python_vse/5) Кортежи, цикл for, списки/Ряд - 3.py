n = int(input())
b = len(str(n))
a = 10 ** (b - 1) - 1
c = str('9') * b
print(*tuple(range(int(c), a, -2)))
