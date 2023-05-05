import pytest
from solution import Solution

def test_minIncrementForUnique_case1():
    s = Solution()
    assert s.minIncrementForUnique([3,2,1,2,1,7]) == 6

def test_minIncrementForUnique_case2():
    s = Solution()
    assert s.minIncrementForUnique([0,2,2]) == 1

def test_minIncrementForUnique_case3():
    s = Solution()
    assert s.minIncrementForUnique([]) == 0

def test_minIncrementForUnique_case4():
    s = Solution()
    assert s.minIncrementForUnique([1]) == 0

def test_minIncrementForUnique_case5():
    s = Solution()
    assert s.minIncrementForUnique(None) == 0