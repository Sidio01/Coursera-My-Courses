import unittest
from a_chastii_element import chastii_element

class TestA(unittest.TestCase):
    def test_chastii_element(self):
        cases = [
            ((3, [3, 3, 3]), 3),
            ((5, [4, 1, 4, 3, 3]), 4),
            ((10, [10, 6, 10, 10, 10, 10, 8, 8, 10, 9]), 10),
            ((9, [10, 10, 10, 11, 11, 11, 8, 8, 8]), 11)
        ]
        for i in cases:
            with self.subTest(test=i):
                self.assertEqual(chastii_element(i[0][0], i[0][1]), i[1])
