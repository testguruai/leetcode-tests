import pytest

@pytest.fixture
def solution():
    return Solution()

def test_countBits_0(solution):
    assert solution.countBits(0) == [0]

def test_countBits_1(solution):
    assert solution.countBits(1) == [0, 1]

def test_countBits_2(solution):
    assert solution.countBits(2) == [0, 1, 1]

def test_countBits_5(solution):
    assert solution.countBits(5) == [0, 1, 1, 2, 1, 2]

def test_countBits_10(solution):
    assert solution.countBits(10) == [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2]