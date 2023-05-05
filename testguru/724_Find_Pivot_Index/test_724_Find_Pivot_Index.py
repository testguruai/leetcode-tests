import pytest

from solution import Solution

def test_pivotIndex():
    s = Solution()

    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1
    assert s.pivotIndex([2, 1, -1]) == 0
    assert s.pivotIndex([2, 3, 4, 4]) == -1
    assert s.pivotIndex([-1, -1, -1, -1, -1, 0]) == 2
