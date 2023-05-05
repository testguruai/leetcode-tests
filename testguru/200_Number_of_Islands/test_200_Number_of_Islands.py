import pytest

from solution import Solution

def test_numIslands():
    s = Solution()
    grid = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    assert s.numIslands(grid) == 1
    
    grid = [['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']]
    assert s.numIslands(grid) == 3
    
    grid = [['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    assert s.numIslands(grid) == 0
    
    grid = None
    assert s.numIslands(grid) == 0
    
    grid = []
    assert s.numIslands(grid) == 0