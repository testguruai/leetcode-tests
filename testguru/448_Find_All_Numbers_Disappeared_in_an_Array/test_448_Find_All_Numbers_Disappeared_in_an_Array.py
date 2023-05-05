import pytest

from solution import Solution


@pytest.fixture
def solution():
    return Solution()


def test_findDisappearedNumbers_1(solution):
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    expected_result = [5, 6]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_2(solution):
    nums = [1, 2, 3, 4, 5]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_3(solution):
    nums = [5, 4, 3, 2, 1]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_4(solution):
    nums = [1, 1, 1, 1, 1]
    expected_result = [2, 3, 4, 5]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_5(solution):
    nums = []
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_6(solution):
    nums = [1]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_7(solution):
    nums = [1, 1]
    expected_result = [2]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_8(solution):
    nums = [2, 2]
    expected_result = [1]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_9(solution):
    nums = [-4, -3, -2, -7, -8, -2, -3, -1]
    expected_result = [4, 5, 6, 7]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_10(solution):
    nums = [-1, -2, -3, -4, -5]
    expected_result = [1, 2, 3, 4, 5]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_11(solution):
    nums = [-5, -4, -3, -2, -1]
    expected_result = [1, 2, 3, 4, 5]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_12(solution):
    nums = [-1, -1, -1, -1, -1]
    expected_result = [1, 2, 3, 4, 5]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_13(solution):
    nums = [1, 1, 1, 1, 1, -2, -3, -4, -5]
    expected_result = [2, 3, 4, 5, 6, 7, 8]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_14(solution):
    nums = [1, 1, 1, 1, 1, 2, 3, 4, 5]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_15(solution):
    nums = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_16(solution):
    nums = [1, 2, 3, 4, 5, -2, -3, -4, -5]
    expected_result = [1]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_17(solution):
    nums = [1, 2, 3, 4, 5, -1, -2, -3, -4]
    expected_result = [5]
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_18(solution):
    nums = [1, 2]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_19(solution):
    nums = [2, 1]
    expected_result = []
    assert solution.findDisappearedNumbers(nums) == expected_result


def test_findDisappearedNumbers_20(solution):
    nums = [1, 1, 2, 2]
    expected_result = [3, 4]
    assert solution.findDisappearedNumbers(nums) == expected_result