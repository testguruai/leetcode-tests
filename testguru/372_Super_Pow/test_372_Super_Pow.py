import pytest

from solution import Solution


def test_superPow():
    s = Solution()
    assert s.superPow(2, []) == 1
    assert s.superPow(2, [0]) == 1
    assert s.superPow(2, [1,0]) == 1024
    assert s.superPow(2, [1,1]) == 2048
    assert s.superPow(3, [1,2,3,4,5,6,7,8,9,0]) == 1198


def test_powmod():
    s = Solution()
    assert s.powmod(2, 3) == 8
    assert s.powmod(3, 4) == 81
    assert s.powmod(4, 5) == 1024
    assert s.powmod(5, 6) == 15625