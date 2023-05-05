import pytest

def test_solution():
    solution = Solution()

    #Test edge cases
    assert solution.minCut("") == 0
    assert solution.minCut("a") == 0
    assert solution.minCut("aa") == 0

    #Test cases for input with even length
    assert solution.minCut("abba") == 0
    assert solution.minCut("abcd") == 3

    #Test cases for input with odd length
    assert solution.minCut("abcba") == 0
    assert solution.minCut("abcdefg") == 6