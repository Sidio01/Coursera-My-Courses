def gcd(a, b):
    if b > a:
        a, b = b, a
    if a == 0 or b == 0:
        return a + b
    return gcd(b, a % b)


def ReduceFraction(n, m):
    p = n / gcd(n, m)
    q = m / gcd(n, m)
    return int(p), int(q)


n = int(input())
m = int(input())
p, q = ReduceFraction(n, m)
print(p, q)
