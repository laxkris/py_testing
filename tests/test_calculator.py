"""
Unit test for calculator
"""


import my_functions.calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == my_functions.calculator.add(2, 2)

    def test_subtraction(self):
        assert 6 == my_functions.calculator.subtract(9, 3)
