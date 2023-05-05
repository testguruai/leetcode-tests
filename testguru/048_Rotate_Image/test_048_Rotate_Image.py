import pytest
from solution import Solution

def test_rotate_4x4_matrix():
    s = Solution()
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    expected_result = [[13,9,5,1],[14,10,6,2],[15,11,7,3],[16,12,8,4]]
    s.rotate(matrix)
    assert matrix == expected_result

def test_rotate_1x1_matrix():
    s = Solution()
    matrix = [[1]]
    expected_result = [[1]]
    s.rotate(matrix)
    assert matrix == expected_result

def test_rotate_empty_matrix():
    s = Solution()
    matrix = []
    expected_result = []
    s.rotate(matrix)
    assert matrix == expected_result

def test_rotate_none_matrix():
    s = Solution()
    matrix = None
    expected_result = None
    s.rotate(matrix)
    assert matrix == expected_result

def test_rotate_odd_matrix():
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected_result = [[7,4,1],[8,5,2],[9,6,3]]
    s.rotate(matrix)
    assert matrix == expected_result