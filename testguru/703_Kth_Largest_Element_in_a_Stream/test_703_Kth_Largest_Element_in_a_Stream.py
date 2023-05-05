import pytest
import heapq

from solution import KthLargest

class TestKthLargest(object):

    def test_kth_largest(self):
        nums = [4, 5, 8, 2]
        k = 3
        obj = KthLargest(k, nums)
        assert obj.add(3) == 4 # 3rd largest is 4
        assert obj.add(5) == 5 # 3rd largest is 5
        assert obj.add(10) == 8 # 3rd largest is 8
        assert obj.add(9) == 8 # 3rd largest is 8

    def test_empty_kth_largest(self):
        nums = []
        k = 1
        obj = KthLargest(k, nums)
        assert obj.add(1) == 1 # only 1 element is added to the heap

    def test_add_to_heap(self):
        nums = [4, 5, 8, 2]
        k = 5 # k greater than len of nums
        obj = KthLargest(k, nums)
        assert obj.add(3) == 2 # 5th largest is 2 since heap is not full yet
        assert obj.add(5) == 2 # 5th largest is still 2 since heap is not full yet
        assert obj.add(10) == 2 # 5th largest is still 2 since heap is not full yet
        assert obj.add(9) == 2 # 5th largest is still 2 since heap is not full yet

    def test_add_small_value(self):
        nums = [4, 5, 8, 2]
        k = 3
        obj = KthLargest(k, nums)
        assert obj.add(1) == 4 # 3rd largest is still 4 since 1 is less than all original values

    def test_add_same_value_twice(self):
        nums = [4, 5, 8, 2]
        k = 3
        obj = KthLargest(k, nums)
        assert obj.add(5) == 5 # 3rd largest is still 5 since we added the same value twice

    def test_add_large_value(self):
        nums = [4, 5, 8, 2]
        k = 3
        obj = KthLargest(k, nums)
        assert obj.add(20) == 8 # 3rd largest is still 8 since 20 is greater than all original values