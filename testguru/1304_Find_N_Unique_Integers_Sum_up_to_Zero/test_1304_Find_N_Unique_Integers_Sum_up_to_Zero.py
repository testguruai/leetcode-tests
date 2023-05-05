import pytest

from solution import Solution

def test_sumZero():
    sol = Solution()

    # Test n = 0
    assert sol.sumZero(0) == []

    # Test n = 1
    assert sol.sumZero(1) == [0]

    # Test n = 2
    assert sol.sumZero(2) == [-1, 1]

    # Test n = 3
    assert sol.sumZero(3) == [-3, -1, 4]

    # Test n = 5
    assert sol.sumZero(5) == [-9, -6, -3, 2, 16]