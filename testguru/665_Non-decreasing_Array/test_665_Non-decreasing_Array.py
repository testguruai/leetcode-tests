import pytest

from solution import Solution

def test_checkPossibility():
    s = Solution()

    # Test case where a number needs to be edited to shift the back of the array
    nums = [4, 2, 3]
    assert s.checkPossibility(nums) == True

    # Test case where two numbers need to be edited to shift the back of the array
    nums = [4, 2, 1]
    assert s.checkPossibility(nums) == False

    # Test case where a number needs to be edited to shift the front of the array
    nums = [3, 4, 2, 3]
    assert s.checkPossibility(nums) == False

    # Test case where no numbers need to be edited
    nums = [1, 2, 3, 4]
    assert s.checkPossibility(nums) == True

    # Test case where only the last number needs to be edited
    nums = [5, 7, 1, 8]
    assert s.checkPossibility(nums) == True

    # Test case where only the first number needs to be edited
    nums = [7, 1, 8, 8]
    assert s.checkPossibility(nums) == True

    # Test case where there is only one number in the array
    nums = [1]
    assert s.checkPossibility(nums) == True

    # Test case where all numbers in the array are the same
    nums = [2, 2, 2, 2]
    assert s.checkPossibility(nums) == True

    # Test case where the numbers in the array are decreasing
    nums = [5, 4, 3, 2, 1]
    assert s.checkPossibility(nums) == False

    # Test case where the numbers in the array are increasing
    nums = [1, 2, 3, 4, 5]
    assert s.checkPossibility(nums) == True