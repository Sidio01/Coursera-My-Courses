a = input().split()
x = 0
d = 0
while x < len(a):
    if int(a[x]) > 0:
        d += 1
    x += 1
print(d)
