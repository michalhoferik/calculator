

import unittest
from main import do_calculation

class CalculatorTest(unittest.TestCase):

    def test_calc_add(self):
        res = do_calculation(1, 2, "+")
        self.assertEqual(res, 3)

    def test_calc_sub(self):
        res = do_calculation(1, 2, "-")
        self.assertEqual(res, -1)

    def test_calc_mul(self):
        res = do_calculation(1, 2, "*")
        self.assertEqual(res, 2)

    def test_calc_div(self):
        res = do_calculation(1, 2, "/")
        self.assertEqual(res, 0.5)
