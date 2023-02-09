#!/usr/bin/env python3
import unittest
import calculator

calc = calculator.Calculator()


class Tests(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-7, 4), -3)
        self.assertEqual(calc.add(-1, 0), -1)
        self.assertEqual(calc.add(-3, -3), -6)

    def test_substraction(self):
        self.assertEqual(calc.sub(8, 3), 5)
        self.assertEqual(calc.sub(8, 9), -1)
        self.assertEqual(calc.sub(2, -5), 7)

    def test_multiplication(self):
        self.assertEqual(calc.mul(12, 8), 96)
        self.assertEqual(calc.mul(0, 5), 0)

    def test_division(self):
        self.assertEqual(calc.div(42, 6), 7)
        self.assertRaises(ZeroDivisionError, calc.div(42, 0))

    def test_remainder(self):
        self.assertEqual(calc.rem(23, 5), 3)
        self.assertRaises(ZeroDivisionError, calc.rem(42, 0))

    def test_squareroot(self):
        self.assertEqual(calc.sqrt(9), 3)
        self.assertEqual(calc.sqrt(0), 0)

    def test_checksum(self):
        self.assertEqual(calc.checksum(9), 0)
        self.assertEqual(calc.checksum(5), 0)
        self.assertNotEqual(calc.checksum(9), calc.checksum(3))

    def test_band(self):
        self.assertEqual(calc.band(7, 9), 1)

    def test_bor(self):
        self.assertEqual(calc.bor(5, 6), 7)

    def test_bxor(self):
        self.assertEqual(calc.bxor(3, 1), 2)

    def test_bnot(self):
        self.assertEqual(calc.bnot(9), -10)

    def test_bshl(self):
        self.assertEqual(calc.bshl(9, 1), 18)

    def test_bshr(self):
        self.assertEqual(calc.bshr(9, 1), 4)









