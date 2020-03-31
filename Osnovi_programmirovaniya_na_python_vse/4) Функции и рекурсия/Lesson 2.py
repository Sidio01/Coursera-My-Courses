def max2(a, b):
    if a > b:
        return a
    return b


def max3(a, b, c):
    return max2(max2(a, b), c)


def sort2(a, b):
    if a < b:
        return a, b
    return b, a


def iseven(n):
    return n % 2 == 0


n = int(input())
if iseven(n):
    print('EVEN')
else:
    print('ODD')
minimum, maximum = sort2(5, 4)
print(max2(2, 5))
print(max2(6, 5))
print(max2(3, 3))
print(max3(1, 4, 3))
print(minimum, maximum)
