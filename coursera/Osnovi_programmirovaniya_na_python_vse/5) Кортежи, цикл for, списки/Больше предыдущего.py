a = list(map(int, input().split()))
x = 1
while x < len(a):
    if int(a[x]) > int(a[x - 1]):
        print(a[x], end=' ')
    x += 1
