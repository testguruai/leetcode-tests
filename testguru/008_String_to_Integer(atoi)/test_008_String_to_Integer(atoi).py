import pytest
from solution import Solution

@pytest.fixture()
def solution():
    return Solution()

def test_case1(solution):
    result = solution.myAtoi("42")
    assert result == 42

def test_case2(solution):
    result = solution.myAtoi("   -42")
    assert result == -42

def test_case3(solution):
    result = solution.myAtoi("4193 with words")
    assert result == 4193

def test_case4(solution):
    result = solution.myAtoi("words and 987")
    assert result == 0

def test_case5(solution):
    result = solution.myAtoi("-91283472332")
    assert result == -2147483648

def test_case6(solution):
    result = solution.myAtoi("+-2")
    assert result == 0
