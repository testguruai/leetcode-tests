
import pytest

@pytest.fixture(scope="module")
def solution():
    from solution import Solution
    return Solution()

def test_minPathSum(solution):
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    assert solution.minPathSum(grid) == 7
    
    grid = [[1,2,3],[4,5,6]]
    assert solution.minPathSum(grid) == 12
    
    grid = [[1]]
    assert solution.minPathSum(grid) == 1
    
    grid = [[]]
    assert solution.minPathSum(grid) == 0

    grid = []
    assert solution.minPathSum(grid) == 0

    grid = [[1,2,3],[4,5,6],[7,8,9]]
    assert solution.minPathSum(grid) == 21
    
    grid = [[1,2,3,4,5]]
    assert solution.minPathSum(grid) == 15
    
    grid = [[1],[2],[3]]
    assert solution.minPathSum(grid) == 6
