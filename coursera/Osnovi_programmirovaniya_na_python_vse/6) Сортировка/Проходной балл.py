enter = open('input.txt', 'r', encoding='utf8')
outer = open('output.txt', 'w', encoding='utf8')
lines = enter.readlines()

out = []
for line in lines[1:]:
    bet = line.split()
    if int(bet[-3]) >= 40 and int(bet[-2]) >= 40 and int(bet[-1]) >= 40:
        out.append(int(bet[-3]) + int(bet[-2]) + int(bet[-1]))

z = []
for i in range(len(out)):
    z.append(out[i])
z.sort()
x = int(lines[0])
y = x + 1
a = max(z)
if len(z) == x or x == 0 or x > (z.index(a) + 1):
    print(0, file=outer)
elif z[-x] == z[-y]:
    d = 0
    i = 0
    while d < len(z):
        if z[d] == a:
            i += 1
        if i > x:
            print(1, file=outer)
        d += 1
    else:
        for i in range(len(z)):
            if z[i] > z[-x]:
                print(z[i], file=outer)
                break
else:
    print(z[-x], file=outer)
