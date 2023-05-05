import pytest

from solution import Solution

def test_islandPerimeter_no_islands():
    s = Solution()
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    assert s.islandPerimeter(grid) == 0

def test_islandPerimeter_one_island():
    s = Solution()
    grid = [[0,1,0],
            [1,1,1],
            [0,1,0]]
    assert s.islandPerimeter(grid) == 16

def test_islandPerimeter_multiple_islands():
    s = Solution()
    grid = [[0,1,0,0],
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0]]
    assert s.islandPerimeter(grid) == 24

def test_islandPerimeter_invalid_input():
    s = Solution()
    grid = []
    assert s.islandPerimeter(grid) == 0

    grid = [[]]
    assert s.islandPerimeter(grid) == 0

    grid = [[0,1,2],
            [3,4,5]]
    assert s.islandPerimeter(grid) == 0
