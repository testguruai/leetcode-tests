import pytest
from solution import Solution

def test_overlap():
    sol = Solution()
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,3]
    assert sol.isRectangleOverlap(rec1, rec2) == True

def test_no_overlap():
    sol = Solution()
    rec1 = [0,0,1,1]
    rec2 = [2,2,3,3]
    assert sol.isRectangleOverlap(rec1, rec2) == False

def test_partial_overlap():
    sol = Solution()
    rec1 = [0,0,2,2]
    rec2 = [1,1,3,5]
    assert sol.isRectangleOverlap(rec1, rec2) == True

def test_same_rectangles():
    sol = Solution()
    rec1 = [0,0,2,2]
    rec2 = [0,0,2,2]
    assert sol.isRectangleOverlap(rec1, rec2) == True

def test_adjacent_rectangles():
    sol = Solution()
    rec1 = [0,0,2,2]
    rec2 = [2,2,4,4]
    assert sol.isRectangleOverlap(rec1, rec2) == False

def test_intersect_helper_function():
    sol = Solution()
    assert sol.intersect(0,3,2,4) == True
    assert sol.intersect(0,2,3,4) == False
    assert sol.intersect(0,2,2,4) == True
    assert sol.intersect(0,4,2,3) == True