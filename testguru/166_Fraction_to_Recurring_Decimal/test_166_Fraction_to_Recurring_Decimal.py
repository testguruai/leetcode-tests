import pytest
from solution import Solution

@pytest.fixture
def solution_instance():
    return Solution()

def test_fraction_to_decimal_zero(solution_instance):
    assert solution_instance.fractionToDecimal(0, 5) == '0'

def test_fraction_to_decimal_positive(solution_instance):
    assert solution_instance.fractionToDecimal(12, 5) == '2.4'

def test_fraction_to_decimal_negative(solution_instance):
    assert solution_instance.fractionToDecimal(-12, 5) == '-2.4'

def test_fraction_to_decimal_recurring(solution_instance):
    assert solution_instance.fractionToDecimal(1, 3) == '0.(3)'

def test_fraction_to_decimal_integer(solution_instance):
    assert solution_instance.fractionToDecimal(5, 1) == '5.0'