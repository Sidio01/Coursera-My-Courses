i = input()
a = 0
b = int(i)
c = set()
y = set()
for x in range(b + 1):
    c.add(x)
c.remove(0)
while i != 'HELP':
    i = input()
    if i == 'HELP':
        break
    if i == 'YES':
        c &= y
    if i == 'NO':
        c -= y
    if i != 'YES' and i != 'NO':
        y = set(map(int, i.split()))
    else:
        y = set(i.split())
    a += 1
d = list(c)
d.sort()
print(*d)
