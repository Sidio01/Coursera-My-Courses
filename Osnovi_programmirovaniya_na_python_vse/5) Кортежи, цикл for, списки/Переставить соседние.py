a = list(map(int, input().split()))
d = 1
while d < len(a):
    a[d - 1], a[d] = a[d], a[d - 1]
    d += 2
print(*a)
