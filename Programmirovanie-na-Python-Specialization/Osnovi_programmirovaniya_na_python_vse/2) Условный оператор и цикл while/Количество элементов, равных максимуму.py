n = int(input())
nMax = n
d = 0
while n != 0:
    if n > nMax:
        nMax, d = n, 1
    elif n == nMax:
        d += 1
    n = int(input())
print(d)
