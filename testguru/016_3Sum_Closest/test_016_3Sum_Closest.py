import pytest

from solution import Solution

def test_threeSumClosest():
    sol = Solution()

    assert sol.threeSumClosest([-1, 2, 1, -4], 1) == 2

    assert sol.threeSumClosest([0, 1, 2], 3) == 3

    assert sol.threeSumClosest([-1, 0, 1], 2) == 0

    assert sol.threeSumClosest([-1, 2, 1, -4], -1) == -1

    assert sol.threeSumClosest([1, 1, 1, 0], -100) == 2

    assert sol.threeSumClosest([], 1) == None