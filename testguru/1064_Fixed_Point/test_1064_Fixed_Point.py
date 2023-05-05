import pytest
from solution import Solution

def test_fixedPoint():
    s = Solution()
    assert s.fixedPoint([0, 2, 3, 4, 5, 6, 7, 8]) == 0
    assert s.fixedPoint([-10, -5, 0, 3, 7]) == 3
    assert s.fixedPoint([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 0
    assert s.fixedPoint([0, 1, 2, 3, 4, 6, 7, 8, 9]) == -1
    assert s.fixedPoint([3, 4, 5, 6, 7, 8]) == -1

def test_fixedPoint_empty():
    s = Solution()
    assert s.fixedPoint([]) == -1

def test_fixedPoint_single():
    s = Solution()
    assert s.fixedPoint([-5]) == -1
    assert s.fixedPoint([0]) == 0
    assert s.fixedPoint([1]) == -1

def test_fixedPoint_duplicates():
    s = Solution()
    assert s.fixedPoint([0, 1, 1, 3, 4]) == 1
    assert s.fixedPoint([-5, -5, 1, 2, 3]) == 2
    assert s.fixedPoint([-1, 0, 0, 0, 3, 5, 7, 9]) == 0
