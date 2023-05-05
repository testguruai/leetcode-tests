import pytest

from solution import Solution

def test_case_1():
    s = Solution()
    assert s.intersect([1,2,2,1], [2,2]) == [2,2]

def test_case_2():
    s = Solution()
    assert s.intersect([4,9,5], [9,4,9,8,4]) == [4,9]

def test_case_3():
    s = Solution()
    assert s.intersect([1,2,3], [4,5,6]) == []

def test_case_4():
    s = Solution()
    assert s.intersect([-1,0,1,2,-1,-4], [-1,-1,1,0,2]) == [-1,0,1,2]

def test_case_5():
    s = Solution()
    assert s.intersect([], [1,2,3]) == []

def test_case_6():
    s = Solution()
    assert s.intersect([], []) == []

def test_case_7():
    s = Solution()
    assert s.intersect([1], [1,1]) == [1]

def test_case_8():
    s = Solution()
    assert s.intersect([1,2,3], [2,4]) == [2]

def test_case_9():
    s = Solution()
    assert s.intersect([1,1], [1]) == [1]

def test_case_10():
    s = Solution()
    assert s.intersect([1,2,3], [3,2,1]) == [1,2,3]
