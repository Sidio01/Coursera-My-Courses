i = input()
a1 = 0
a2 = 0
b = int(i)
c = set()
d = set()
y = set()
while a1 < b:
    i = input()
    i2 = int(i)
    c &= y
    if isinstance(i2, int):
        a2 = 0
        y = set()
        while a2 < i2:
            i = input()
            y.add(i)
            d.add(i)
            a2 += 1
    if a1 == 0:
        c = y
    a1 += 1
c &= y
print(len(c))
print('\n'.join(c))
print(len(d))
print('\n'.join(d))
