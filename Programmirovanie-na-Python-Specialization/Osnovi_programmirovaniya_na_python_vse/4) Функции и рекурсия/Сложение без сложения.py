def sum(x, y):
    if y == 0:
        return x
    return sum(x + 1, y - 1)


a = int(input())
b = int(input())
print(sum(a, b))
