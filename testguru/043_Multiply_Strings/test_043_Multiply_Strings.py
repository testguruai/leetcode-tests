
import pytest
from solution import Solution

def test_multiply():
    s = Solution()
    assert s.multiply("0", "123") == "0"
    assert s.multiply("987654321", "123") == "12193263163"
    assert s.multiply("123", "987654321") == "12193263163"
    assert s.multiply("9", "99") == "891"
    assert s.multiply("5566", "7788") == "43332768"
    assert s.multiply("1234", "5678") == "7006652"
    assert s.multiply("123456789", "987654321") == "121932631137988491"
