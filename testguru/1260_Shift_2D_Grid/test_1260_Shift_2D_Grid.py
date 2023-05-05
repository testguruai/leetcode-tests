import pytest

from .solution_file import Solution


@pytest.fixture
def grid():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def test_shiftGrid(grid):
    s = Solution()
    assert s.shiftGrid(grid, 1) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    assert s.shiftGrid(grid, 9) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert s.shiftGrid(grid, 3) == [[7, 8, 9], [1, 2, 3], [4, 5, 6]]
    assert s.shiftGrid(grid, 4) == [[6, 7, 8], [9, 1, 2], [3, 4, 5]]