import pytest
from solution import Solution

def test_hIndex_sort():
    sol = Solution()
    assert sol.hIndex([3,0,6,1,5]) == 3
    assert sol.hIndex([]) == 0
    assert sol.hIndex([1]) == 1
    assert sol.hIndex([0]) == 0
    assert sol.hIndex([0, 1]) == 1

def test_hIndex_counting():
    sol = Solution()
    assert sol.hIndex([3,0,6,1,5]) == 3
    assert sol.hIndex([]) == 0
    assert sol.hIndex([1]) == 1
    assert sol.hIndex([0]) == 0
    assert sol.hIndex([0, 1]) == 1
