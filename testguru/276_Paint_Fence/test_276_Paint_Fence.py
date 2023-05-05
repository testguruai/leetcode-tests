import pytest

from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_num_ways_when_n_is_zero(solution):
    assert solution.numWays(0, 5) == 0

def test_num_ways_when_n_is_one(solution):
    assert solution.numWays(1, 5) == 5

def test_num_ways_when_n_is_two(solution):
    assert solution.numWays(2, 5) == 25

def test_num_ways_when_n_is_greater_than_two(solution):
    assert solution.numWays(3, 3) == 24

def test_num_ways_when_k_is_one(solution):
    assert solution.numWays(5, 1) == 0