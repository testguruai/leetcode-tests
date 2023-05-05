import pytest

from solution import Solution

@pytest.fixture(scope="module")
def solution():
    return Solution()

def test_canCompleteCircuit_empty(solution):
    assert solution.canCompleteCircuit([], []) == -1

def test_canCompleteCircuit_single(solution):
    assert solution.canCompleteCircuit([2], [1]) == 0

def test_canCompleteCircuit_no_solution(solution):
    assert solution.canCompleteCircuit([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]) == -1

def test_canCompleteCircuit_solution(solution):
    assert solution.canCompleteCircuit([5, 1, 2, 3, 4], [4, 4, 1, 1, 3]) == 4

def test_canCompleteCircuit_large_input(solution):
    gas = [100] * 1000
    cost = [99] * 999 + [1]
    assert solution.canCompleteCircuit(gas, cost) == 0