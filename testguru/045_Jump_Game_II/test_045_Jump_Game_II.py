import pytest

from ...path.to import Solution


@pytest.fixture()
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected_jump",
    [
        ([2, 3, 1, 1, 4], 2),
        ([1, 2, 3], 2),
        ([1, 1, 1, 1, 1], 4),
        ([5], 0),
        ([2, 5, 0, 0, 3, 2, 1], 3)
    ],
)
def test_jump(solution, nums, expected_jump):
    assert solution.jump(nums) == expected_jump


def test_jump_empty(solution):
    assert solution.jump([]) == 0


def test_jump_single_elem(solution):
    assert solution.jump([2]) == 0


def test_jump_duplicate_elems(solution):
    assert solution.jump([2, 2, 2, 2, 2]) == len(nums) - 1


def test_jump_one_step_at_a_time(solution):
    nums = [i + 1 for i in range(1000)]
    assert solution.jump(nums) == len(nums) - 1


def test_jump_worst_case(solution):
    nums = [i % 100 + 1 for i in range(1000)]
    assert solution.jump(nums) == 10