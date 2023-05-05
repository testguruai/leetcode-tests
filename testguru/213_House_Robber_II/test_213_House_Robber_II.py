import pytest

from solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "nums, expected_outcome",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([2, 1, 1, 2], 4),
        ([2, 1, 3, 4, 5], 8),
        ([1], 1),
        ([1, 2], 2),
        ([1, 2, 3], 3),
        ([1, 2, 3, 4], 6),
        ([1, 3, 1], 3),
        ([3, 1, 1], 3),
        ([0], 0),
        ([], 0)
    ]
)
def test_rob(solution, nums, expected_outcome):
    assert solution.rob(nums) == expected_outcome