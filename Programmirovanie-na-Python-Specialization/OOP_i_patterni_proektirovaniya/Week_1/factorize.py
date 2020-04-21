# import unittest
# from contracts import contract
#
#
# @contract(x='int,>=0')
# def factorize(x):
#     """
#     Factorize positive integer and return its factors
#     :type x: int,>=0
#     :rtype: tuple[N],N>0
#     """
#     pass


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        cases = ('string', 1.5)
        for b in cases:
            with self.subTest(case=b):
                self.assertRaises(TypeError, factorize, b)

    def test_negative(self):
        cases = (-1, -10, -100)
        for b in cases:
            with self.subTest(case=b):
                self.assertRaises(ValueError, factorize, b)

    def test_zero_and_one_cases(self):
        cases = (0, 1)
        for b in cases:
            with self.subTest(case=b):
                a = factorize(b)
                self.assertTupleEqual(a, (b,))

    def test_simple_numbers(self):
        cases = (3, 13, 29)
        for b in cases:
            with self.subTest(case=b):
                a = factorize(b)
                self.assertTupleEqual(a, (b,))

    def test_two_simple_multipliers(self):
        cases = ((6, (2, 3)), (26, (2, 13)), (121, (11, 11)))
        for b, answer in cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), answer)

    def test_many_multipliers(self):
        cases = ((1001, (7, 11, 13)), (9699690, (2, 3, 5, 7, 11, 13, 17, 19)))
        for b, answer in cases:
            with self.subTest(case=b):
                self.assertEqual(factorize(b), answer)
