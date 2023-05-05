import pytest

from solution import Solution

@pytest.fixture(scope="module")
def solution():
    return Solution()

@pytest.mark.parametrize("n,k,result", [
    (3, 2, "132"),
    (4, 9, "2314"),
    (1, 1, "1")
])
def test_getPermutation(solution, n, k, result):
    assert solution.getPermutation(n, k) == result

def test_getPermutation_negative_cases(solution):
    assert solution.getPermutation(0, 0) == ""
    assert solution.getPermutation(-3, -2) == ""
    assert solution.getPermutation(3, -2) == ""
    assert solution.getPermutation(-3, 2) == ""