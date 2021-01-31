a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
m1 = abs(a1 - a2)
m2 = abs(b1 - b2)
if 0 <= m1 <= 1 and 0 <= m2 <= 1:
    print('YES')
else:
    print('NO')
