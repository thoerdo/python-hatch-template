import unittest

import arithmetic.add
import arithmetic.divide
import arithmetic.multiply
import arithmetic.subtract


class TestArithmetic(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(arithmetic.add.add(1, 2), 3)

    def test_subtraction(self):
        self.assertEqual(arithmetic.subtract.subtract(3, 1), 2)

    def test_mulitply(self):
        self.assertEqual(arithmetic.multiply.multiply(4, 2), 8)

    def test_divide(self):
        self.assertEqual(arithmetic.divide.divide(4, 2), 2)
