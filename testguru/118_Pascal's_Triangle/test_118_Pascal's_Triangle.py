import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_generate_0_rows(solution):
    assert solution.generate(0) == []

def test_generate_1_row(solution):
    assert solution.generate(1) == [[1]]

def test_generate_2_rows(solution):
    assert solution.generate(2) == [[1], [1, 1]]

def test_generate_5_rows(solution):
    expected_result = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    assert solution.generate(5) == expected_result

def test_generate_10_rows(solution):
    expected_result = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1],
        [1, 5, 10, 10, 5, 1],
        [1, 6, 15, 20, 15, 6, 1],
        [1, 7, 21, 35, 35, 21, 7, 1],
        [1, 8, 28, 56, 70, 56, 28, 8, 1],
        [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    ]
    assert solution.generate(10) == expected_result

def test_generate_negative_rows_raises_value_error(solution):
    with pytest.raises(ValueError):
        solution.generate(-1)