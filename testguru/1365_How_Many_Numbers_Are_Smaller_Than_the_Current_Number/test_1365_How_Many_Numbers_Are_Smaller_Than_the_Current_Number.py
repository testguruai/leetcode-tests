import pytest

from .solution import Solution


@pytest.fixture
def solution():
    return Solution()


def test_smallerNumbersThanCurrent_sorted(solution):
    nums = [1, 2, 3, 4, 5]
    expected = [0, 1, 2, 3, 4]
    assert solution.smallerNumbersThanCurrent(nums) == expected


def test_smallerNumbersThanCurrent_unsorted(solution):
    nums = [5, 3, 1, 4, 2]
    expected = [4, 2, 0, 3, 1]
    assert solution.smallerNumbersThanCurrent(nums) == expected


def test_smallerNumbersThanCurrent_duplicates(solution):
    nums = [2, 2, 3, 4, 5]
    expected = [0, 0, 1, 2, 3]
    assert solution.smallerNumbersThanCurrent(nums) == expected


def test_smallerNumbersThanCurrent_all_same(solution):
    nums = [1, 1, 1, 1]
    expected = [0, 0, 0, 0]
    assert solution.smallerNumbersThanCurrent(nums) == expected


def test_smallerNumbersThanCurrent_one_number(solution):
    nums = [5]
    expected = [0]
    assert solution.smallerNumbersThanCurrent(nums) == expected


def test_smallerNumbersThanCurrent_zero_in_list(solution):
    nums = [1, 2, 0, 4, 5]
    expected = [0, 1, 0, 2, 3]
    assert solution.smallerNumbersThanCurrent(nums) == expected