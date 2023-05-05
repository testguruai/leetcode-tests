import pytest
from solution import Solution

def test_four_sum():
    s = Solution()
    assert s.fourSum([1, 0, -1, 0, -2, 2], 0) == [(-2, -1, 1, 2), (-2, 0, 0, 2), (-1, 0, 0, 1)]
    assert s.fourSum([2,2,2,2,2],8) == [(2,2,2,2)]
    assert s.fourSum([1,4,-3,0,0,0,5,0],0) == [(-3, 0, 1, 4), (-3, 0, 5, 4), (-3, 0, 0, 5), (0, 0, 1, -1), (-3, 0, 0, 4), (-1, 0, 0, 1), (-1, 0, 0, 5), (-1, 0, 5, 4), (0, 0, 4, -1), (-1, 0, 4, 5), (1, 0, 0, -1), (1, 0, 0, 5), (1, 0, 5, 4), (0, 0, -1, 1), (0, 0, -1, 5), (4, 0, -3, -1), (1, 0, -3, 4), (1, 0, -3, -1), (1, 4, -3, 0), (0, 0, 1, -3), (-1, 1, -3, 5), (0, -1, -3, 4), (-1, 0, -3, 4), (-1, 1, 0, 0), (0, -3, -1, 4), (0, 1, -3, 5), (1, -3, 0, 5), (-1, 5, -3, -1), (-1, 5, -3, 4), (1, 5, -3, 0), (1, 5, -3, 4), (0, 4, -3, -1), (0, 4, -3, 5), (-1, 1, -3, 4), (1, -3, -1, 4), (0, -1, -3, 0)]
    assert s.fourSum([1,2,3,4,5,6,7,8,9,10],19) == [(1, 2, 6, 10), (1, 3, 5, 10), (1, 4, 5, 9), (1, 4, 6, 8), (2, 3, 5, 9), (2, 3, 6, 8), (2, 4, 5, 8), (3, 4, 6, 6)]
    assert s.fourSum([0,0,0,0],0) == [(0,0,0,0)]
    assert s.fourSum([0,0,0],1) == []