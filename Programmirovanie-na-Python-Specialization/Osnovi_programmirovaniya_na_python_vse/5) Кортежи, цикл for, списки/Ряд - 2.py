a = int(input())
b = int(input())
c = b + 1
d = b - 1
if a < b:
    print(*tuple(range(a, c)))
else:
    print(*tuple(range(a, d, -1)))
