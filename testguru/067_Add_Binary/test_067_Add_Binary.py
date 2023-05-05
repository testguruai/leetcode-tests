import pytest

from solution import Solution

def test_addBinary():
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("1111", "1111") == "11110"
    assert s.addBinary("0", "0") == "0"
    assert s.addBinary("0", "1111") == "1111"
    assert s.addBinary("1111", "0") == "1111"
    assert s.addBinary("1", "11111111") == "100000000"