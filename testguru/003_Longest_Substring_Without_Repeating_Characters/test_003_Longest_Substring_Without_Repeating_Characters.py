import pytest

from solution import Solution

def test_empty_string():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('') == 0

def test_single_character():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('a') == 1

def test_same_character():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('bbbbbb') == 1

def test_distinct_characters():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcde') == 5

def test_repeating_character():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcdea') == 5

def test_mixed_characters():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcdecfghi') == 7

def test_long_string():
    solution = Solution()
    assert solution.lengthOfLongestSubstring('abcdefghijklmabcdefghijklm') == 13