import pytest

from solution import Solution


def test_is_ugly_returns_false_for_negative_numbers():
    s = Solution()
    assert not s.isUgly(-1)
    assert not s.isUgly(-2147483648)


def test_is_ugly_returns_false_for_zero():
    s = Solution()
    assert not s.isUgly(0)


def test_is_ugly_returns_true_for_ugly_numbers():
    s = Solution()
    assert s.isUgly(1)
    assert s.isUgly(6)
    assert s.isUgly(8)
    assert s.isUgly(14)
    assert s.isUgly(15)
    assert s.isUgly(30)


def test_is_ugly_returns_false_for_non_ugly_numbers():
    s = Solution()
    assert not s.isUgly(7)
    assert not s.isUgly(11)
    assert not s.isUgly(17)
    assert not s.isUgly(21)
    assert not s.isUgly(23)
    assert not s.isUgly(27)