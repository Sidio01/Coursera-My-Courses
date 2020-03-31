a = list(map(int, input().split()))
x = 0
y = max(a)
d = 0
while x < len(a):
    if int(a[x]) == y:
        d = x
    x += 1
print(y, d)
