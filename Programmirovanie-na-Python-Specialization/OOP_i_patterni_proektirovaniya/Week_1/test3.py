import unittest


def gcd(a, b):
    assert isinstance(a, int) and isinstance(b, int)
    assert a > 0 and b > 0
    while b != 0:
        r = a % b
        b = a
        a = r
    return a


print(gcd(10, 3))


class TestFactorization(unittest.TestCase):
    def test_simple_multipliers(self):
        x = 77
        a, b = factorize(x)
        self.assertEqual(a * b, x)