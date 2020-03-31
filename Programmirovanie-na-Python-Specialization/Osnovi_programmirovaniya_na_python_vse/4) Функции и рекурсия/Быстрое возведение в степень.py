def power(a, n):
    if n != 0:
        if n % 2 == 0:
            return power(a * a, n / 2)
        if n % 2 != 0:
            return a * power(a, n - 1)
    return 1


a = float(input())
n = int(input())
print(power(a, n))
