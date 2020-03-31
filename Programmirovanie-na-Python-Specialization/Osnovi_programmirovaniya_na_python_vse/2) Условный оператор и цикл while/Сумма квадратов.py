n = int(input())
i = 0
sumK = 0
while i < n:
    i = i + 1
    k = i ** 2
    sumK += k
    if i >= n:
        print(sumK)
