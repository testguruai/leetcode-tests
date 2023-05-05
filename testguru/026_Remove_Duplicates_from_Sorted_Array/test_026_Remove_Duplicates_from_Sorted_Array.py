import pytest

from solution import Solution

solution = Solution()

def test_case_1():
    nums = [1, 1, 2]
    assert solution.removeDuplicates(nums) == 2

def test_case_2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert solution.removeDuplicates(nums) == 5

def test_case_3():
    nums = []
    assert solution.removeDuplicates(nums) == 0

def test_case_4():
    nums = [1, 1]
    assert solution.removeDuplicates(nums) == 1

def test_case_5():
    nums = [1]
    assert solution.removeDuplicates(nums) == 1

def test_case_6():
    nums = [1, 2, 3]
    assert solution.removeDuplicates(nums) == 3

def test_case_7():
    nums = [1, 1, 1, 1]
    assert solution.removeDuplicates(nums) == 1

def test_case_8():
    nums = [1, 2, 2, 3]
    assert solution.removeDuplicates(nums) == 3

def test_case_9():
    nums = [1, 2, 3, 3]
    assert solution.removeDuplicates(nums) == 3

def test_case_10():
    nums = [1, 1, 2, 2, 3, 3]
    assert solution.removeDuplicates(nums) == 3
