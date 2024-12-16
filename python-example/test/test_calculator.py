import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import Calculator


class TestCalculator:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add(self):
        assert self.calculator.add(2, 3) == 5
        assert self.calculator.add(-4, 3) == -1

    def test_subtract(self):
        assert self.calculator.subtract(2, 3) == -1
        assert self.calculator.subtract(-4, 3) == -7

    def test_multiply(self):
        assert self.calculator.multiply(2, 3) == 6
        assert self.calculator.multiply(-4, 3) == -12

    def test_divide(self):
        assert self.calculator.divide(6, 3) == 2.0
        assert self.calculator.divide(-6, 3) == -2.0
        with pytest.raises(ValueError):
            self.calculator.divide(4, 0)
