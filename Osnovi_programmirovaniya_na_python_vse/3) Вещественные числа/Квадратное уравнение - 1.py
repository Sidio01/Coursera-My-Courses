a = float(input())
b = float(input())
c = float(input())
# ax ** 2 + bx + c = 0
d = b ** 2 - 4 * a * c
if d < 0:
    print('')
elif d == 0:
    x = -b / (2 * a)
    print('{0:.6f}'.format(x))
elif d > 0:
    x1 = (-b + d ** (1/2)) / (2 * a)
    x2 = (-b - d ** (1 / 2)) / (2 * a)
    xMax = max(x1, x2)
    xMin = min(x1, x2)
    print('{0:.6f}'.format(xMin), '{0:.6f}'.format(xMax))
