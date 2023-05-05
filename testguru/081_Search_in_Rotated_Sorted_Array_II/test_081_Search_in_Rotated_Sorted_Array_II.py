import pytest

from solution import Solution

# Define test cases
test_cases = [
    ([2, 5, 6, 0, 0, 1, 2], 0, True),
    ([2, 5, 6, 0, 0, 1, 2], 3, False),
    ([1], 0, False),
    ([1], 1, True),
    ([1, 3, 1, 1, 1], 3, True),
]

# Define test functions
@pytest.mark.parametrize("nums, target, expected", test_cases)
def test_search(nums, target, expected):
    sol = Solution()
    assert sol.search(nums, target) == expected
