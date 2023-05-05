import pytest

from solution import Solution

def test_computeArea():
    sol = Solution()
    assert sol.computeArea(-3, 0, 3, 4, 0, -1, 9, 2) == 45
    assert sol.computeArea(0, 0, 0, 0, 0, 0, 0, 0) == 0
    assert sol.computeArea(-2, -2, 2, 2, -1, -1, 1, 1) == 16
    assert sol.computeArea(-2, -2, 2, 2, -3, -3, 3, 3) == 36
    assert sol.computeArea(-2, -2, 2, 2, -1, -1, 1, 3) == 16
    assert sol.computeArea(-2, -2, 2, 2, -1, -1, 3, 1) == 16
    assert sol.computeArea(-2, -2, 2, 2, -3, -1, 3, 1) == 24
    assert sol.computeArea(-2, -2, 2, 2, -1, -3, 1, 3) == 24