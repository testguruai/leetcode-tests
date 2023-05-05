import pytest

from .solution import Solution

def test_with_match_case():
    pattern = "abba"
    string = "dog cat cat dog"
    assert Solution().wordPattern(pattern, string) == True

def test_with_unmatch_case():
    pattern = "abba"
    string = "dog dog dog dog"
    assert Solution().wordPattern(pattern, string) == False

def test_with_empty_pattern():
    pattern = ""
    string = "abcd"
    assert Solution().wordPattern(pattern, string) == False

def test_with_empty_string():
    pattern = "abab"
    string = ""
    assert Solution().wordPattern(pattern, string) == False

def test_with_none_pattern_and_string():
    pattern = None
    string = None
    assert Solution().wordPattern(pattern, string) == True

def test_with_longer_string_than_pattern():
    pattern = "abcd"
    string = "dog cat cat dog bull"
    assert Solution().wordPattern(pattern, string) == False

def test_with_longer_pattern_than_string():
    pattern = "abcde"
    string = "dog cat cat dog"
    assert Solution().wordPattern(pattern, string) == False