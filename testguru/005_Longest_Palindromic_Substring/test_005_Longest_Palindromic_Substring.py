import pytest

from solution import Solution

def test_longest_palindrome_empty_string():
    s = Solution()
    assert s.longestPalindrome("") == ""

def test_longest_palindrome_single_character():
    s = Solution()
    assert s.longestPalindrome("a") == "a"

def test_longest_palindrome_all_same_characters():
    s = Solution()
    assert s.longestPalindrome("aaa") == "aaa"

def test_longest_palindrome_odd_length_string():
    s = Solution()
    assert s.longestPalindrome("babad") == "bab"

def test_longest_palindrome_even_length_string():
    s = Solution()
    assert s.longestPalindrome("cbbd") == "bb"

def test_longest_palindrome_multiple_palindromes():
    s = Solution()
    assert s.longestPalindrome("abcbe") == "bcb"

def test_longest_palindrome_full_string_palindrome():
    s = Solution()
    assert s.longestPalindrome("racecar") == "racecar"