n = int(input())
for x in range(1, n + 1):
    print(*range(1, x + 1), sep='')
