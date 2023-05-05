
from typing import List
from solution import Solution

s = Solution()

def test_maxArea():
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert s.maxArea([1, 1]) == 1
    assert s.maxArea([4, 3, 2, 1, 4]) == 16
    assert s.maxArea([1, 2, 1]) == 2
