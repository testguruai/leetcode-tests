import pytest

from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_sortArrayByParity_evenNumbersFirst(solution):
    assert solution.sortArrayByParity([2, 4, 3, 1, 7, 9]) == [2, 4, 3, 1, 7, 9]

def test_sortArrayByParity_oddNumbersFirst(solution):
    assert solution.sortArrayByParity([3, 5, 2, 4, 8, 6]) == [2, 4, 8, 6, 3, 5]

def test_sortArrayByParity_emptyList(solution):
    assert solution.sortArrayByParity([]) == []

def test_sortArrayByParity_allEvenNumbers(solution):
    assert solution.sortArrayByParity([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_sortArrayByParity_allOddNumbers(solution):
    assert solution.sortArrayByParity([3, 1, 7, 5]) == [3, 1, 7, 5]