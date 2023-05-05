import pytest
from solution import Solution


def test_palindrome_pairs():
    s = Solution()
    words = ["abcd","dcba","lls","s","sssll"]
    assert s.palindromePairs(words) == [[0,1],[1,0],[2,4],[3,2]]
    
    words = ["bat", "tab", "cat"]
    assert s.palindromePairs(words) == [[0,1],[1,0]]
    
    words = ["a", ""]
    assert s.palindromePairs(words) == [[0,1],[1,0]]