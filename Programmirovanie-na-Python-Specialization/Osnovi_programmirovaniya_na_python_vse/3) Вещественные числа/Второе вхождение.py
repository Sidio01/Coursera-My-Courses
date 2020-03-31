s = str(input())
d = 0
pos = 0
while s.find('f', pos) != -1:
    d += 1
    if d == 2:
        print(s.find('f', pos))
    pos = s.find('f', pos) + 1
if d == 1:
    print(-1)
if d == 0:
    print(-2)
