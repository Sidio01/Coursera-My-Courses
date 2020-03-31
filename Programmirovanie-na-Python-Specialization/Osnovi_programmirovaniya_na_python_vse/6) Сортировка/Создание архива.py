s = list(map(int, input().split()))
b = []
i = 1
while i <= s[1]:
    n = int(input())
    b.append(n)
    i += 1
z = len(b)
i = 0
si = s[0]
d = 0
while i < z:
    y = min(b)
    si -= y
    if si < 0:
        print(d)
        break
    d += 1
    b.remove(y)
    i += 1
if si >= 0:
    print(d)
