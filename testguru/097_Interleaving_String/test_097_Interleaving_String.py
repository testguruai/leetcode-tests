import pytest

from solution import Solution

def test_isInterleave():
    sol = Solution()
    assert sol.isInterleave('aabcc', 'dbbca', 'aadbbcbcac') == True
    assert sol.isInterleave('aabcc', 'dbbca', 'aadbbbaccc') == False
    assert sol.isInterleave('', '', '') == True
    assert sol.isInterleave('a', '', 'a') == True
    assert sol.isInterleave('', 'b', 'b') == True