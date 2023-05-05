import pytest

from solution import Solution

def test_transpose():
    sol = Solution()

    # Test case 1
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected_output = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert sol.transpose(A) == expected_output

    # Test case 2
    A = [[1, 2], [3, 4], [5, 6]]
    expected_output = [[1, 3, 5], [2, 4, 6]]
    assert sol.transpose(A) == expected_output

    # Test case 3
    A = [[1, 2, 3], [4, 5, 6]]
    expected_output = [[1, 4], [2, 5], [3, 6]]
    assert sol.transpose(A) == expected_output

    # Test case 4
    A = [[1]]
    expected_output = [[1]]
    assert sol.transpose(A) == expected_output

    # Test case 5
    A = []
    expected_output = []
    assert sol.transpose(A) == expected_output

    # Test case 6
    A = [[1, 2], [3, 4]]
    expected_output = [[1, 3], [2, 4]]
    assert sol.transpose(A) == expected_output

    # Test case 7
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    expected_output = [[1, 4, 7, 10], [2, 5, 8, 11], [3, 6, 9, 12]]
    assert sol.transpose(A) == expected_output

    # Test case 8
    A = [[1, 2], [3, 4], [5, 6], [7, 8]]
    expected_output = [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert sol.transpose(A) == expected_output

    # Test case 9
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
    expected_output = [[1, 4, 7, 10, 13], [2, 5, 8, 11, 14], [3, 6, 9, 12, 15]]
    assert sol.transpose(A) == expected_output

    # Test case 10
    A = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
    expected_output = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
    assert sol.transpose(A) == expected_output

    # Test case 11
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]
    expected_output = [[1, 4, 7, 10, 13, 16], [2, 5, 8, 11, 14, 17], [3, 6, 9, 12, 15, 18]]
    assert sol.transpose(A) == expected_output

    # Test case 12
    A = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]
    expected_output = [[1, 3, 5, 7, 9, 11], [2, 4, 6, 8, 10, 12]]
    assert sol.transpose(A) == expected_output

    # Test case 13
    A = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    expected_output = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    assert sol.transpose(A) == expected_output

    # Test case 14
    A = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
    expected_output = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    assert sol.transpose(A) == expected_output

    # Test case 15
    A = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
    expected_output = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
    assert sol.transpose(A) == expected_output

    # Test case 16
    A = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
    expected_output = [[1, 7], [2, 8], [3, 9], [4, 10], [5, 11], [6, 12]]
    assert sol.transpose(A) == expected_output
