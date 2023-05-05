import pytest

def test_empty_matrix():
    matrix = []
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == 0

def test_single_element_matrix():
    matrix = [[1]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == 1

def test_square_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == 1
    assert obj.sumRegion(0, 0, 1, 1) == 11
    assert obj.sumRegion(0, 0, 2, 2) == 15
    assert obj.sumRegion(0, 0, 2, 1) == 12
    assert obj.sumRegion(1, 0, 2, 2) == 24

def test_rectangular_matrix():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == 1
    assert obj.sumRegion(0, 0, 1, 1) == 12
    assert obj.sumRegion(0, 0, 1, 2) == 18
    assert obj.sumRegion(0, 0, 1, 3) == 22
    assert obj.sumRegion(1, 0, 1, 3) == 26

def test_negative_values():
    matrix = [[-2,-1,-3,-4],[-1,-2,-3,-1],[-4,-1,-1,-1],[-2,-4,-2,-2]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == -2
    assert obj.sumRegion(0, 0, 1, 1) == -6
    assert obj.sumRegion(1, 0, 2, 1) == -8
    assert obj.sumRegion(1, 1, 3, 3) == -13

def test_matrix_with_zero_values():
    matrix = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    obj = NumMatrix(matrix)
    assert obj.sumRegion(0, 0, 0, 0) == 0
    assert obj.sumRegion(0, 0, 1, 1) == 0
    assert obj.sumRegion(1, 1, 2, 2) == 0
    assert obj.sumRegion(0, 0, 3, 3) == 0