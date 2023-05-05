import pytest

from solution import Solution

def test_containsNearbyDuplicate_true():
    s = Solution()
    nums = [1,2,3,1]
    k = 3
    assert s.containsNearbyDuplicate(nums, k) == True

def test_containsNearbyDuplicate_false():
    s = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    assert s.containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_empty_input():
    s = Solution()
    nums = []
    k = 1
    assert s.containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_one_element():
    s = Solution()
    nums = [1]
    k = 1
    assert s.containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_same_elements():
    s = Solution()
    nums = [1,1,1,1,1]
    k = 3
    assert s.containsNearbyDuplicate(nums, k) == True

def test_containsNearbyDuplicate_k_greater_than_len_nums():
    s = Solution()
    nums = [1,2,3,4,5]
    k = 10
    assert s.containsNearbyDuplicate(nums, k) == False

def test_containsNearbyDuplicate_all_distinct_elements():
    s = Solution()
    nums = [1,2,3,4,5]
    k = 3
    assert s.containsNearbyDuplicate(nums, k) == False