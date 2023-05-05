import pytest
from solution import Solution

def test_canConstruct_true():
    assert Solution().canConstruct("aa", "aab") == True
    assert Solution().canConstruct("a", "a") == True

def test_canConstruct_false():
    assert Solution().canConstruct("aa", "ab") == False
    assert Solution().canConstruct("abc", "def") == False

def test_canConstruct_edge_cases():
    assert Solution().canConstruct("", "") == True
    assert Solution().canConstruct("a", "") == False
    assert Solution().canConstruct("", "a") == True