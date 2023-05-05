import pytest
from solution import Solution

def test_findShortestSubArray():
    solution = Solution()
    assert solution.findShortestSubArray([1, 2, 2, 3, 1]) == 2
    assert solution.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6
    assert solution.findShortestSubArray([1, 2, 3, 4, 5]) == 1
    assert solution.findShortestSubArray([1, 2, 3, 2, 1]) == 5
    assert solution.findShortestSubArray([1]) == 1
    assert solution.findShortestSubArray([]) == 0
    assert solution.findShortestSubArray([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]) == 9

def test_smallestSubArray():
    solution = Solution()
    assert solution.smallestSubArray([1, 2, 2, 3, 1], 2, 2) == 2
    assert solution.smallestSubArray([1, 2, 2, 3, 1, 4, 2], 2, 3) == 3
    assert solution.smallestSubArray([1, 2, 3, 4, 5], 1, 1) == 1
    assert solution.smallestSubArray([1, 2, 3, 2, 1], 1, 2) == 5
    assert solution.smallestSubArray([1], 1, 1) == 1
    assert solution.smallestSubArray([], 0, 0) == 0
    assert solution.smallestSubArray([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], 5, 10) == 10
