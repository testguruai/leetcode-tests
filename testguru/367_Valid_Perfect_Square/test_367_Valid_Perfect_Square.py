import pytest
from solution import Solution

def test_case1():
    sol = Solution()
    assert sol.isPerfectSquare(16) == True

def test_case2():
    sol = Solution()
    assert sol.isPerfectSquare(14) == False

def test_case3():
    sol = Solution()
    assert sol.isPerfectSquare(0) == True

def test_case4():
    sol = Solution()
    assert sol.isPerfectSquare(1) == True