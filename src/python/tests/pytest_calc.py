import sys, os

from pathlib import Path
import sys

sys.path.append(os.path.realpath(os.path.dirname(__file__)+"/.."))
from calc import Calc

calc = Calc()

def test_add():
    assert calc.add(8, 5) == 13
    assert calc.add(-8, 6) == -2
    assert calc.add(-2, -4) == -6

def test_sub():
    assert calc.sub(8, 5) == 3
    assert calc.sub(1, 6) == -5
    assert calc.sub(-8, 6) == -14
    assert calc.sub(-2, -4) == 2

def test_mul():
    assert calc.mul(1, 4) == 4
    assert calc.mul(-8, 6) == -48
    assert calc.mul(-2, -4) == 8

def test_div():
    assert calc.div(3, 1) == 3
    assert calc.div(-4, 2) == -2
    assert calc.div(-15, -5) == 3
