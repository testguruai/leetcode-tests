import pytest


def test_mySqrt_zero():
    sol = Solution()
    assert sol.mySqrt(0) == 0


def test_mySqrt_one():
    sol = Solution()
    assert sol.mySqrt(1) == 1


def test_mySqrt_four():
    sol = Solution()
    assert sol.mySqrt(4) == 2


def test_mySqrt_nine():
    sol = Solution()
    assert sol.mySqrt(9) == 3


def test_mySqrt_twenty_five():
    sol = Solution()
    assert sol.mySqrt(25) == 5


def test_mySqrt_negative():
    sol = Solution()
    with pytest.raises(ValueError):
        sol.mySqrt(-4)