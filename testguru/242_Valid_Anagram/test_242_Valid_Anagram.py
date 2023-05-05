import pytest

from solution import Solution


def test_is_anagram_with_sort():
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t) is True

def test_is_not_anagram_with_sort():
    solution = Solution()
    s = "cat"
    t = "rat"
    assert solution.isAnagram(s, t) is False 

def test_is_anagram_with_hash():
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    assert solution.isAnagram(s, t) is True

def test_is_not_anagram_with_hash():
    solution = Solution()
    s = "cat"
    t = "rat"
    assert solution.isAnagram(s, t) is False 

def test_is_not_anagram_with_hash_len_not_equal():
    solution = Solution()
    s = "ana"
    t = "nagaram"
    assert solution.isAnagram(s, t) is False

def test_is_anagram_with_hash_repeated_chars():
    solution = Solution()
    s = "abb"
    t = "bba"
    assert solution.isAnagram(s, t) is True 

def test_is_not_anagram_with_hash_repeated_chars():
    solution = Solution()
    s = "ab"
    t = "bb"
    assert solution.isAnagram(s, t) is False