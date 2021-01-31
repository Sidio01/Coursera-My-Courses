a = list(map(int, input().split()))
y = a.index(max(a))
z = a.index(min(a))
a[y], a[z] = a[z], a[y]
print(*a)
