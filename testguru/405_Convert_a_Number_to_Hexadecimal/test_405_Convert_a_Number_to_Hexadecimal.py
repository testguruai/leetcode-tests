import pytest

from solution import Solution

def test_toHex_zero_input():
    sol = Solution()
    assert sol.toHex(0) == '0'

def test_toHex_positive_input():
    sol = Solution()
    assert sol.toHex(26) == '1a'
    assert sol.toHex(16) == '10'
    assert sol.toHex(255) == 'ff'

def test_toHex_negative_input():
    sol = Solution()
    assert sol.toHex(-1) == 'ffffffff'
    assert sol.toHex(-26) == 'ffffffe6'
    assert sol.toHex(-255) == 'ffffff01'