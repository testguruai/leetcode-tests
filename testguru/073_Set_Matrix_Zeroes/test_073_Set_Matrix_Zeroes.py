import pytest
from solution import Solution

def test_solution():
    solution = Solution()
    # Test case for an empty matrix
    assert solution.setZeroes([]) == None
    # Test case for a matrix where no zero is present
    assert solution.setZeroes([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]
    # Test case where all elements in a row and column are 0
    assert solution.setZeroes([[0, 2, 3], [4, 5, 6], [7, 8, 0]]) == [[0, 0, 0], [0, 5, 0], [0, 0, 0]]
    # Test case where only one element in a row and column is 0
    assert solution.setZeroes([[1, 2, 3], [4, 0, 6], [7, 8, 9]]) == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
    # Test case where all elements in the matrix are 0
    assert solution.setZeroes([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]