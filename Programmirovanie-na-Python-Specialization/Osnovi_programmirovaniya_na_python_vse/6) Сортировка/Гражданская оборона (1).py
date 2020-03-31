n = int(input())
ni = list(map(int, input().split()))
m = int(input())
mi = list(map(int, input().split()))
a = sorted(ni)
b = sorted(mi)
i = 0
j = 0
listn = ni
while i < len(ni):
    x = a[i]
    y = b[j]
    ai = ni.index(a[i])
    bi = mi.index(b[j]) + 1
    if y == max(mi):
        br1 = abs(b[j] - a[i])
        br2 = abs(b[j] - a[i])
    else:
        br1 = abs(b[j] - a[i])
        br2 = abs(b[j + 1] - a[i])
    if x <= y:
        listn[ai] = bi
        i += 1
    elif x == max(ni) and y == max(mi):
        listn[ai] = bi
        break
    else:
        if br2 >= br1:
            listn[ai] = bi
            i += 1
        j += 1
print(*listn)
