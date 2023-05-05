import pytest
from solution import Solution

def test_findMissingRanges_simple():
    s = Solution()
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    expected_output = ["2", "4->49", "51->74", "76->99"]
    assert s.findMissingRanges(nums, lower, upper) == expected_output

def test_findMissingRanges_empty():
    s = Solution()
    nums = []
    lower = 1
    upper = 1
    expected_output = ["1"]
    assert s.findMissingRanges(nums, lower, upper) == expected_output

def test_findMissingRanges_full():
    s = Solution()
    nums = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lower = -15
    upper = 15
    expected_output = ["-15->-11", "-10->10", "11->15"]
    assert s.findMissingRanges(nums, lower, upper) == expected_output

def test_findMissingRanges_single():
    s = Solution()
    nums = [5]
    lower = 0
    upper = 9
    expected_output = ["0->4", "6->9"]
    assert s.findMissingRanges(nums, lower, upper) == expected_output

def test_findMissingRanges_no_missing():
    s = Solution()
    nums = [0, 1, 2, 3, 4, 5, 6]
    lower = 0
    upper = 6
    expected_output = []
    assert s.findMissingRanges(nums, lower, upper) == expected_output