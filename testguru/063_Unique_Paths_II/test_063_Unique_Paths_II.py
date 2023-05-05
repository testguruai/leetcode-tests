
import pytest
from solution import Solution

def test_uniquePathsWithObstacles():
    s = Solution()
    
    # Test Case 1
    grid1 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    assert s.uniquePathsWithObstacles(grid1) == 2
    
    # Test Case 2
    grid2 = [
        [0,1],
        [0,0]
    ]
    assert s.uniquePathsWithObstacles(grid2) == 1
    
    # Test Case 3
    grid3 = [
        [0,0],
        [1,1],
        [0,0]
    ]
    assert s.uniquePathsWithObstacles(grid3) == 0
    
    # Test Case 4
    grid4 = [
        [1,0]
    ]
    assert s.uniquePathsWithObstacles(grid4) == 0
    
    # Test Case 5
    grid5 = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    assert s.uniquePathsWithObstacles(grid5) == 8
