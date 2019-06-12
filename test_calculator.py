"""
Unit tests for the calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.addition(2,2)