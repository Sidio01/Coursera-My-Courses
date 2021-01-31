enter = open('input.txt', 'r', encoding='utf8')
outer = open('output.txt', 'w', encoding='utf8')
lines = enter.readlines()

out = []
for line in lines:
    bet = line.split()
    out.append((bet[0], bet[1], bet[3]))


def first(a):
    return a[0]


z = []
out.sort(key=first)
for i in range(len(out)):
    z.append(out[i][0] + ' ' + out[i][1] + ' ' + out[i][2])
for now in range(len(z)):
    print(z[now], file=outer)
