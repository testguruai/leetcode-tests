import pytest
from solution import Solution

def test_wordBreak():
    s = Solution()
    assert s.wordBreak("leetcode", ["leet", "code"]) == True
    assert s.wordBreak("abcd", ["a", "abc", "b", "cd"]) == True
    assert s.wordBreak("applepenapple", ["apple", "pen"]) == True
    assert s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert s.wordBreak("bb", ["a", "b", "bbb", "bbbb"]) == True
