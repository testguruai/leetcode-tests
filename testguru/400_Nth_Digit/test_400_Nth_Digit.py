import pytest
from solution import Solution

def test_findNthDigit():
    solution = Solution()
    assert solution.findNthDigit(3) == 3
    assert solution.findNthDigit(11) == 0
    assert solution.findNthDigit(12) == 1
    assert solution.findNthDigit(100) == 5
    assert solution.findNthDigit(1000) == 3