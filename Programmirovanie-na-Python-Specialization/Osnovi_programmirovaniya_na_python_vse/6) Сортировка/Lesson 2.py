p = [(-172, 'Vasya'),
     (-180, 'Petya'),
     (-172, 'Fedya')]
p.sort()
for i in range(len(p)):
    p[i] = (-p[i][0], p[i][1])
print(*p)

ls = ['abcd', 'bc', '1234']
ls.sort(key=len)
print(*ls)

points = [
    (1, 1),
    (10, 1),
    (5, 5)
]


def sqrDist(point):
    return point[0] ** 2 + point[1] ** 2


points.sort(key=sqrDist)
print(*points)

a = [(172, 'Vasya'),
     (180, 'Petya'),
     (172, 'Fedya')]


def makeTuple(man):
    return (-man[0], man[1])


a.sort(key=makeTuple)
print(*a)

b = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
c = sorted(b)
d = c[2]
e = b.index(c[2])
i = 0
y = []
while i < len(b):
    y.append(b.index(c[i]) + 1)
    i += 1
print(c)
print(d)
print(e)
print(y)
