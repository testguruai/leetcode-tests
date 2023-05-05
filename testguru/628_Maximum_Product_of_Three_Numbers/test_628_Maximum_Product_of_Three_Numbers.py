import pytest

from solution import Solution

def test_maximum_product():
    # Test case 1
    s = Solution()
    nums = [1,2,3,4]
    expected_output = 24
    assert s.maximumProduct(nums) == expected_output

    # Test case 2
    s = Solution()
    nums = [-1,-2,-3,-4,-5]
    expected_output = -6
    assert s.maximumProduct(nums) == expected_output

    # Test case 3
    s = Solution()
    nums = [-1,-2,3,4,5]
    expected_output = 40
    assert s.maximumProduct(nums) == expected_output

    # Test case 4
    s = Solution()
    nums = [0,0,0,0,0,5,6,7,8,9]
    expected_output = 0
    assert s.maximumProduct(nums) == expected_output

    # Test case 5
    s = Solution()
    nums = [1,2,-3,-4,-5]
    expected_output = 40
    assert s.maximumProduct(nums) == expected_output