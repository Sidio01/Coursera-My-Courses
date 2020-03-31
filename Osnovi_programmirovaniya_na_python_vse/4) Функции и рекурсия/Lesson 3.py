def rec():
    n = int(input())
    if n != 0:
        if n % 2 == 0:
            print(n)
        rec()
        if n % 2 != 0:
            print(n)


rec()


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


n = int(input())
print(factorial(n))
