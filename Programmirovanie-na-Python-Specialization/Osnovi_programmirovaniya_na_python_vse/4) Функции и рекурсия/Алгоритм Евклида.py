def gcd(a, b):
    if b > a:
        a, b = b, a
    if a == 0 or b == 0:
        return a + b
    return gcd(b, a % b)


a = int(input())
b = int(input())
print(gcd(a, b))
