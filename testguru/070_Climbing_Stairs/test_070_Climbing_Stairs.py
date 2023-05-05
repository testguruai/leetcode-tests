import pytest

from solution import Solution

def test_climbing_stairs():
    s = Solution()

    assert s.climbStairs(2) == 2
    assert s.climbStairs(3) == 3
    assert s.climbStairs(4) == 5
    assert s.climbStairs(5) == 8

def test_climbing_stairs_with_zero_or_one_steps():
    s = Solution()

    assert s.climbStairs(0) == 1
    assert s.climbStairs(1) == 1