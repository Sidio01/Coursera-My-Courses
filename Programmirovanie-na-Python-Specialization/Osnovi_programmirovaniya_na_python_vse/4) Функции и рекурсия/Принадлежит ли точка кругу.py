def isPointInCircle(x, y, xc, yc, r):
    b = ((xc - x) ** 2 + (yc - y) ** 2) ** (1 / 2)
    while b <= r:
        return 'YES'
    return 'NO'


x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())
print(isPointInCircle(x, y, xc, yc, r))
