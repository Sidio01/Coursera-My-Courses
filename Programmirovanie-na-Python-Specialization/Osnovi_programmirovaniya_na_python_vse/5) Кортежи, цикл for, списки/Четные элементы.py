a = input().split()
x = 0
while x < len(a):
    if int(a[x]) % 2 == 0:
        print(a[x], end=' ')
    x += 1
