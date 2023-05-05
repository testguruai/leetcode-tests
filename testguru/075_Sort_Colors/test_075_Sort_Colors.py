import pytest

def test_sortColors_1():
    s = Solution()
    nums = [2,0,2,1,1,0]
    s.sortColors(nums)
    assert nums == [0,0,1,1,2,2]

def test_sortColors_2():
    s = Solution()
    nums = [1,0,2,1,0,2]
    s.sortColors(nums)
    assert nums == [0,0,1,1,2,2]

def test_sortColors_3():
    s = Solution()
    nums = [1,1,1,0,0,0,2,2,2]
    s.sortColors(nums)
    assert nums == [0,0,0,1,1,1,2,2,2]