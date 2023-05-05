
import pytest
from solution import Solution

def test_num_islands():
    s = Solution()

    # Test case 1
    m = 3
    n = 3
    positions = [[0,0],[0,1],[1,2],[2,1]]
    expected_output = [1, 1, 2, 3]
    assert s.numIslands2(m, n, positions) == expected_output

    # Test case 2
    m = 3
    n = 3
    positions = [[0,0],[0,1],[1,2],[2,1],[1,1]]
    expected_output = [1, 1, 2, 3, 2]
    assert s.numIslands2(m, n, positions) == expected_output

    # Test case 3
    m = 2
    n = 2
    positions = [[0,0],[1,1],[0,1],[1,0]]
    expected_output = [1, 2, 2, 1]
    assert s.numIslands2(m, n, positions) == expected_output

    # Test case 4
    m = 3
    n = 3
    positions = [[0,0],[0,1],[1,2],[2,1],[2,2]]
    expected_output = [1, 1, 2, 3, 3]
    assert s.numIslands2(m, n, positions) == expected_output
