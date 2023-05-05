import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_generateTheString_1(solution):
    result = solution.generateTheString(4)
    assert len(result) == 4
    assert all(result.count(char) % 2 == 1 for char in result)

def test_generateTheString_2(solution):
    result = solution.generateTheString(7)
    assert len(result) == 7
    assert all(result.count(char) % 2 == 1 for char in result)

def test_generateTheString_3(solution):
    result = solution.generateTheString(1)
    assert len(result) == 1
    assert all(result.count(char) % 2 == 1 for char in result)

def test_generateTheString_4(solution):
    result = solution.generateTheString(2)
    assert len(result) == 2
    assert all(result.count(char) % 2 == 1 for char in result) 

def test_generateTheString_5(solution):
    result = solution.generateTheString(18)
    assert len(result) == 18
    assert all(result.count(char) % 2 == 1 for char in result) 

def test_generateTheString_6(solution):
    result = solution.generateTheString(0)
    assert result == ""