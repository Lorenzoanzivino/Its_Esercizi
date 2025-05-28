from my_project.calculator import Calculator
import pytest
@pytest.fixture

def test_addition():
    calculation: Calculator = Calculator(10, 5)
    assert calculation.addition() == 13, "The sum is wrong"

def test_subtraction():
    Calculation: Calculator = Calculator(10, 5)
    assert Calculation.subtraction() == 5, "The substraction is wrong"

def test_multiplication():
    Calculation: Calculator = Calculator(10, 5)
    assert Calculation.multiplication() == 50, "The multiplication is wrong"

def test_division():
    Calculation: Calculator = Calculator(10, 5)
    assert Calculation.division() == 2.00, "The quotient is wrong"