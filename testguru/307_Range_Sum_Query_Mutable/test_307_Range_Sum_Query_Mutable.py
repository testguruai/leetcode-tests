
import pytest

def test_num_array():
    nums = [1, 3, 5]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 2) == 9
    num_array.update(1, 2)
    assert num_array.sumRange(0, 2) == 8
    num_array.update(0, 4)
    assert num_array.sumRange(0, 2) == 11

def test_build_tree():
    nums = [1, 3, 5]
    num_array = NumArray(nums)
    assert num_array.tree == [0, 9, 4, 5, 1, 3, 0, 0]

def test_update():
    nums = [1, 3, 5]
    num_array = NumArray(nums)
    num_array.update(1, 2)
    assert num_array.tree == [0, 8, 4, 4, 1, 3, 0, 0]
    num_array.update(0, 4)
    assert num_array.tree == [0, 12, 6, 6, 4, 2, 5, 1]

def test_sum_range():
    nums = [1, 3, 5]
    num_array = NumArray(nums)
    assert num_array.sumRange(0, 2) == 9
    assert num_array.sumRange(0, 1) == 4
    assert num_array.sumRange(1, 2) == 8
