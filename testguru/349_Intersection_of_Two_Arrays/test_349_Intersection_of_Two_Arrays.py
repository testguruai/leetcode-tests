
import pytest
from solution import Solution

def test_case1():
    s = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    assert s.intersection(nums1, nums2) == [2]

def test_case2():
    s = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    assert s.intersection(nums1, nums2) == [9,4]

def test_case3():
    s = Solution()
    nums1 = [1,2,3]
    nums2 = [4,5,6]
    assert s.intersection(nums1, nums2) == []

def test_case4():
    s = Solution()
    nums1 = [1,1,1,1,1]
    nums2 = [1,1,1,1,1]
    assert s.intersection(nums1, nums2) == [1]

def test_case5():
    s = Solution()
    nums1 = [1,2,3]
    nums2 = [1,2,3]
    assert s.intersection(nums1, nums2) == [1,2,3]
