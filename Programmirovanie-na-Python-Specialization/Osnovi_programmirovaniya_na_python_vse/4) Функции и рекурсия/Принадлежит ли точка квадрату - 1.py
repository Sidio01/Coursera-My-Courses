def isPointInSquare(x, y):
    while -1 <= x <= 1 and -1 <= y <= 1:
        return 'YES'
    return 'NO'


x = float(input())
y = float(input())
print(isPointInSquare(x, y))
