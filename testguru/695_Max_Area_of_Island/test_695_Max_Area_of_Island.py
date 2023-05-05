
import pytest
from solution import Solution

def test_maxAreaOfIsland():
    s = Solution()

    # Test case 1: typical input with multiple islands
    grid = [[0,0,1,0,0],[0,0,0,1,1],[1,0,0,1,1],[0,1,1,0,0],[0,0,0,0,0]]
    assert s.maxAreaOfIsland(grid) == 6

    # Test case 2: input with only one island
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    assert s.maxAreaOfIsland(grid) == 25

    # Test case 3: input with no island
    grid = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    assert s.maxAreaOfIsland(grid) == 0

    # Test case 4: input with irregular shape island
    grid = [[1,1,0,0,0],[1,0,0,0,0],[0,0,1,1,0],[0,0,0,1,1]]
    assert s.maxAreaOfIsland(grid) == 4

    # Test case 5: empty input list
    grid = []
    assert s.maxAreaOfIsland(grid) == 0

    # Test case 6: input with all zeros
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    assert s.maxAreaOfIsland(grid) == 0
