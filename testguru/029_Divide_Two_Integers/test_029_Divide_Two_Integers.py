import pytest
from solution import Solution

def test_divide_by_zero():
    # Test case for divisor equals to zero
    s = Solution()
    assert s.divide(10, 0) == 2147483647

def test_dividend_equals_to_zero():
    # Test case for dividend equals to zero
    s = Solution()
    assert s.divide(0, 5) == 0

def test_positive_dividend_and_divisor():
    # Test case for positive dividend and divisor
    s = Solution()
    assert s.divide(18, 3) == 6

def test_negative_dividend_and_divisor():
    # Test case for negative dividend and divisor
    s = Solution()
    assert s.divide(-18, -3) == 6

def test_negative_dividend_and_positive_divisor():
    # Test case for negative dividend and positive divisor
    s = Solution()
    assert s.divide(-18, 3) == -6

def test_max_dividend_and_divisor():
    # Test case for maximum values of dividend and divisor
    s = Solution()
    assert s.divide(2147483647, 1) == 2147483647

def test_min_dividend_and_divisor():
    # Test case for minimum values of dividend and divisor
    s = Solution()
    assert s.divide(-2147483648, -1) == 2147483647