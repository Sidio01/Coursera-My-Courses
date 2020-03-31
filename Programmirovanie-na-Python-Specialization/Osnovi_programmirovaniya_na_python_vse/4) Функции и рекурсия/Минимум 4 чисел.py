def min2(a, b):
    if a < b:
        return a
    return b


def min3(a, b, c):
    return min2(min2(a, b), c)


def min4(a, b, c, d):
    return min2(min3(a, b, c), d)


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(min4(a, b, c, d))
