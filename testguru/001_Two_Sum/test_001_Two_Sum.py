import pytest

from solution import Solution


def test_twoSum():
    s = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    assert s.twoSum(nums, target) == [0, 1]

    nums = [3, 2, 4]
    target = 6
    assert s.twoSum(nums, target) == [1, 2]

    nums = [3, 3]
    target = 6
    assert s.twoSum(nums, target) == [0, 1]

    nums = [-1, 0, 1, 2, -1, -4]
    target = -1
    assert s.twoSum(nums, target) == [0, 5]

    nums = [1, 2, 3, 4, 5]
    target = 10
    assert s.twoSum(nums, target) == [3, 4]