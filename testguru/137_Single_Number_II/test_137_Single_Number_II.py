import pytest

from solution import Solution

# test cases
test_cases = [
    ([2,2,3,2], 3),
    ([0,1,0,1,0,1,99], 99),
]

@pytest.mark.parametrize("nums, expected", test_cases)
def test_singleNumber(nums, expected):
    sol = Solution()
    assert sol.singleNumber(nums) == expected