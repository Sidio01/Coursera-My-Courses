n = int(input())
a = list(map(int, input().split()))
x = int(input())
d = 0
b = []
while d < n:
    z = a[d] - x
    b.append(abs(z))
    d += 1
y = b.index(min(b))
print(a[y])
