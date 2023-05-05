import pytest

from solution import Solution

def test_twoSum_positive_numbers():
    s = Solution()
    assert s.twoSum([1,2,3,4,5], 9) == [4, 5]
    assert s.twoSum([3, 4, 6, 7], 10) == [2, 4]

def test_twoSum_zero_target():
    s = Solution()
    assert s.twoSum([1,2,3,4], 0) == []

def test_twoSum_negative_numbers():
    s = Solution()
    assert s.twoSum([-3,-2,-1,0,1,2,3], -5) == [-3,-2]
    assert s.twoSum([-5,-4,-3,-2,-1,0,1,2,3,4,5], 5) == [-5, 10]

def test_twoSum_duplicate_numbers():
    s = Solution()
    assert s.twoSum([1,1,1,1,2,2,2,3,4], 5) == [6, 9]
    assert s.twoSum([1,1,1,1,2,2,3,4,4], 6) == [7, 8]
