def MinDivisor(n):
    i = 1
    while i <= n ** (1 / 2):
        i = i + 1
        if n % i == 0:
            return i
    return n


n = int(input())
print(MinDivisor(n))
