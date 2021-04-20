import unittest
from b_vershinnoe_pokritie import vershinnoe_pokritie

class TestB(unittest.TestCase):
    def test_vershinnoe_pokritie(self):
        cases = [
            ((9, [0, 3, 0, 1, 2, 1, 3, 1, 0]), 48304),
            ((4, [0, 0, 0, 0]), 8),
            ((3, [0, 100, 0]), 905485120)
        ]
        for i in cases:
            with self.subTest(test=i):
                self.assertEqual(vershinnoe_pokritie(i[0][0], i[0][1]), i[1])
