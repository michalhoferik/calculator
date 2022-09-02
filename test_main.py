

import unittest
from main import is_input_valid

class CalculatorTest(unittest.TestCase):

    def test_input_validatio_pass(self):
        res = is_input_valid("4")
        self.assertTrue(res)

    def test_input_validatis_fail(self):
        res = is_input_valid("f")
        self.assertFalse(res)
