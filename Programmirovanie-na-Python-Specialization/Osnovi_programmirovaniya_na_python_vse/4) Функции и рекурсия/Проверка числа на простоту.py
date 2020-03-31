def MinDivisor(n):
    i = 1
    while i <= n ** (1 / 2):
        i = i + 1
        if n % i == 0:
            return i
    return n


def isPrime(n):
    if MinDivisor(n) == n:
            return 'YES'
    return'NO'


n = int(input())
print(isPrime(n))
