a = list(map(int, input().split()))
x = 0
d = 1000
while x < len(a):
    if int(a[x]) > 0:
        b = a[x]
        if b < d:
            d = b
    x += 1
print(d)
