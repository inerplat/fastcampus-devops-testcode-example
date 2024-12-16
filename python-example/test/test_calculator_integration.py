import pytest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import Calculator


class TestCalculatorIntegration:
    def setup_method(self):
        self.calculator = Calculator()

    def test_complex_calculation(self):
        # (10 + 5) * 2 = 30
        result1 = self.calculator.add(10, 5)
        assert self.calculator.multiply(result1, 2) == 30

        # (20 - 5) / 3 = 5
        result2 = self.calculator.subtract(20, 5)
        assert self.calculator.divide(result2, 3) == 5.0
