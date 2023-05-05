import pytest

from solution import Solution


@pytest.fixture()
def solution():
    return Solution()

@pytest.mark.parametrize("nums, expected_output", [
    ([3, 10, 5, 25, 2, 8], 28),
    ([1, 2, 3], 3),
    ([1, 1, 1, 1, 1], 0),
    ([1], 0),
    ([2**31-1, 2**31-2], 1),
])
def test_solution_findMaximumXOR(solution, nums, expected_output):
    assert solution.findMaximumXOR(nums) == expected_output