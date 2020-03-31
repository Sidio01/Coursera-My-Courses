from time import time
tic = time()
n = int(input())
ni = list(map(int, input().split()))
m = int(input())
mi = list(map(int, input().split()))
a = []
b = []
am = max(ni)
bm = max(mi)
for i in range(1, n + 1):
    x = (i, ni[i - 1])
    a.append(x)
for i in range(1, m + 1):
    y = (i, mi[i - 1])
    b.append(y)
a.sort(key=lambda a: (a[1], a[0]))
b.sort(key=lambda b: (b[1], b[0]))
lena = len(a)
lenb = len(b)
i = 0
j = 0
listn = []
while i < lena:
    az = a[i][1]
    bz = b[j][1]
    if bz == bm:
        br1 = abs(b[j][1] - a[i][1])
        br2 = abs(b[j][1] - a[i][1])
    else:
        br1 = abs(b[j][1] - a[i][1])
        br2 = abs(b[j + 1][1] - a[i][1])
    if az <= bz:
        listn.append((b[j][0], a[i][0]))
        i += 1
    elif az == am and bz == bm:
        listn.append((b[j][0], a[i][0]))
        break
    else:
        if br2 >= br1:
            listn.append((b[j][0], a[i][0]))
            i += 1
        j += 1
z = list(listn)
z.sort(key=lambda z: (z[1], z[0]))
d = 0
listf = []
while d < len(z):
    listf.append(z[d][0])
    d += 1
print(a)
print(b)
print(listn)
print(*listf)
toc = time()
print(toc - tic)