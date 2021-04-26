"""
Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :

 "(p1**n1)(p2**n2)...(pk**nk)"
where a ** b means a to the power of b

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

from icecream import ic


def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True


def get_prime_list(n):
    li = set()
    for i in range(int(n**0.5)):
        if is_prime(i):
            li.add(i)
    return sorted(li)


def prime_factors(n):
    if is_prime(n):
        return f'({n})'
    else:
        li = get_prime_list(n)
        result = 1
        result_str = ''
        for i in li:
            x = 1
            if n % (i**x) == 0:
                while n % (i**x) == 0:
                    x += 1
                result *= i**(x-1)
                result_str += f'({i}**{x-1})' if (x-1) > 1 else f'({i})'
            else:
                continue
            if result >= n:
                break
        if is_prime(n // result):
            result_str += f'({n // result})'
        if result_str == '':
            return n
        return result_str


ic(prime_factors(86240)) # Standart Tests
ic(prime_factors(18195729)) # Small Tests
ic(prime_factors(933555431)) # Small Tests - (7537)(123863)
ic(prime_factors(6235472)) # Extremely Big Tests - 6235472
ic(is_prime(6235472))
print(get_prime_list(30554))
