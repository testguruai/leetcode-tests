import pytest

from solution import Solution


# Test cases for findCircleNum() method
def test_findCircleNum():
    sol = Solution()

    # Test case 1
    M1 = [[1,1,0],
          [1,1,0],
          [0,0,1]]

    assert sol.findCircleNum(M1) == 2

    # Test case 2
    M2 = [[1,1,0],
          [1,1,1],
          [0,1,1]]

    assert sol.findCircleNum(M2) == 1

    # Test case 3
    M3 = [[1,0,0,1],
          [0,1,1,0],
          [0,1,1,1],
          [1,0,1,1]]

    assert sol.findCircleNum(M3) == 1


# Test cases for dfs() method
def test_dfs():
    sol = Solution()

    # Test case 1
    M1 = [[1,1,0],
          [1,1,0],
          [0,0,1]]
    visited1 = [0, 0, 0]

    sol.dfs(M1, visited1, 0)
    assert visited1 == [1, 1, 0]

    # Test case 2
    M2 = [[1,1,0],
          [1,1,1],
          [0,1,1]]
    visited2 = [0, 0, 0]

    sol.dfs(M2, visited2, 0)
    assert visited2 == [1, 1, 0]

    # Test case 3
    M3 = [[1,0,0,1],
          [0,1,1,0],
          [0,1,1,1],
          [1,0,1,1]]
    visited3 = [0, 0, 0, 0]

    sol.dfs(M3, visited3, 0)
    assert visited3 == [1, 0, 0, 1]