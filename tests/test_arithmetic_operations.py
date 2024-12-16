import pytest


class TestArithmeticOperations:
    """Test suite for arithmetic operations"""

    def test_addition(self):
        """Test addition operation"""
        from arithmetics_server import Addition
        addition = Addition()
        assert addition.calculate(5, 3) == 8
        assert addition.calculate(-1, 1) == 0
        assert pytest.approx(addition.calculate(0.5, 0.7)) == 1.2

    def test_subtraction(self):
        """Test subtraction operation"""
        from arithmetics_server import Subtraction
        subtraction = Subtraction()
        assert subtraction.calculate(5, 3) == 2
        assert subtraction.calculate(-1, 1) == -2
        assert pytest.approx(subtraction.calculate(0.5, 0.7)) == -0.2

    def test_multiplication(self):
        """Test multiplication operation"""
        from arithmetics_server import Multiplication
        multiplication = Multiplication()
        assert multiplication.calculate(5, 3) == 15
        assert multiplication.calculate(-1, 1) == -1
        assert pytest.approx(multiplication.calculate(0.5, 0.7)) == 0.35

    def test_division(self):
        """Test division operation"""
        from arithmetics_server import Division
        division = Division()
        assert division.calculate(6, 3) == 2
        assert division.calculate(-6, 2) == -3
        assert pytest.approx(division.calculate(0.6, 0.2)) == 3.0

        with pytest.raises(ValueError):
            division.calculate(5, 0)