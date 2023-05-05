import pytest
from solution import Solution

def test_totalFruit1():
    s = Solution()
    res = s.totalFruit([1,2,1])
    assert res == 3

def test_totalFruit2():
    s = Solution()
    res = s.totalFruit([0,1,2,2])
    assert res == 3

def test_totalFruit3():
    s = Solution()
    res = s.totalFruit([1,2,3,2,2])
    assert res == 4

def test_totalFruit4():
    s = Solution()
    res = s.totalFruit([3,3,3,1,2,1,1,2,3,3,4])
    assert res == 5

def test_totalFruit5():
    s = Solution()
    res = s.totalFruit([])
    assert res == 0