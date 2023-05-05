import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxWidthRamp_case1(solution):
    assert solution.maxWidthRamp([6, 0, 8, 2, 1, 5]) == 4

def test_maxWidthRamp_case2(solution):
    assert solution.maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]) == 7

def test_maxWidthRamp_empty(solution):
    assert solution.maxWidthRamp([]) == 0

def test_maxWidthRamp_single_value(solution):
    assert solution.maxWidthRamp([5]) == 0

def test_maxWidthRamp_sorted(solution):
    assert solution.maxWidthRamp([1, 2, 3, 4, 5, 6]) == 5

def test_maxWidthRamp_reverse_sorted(solution):
    assert solution.maxWidthRamp([6, 5, 4, 3, 2, 1]) == 0

def test_maxWidthRamp_all_values_same(solution):
    assert solution.maxWidthRamp([4, 4, 4, 4, 4]) == 0

def test_maxWidthRamp_duplicate_values(solution):
    assert solution.maxWidthRamp([4, 5, 6, 4, 5, 6]) == 3

def test_maxWidthRamp_negative_values(solution):
    assert solution.maxWidthRamp([2, 4, -1, 3, -4, 0]) == 5

def test_maxWidthRamp_all_negative_values(solution):
    assert solution.maxWidthRamp([-5, -4, -3, -2, -1]) == 0

def test_maxWidthRamp_mixed_values(solution):
    assert solution.maxWidthRamp([10, 3, 8, 1, 5, 2, 7, 4, 6, 9]) == 7

def test_maxWidthRamp_large_input(solution):
    A = list(range(100001))
    assert solution.maxWidthRamp(A) == 100000