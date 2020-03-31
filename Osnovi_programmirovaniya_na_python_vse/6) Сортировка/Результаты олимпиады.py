class Man:
    name = 0
    grade = ''


p = []
g = int(input())
for i in range(g):
    n, g = input().split()
    g = int(g)
    man = Man()
    man.name = n
    man.grade = g
    p.append(man)


def makeTuple(man):
    return (-man.grade, man.name)


p.sort(key=makeTuple)
for now in p:
    print(now.name)
