
import pytest
from solution import Solution

def test_empty_range():
    sol = Solution()
    res = sol.selfDividingNumbers(1, 0)
    assert res == []

def test_single_self_dividing():
    sol = Solution()
    res = sol.selfDividingNumbers(1, 1)
    assert res == [1]

def test_single_non_self_dividing():
    sol = Solution()
    res = sol.selfDividingNumbers(10, 10)
    assert res == []

def test_multiple_self_dividing():
    sol = Solution()
    res = sol.selfDividingNumbers(1, 22)
    assert res == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

def test_multiple_non_self_dividing():
    sol = Solution()
    res = sol.selfDividingNumbers(22, 24)
    assert res == []
