import pytest

from solution import Solution

def test_longest_consecutive():
    solution = Solution()

    # test case 1 - regular input
    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

    # test case 2 - empty input
    assert solution.longestConsecutive([]) == 0

    # test case 3 - minimum input
    assert solution.longestConsecutive([5]) == 1

    # test case 4 - negative input
    assert solution.longestConsecutive([-1, -2, -3, -4, -5]) == 5

    # test case 5 - input with duplicates
    assert solution.longestConsecutive([1, 2, 3, 3, 4, 5, 5, 6, 6, 7]) == 7

    # test case 6 - input with no consecutive numbers
    assert solution.longestConsecutive([1, 3, 5, 7, 9]) == 1

    # test case 7 - input with all consecutive numbers
    assert solution.longestConsecutive([3, 4, 5, 6, 7, 8, 9, 10, 11]) == 9

    # test case 8 - input with large numbers
    assert solution.longestConsecutive([1000000, 1000001, 1000002, 1000003, 1000004]) == 5

    # test case 9 - input with negative and positive numbers
    assert solution.longestConsecutive([-3, -2, -1, 0, 1, 2, 3, 4]) == 8

    # test case 10 - input with one number repeated
    assert solution.longestConsecutive([1, 2, 3, 4, 5, 5, 5, 5, 6, 7]) == 7