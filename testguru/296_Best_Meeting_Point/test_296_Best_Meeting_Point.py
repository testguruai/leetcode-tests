import pytest
from solution import Solution

def test_minDistance1D():
    s = Solution()
    assert s.minDistance1D([1,2,3,4,5]) == 10
    assert s.minDistance1D([1,5]) == 4
    assert s.minDistance1D([1]) == 0

def test_collectRows():
    s = Solution()
    grid = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
    assert s.collectRows(grid) == [0, 1, 2]
    assert s.collectRows([[1,0],[0,1]]) == [0, 1]

def test_collectCols():
    s = Solution()
    grid = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
    assert s.collectCols(grid) == [0, 1, 2]
    assert s.collectCols([[1,0],[0,1]]) == [0, 1]

def test_minTotalDistance():
    s = Solution()
    grid = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
    assert s.minTotalDistance(grid) == 4
    grid = [
        [1,1],
        [1,1]
    ]
    assert s.minTotalDistance(grid) == 2