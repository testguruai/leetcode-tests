
import pytest
from solution import Solution

def test_toeplitz_matrix():
    s = Solution()

    assert s.isToeplitzMatrix([[1, 2], [3, 4]]) == True
    assert s.isToeplitzMatrix([[1, 2, 3], [4, 1, 2], [5, 4, 1]]) == True
    assert s.isToeplitzMatrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == False
    assert s.isToeplitzMatrix([[1, 2], [1, 2]]) == False
