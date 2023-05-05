
import pytest
from solution import Solution

def test_positive_powers_of_two():
    solution = Solution()
    result = solution.isPowerOfTwo(1)
    assert result == True

    result = solution.isPowerOfTwo(2)
    assert result == True

    result = solution.isPowerOfTwo(4)
    assert result == True

    result = solution.isPowerOfTwo(8)
    assert result == True

def test_negative_powers_of_two():
    solution = Solution()
    result = solution.isPowerOfTwo(-1)
    assert result == False

    result = solution.isPowerOfTwo(-2)
    assert result == False

    result = solution.isPowerOfTwo(-4)
    assert result == False

def test_non_powers_of_two():
    solution = Solution()
    result = solution.isPowerOfTwo(0)
    assert result == False

    result = solution.isPowerOfTwo(3)
    assert result == False

    result = solution.isPowerOfTwo(10)
    assert result == False

    result = solution.isPowerOfTwo(1023)
    assert result == False
