import sys, os

from pathlib import Path
import sys
import unittest

#sys.path.append(os.path.realpath(os.path.dirname(__file__)))
sys.path.append(os.path.realpath('..'))
from calc import Calc

class UnitestCalc(unittest.TestCase):
    def test_add(self):
        calc = Calc()
        self.assertEqual(13, calc.add(8, 5))
        self.assertEqual(-2, calc.add(-8, 6))
        self.assertEqual(-6, calc.add(-2, -4))

    def test_sub(self):
        calc = Calc()
        self.assertEqual(3, calc.sub(8, 5))
        self.assertEqual(-5, calc.sub(1, 6))
        #self.assertEqual(-14, calc.sub(-8, 6))
        self.assertEqual(-12, calc.sub(-8, 6))
        self.assertEqual(2, calc.sub(-2, -4))

    def test_mul(self):
        calc = Calc()
        self.assertEqual(4, calc.mul(1, 4))
        self.assertEqual(-48, calc.mul(-8, 6))
        self.assertEqual(8, calc.mul(-2, -4))

    def test_div(self):
        calc = Calc()
        self.assertEqual(3, calc.div(3, 1))
        self.assertEqual(-2, calc.div(-4, 2))
        self.assertEqual(3, calc.div(-15, -5))
