x = list(map(int, input().split()))
y = list(map(int, input().split()))
a = set(x)
b = set(y)
c = list(a & b)
print(*sorted(c))
