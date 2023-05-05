import pytest
from solution import Solution

def test_summaryRanges_empty():
    solution = Solution()
    result = solution.summaryRanges([])
    assert result == []

def test_summaryRanges_single():
    solution = Solution()
    result = solution.summaryRanges([5])
    assert result == ["5"]

def test_summaryRanges_multiple():
    solution = Solution()
    result = solution.summaryRanges([0, 1, 2, 4, 5, 7])
    assert result == ["0->2", "4->5", "7"]

def test_summaryRanges_duplicate():
    solution = Solution()
    result = solution.summaryRanges([0, 1, 1, 2])
    assert result == ["0->2"]

def test_summaryRanges_negative():
    solution = Solution()
    result = solution.summaryRanges([-3, -2, -1, 5])
    assert result == ["-3->-1", "5"] 

def test_summaryRanges_all_same():
    solution = Solution()
    result = solution.summaryRanges([1,1,1,1,1])
    assert result == ["1"] 

def test_summaryRanges_case_insensitive():
    solution = Solution()
    result = solution.summaryRanges([44,46,47])
    assert result == ["44","46->47"] 

# test to ensure function handles large input arrays
def test_summaryRanges_large_input():
    solution = Solution()
    nums = list(range(1, 10000))
    result = solution.summaryRanges(nums)
    expected = ["1->9999"]
    assert result == expected