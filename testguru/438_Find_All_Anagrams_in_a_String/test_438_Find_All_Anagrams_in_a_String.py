import pytest

from .solution import Solution


class TestSolution:
    def test_findAnagrams_empty_input(self):
        s = ""
        p = "b"
        solution = Solution()
        assert solution.findAnagrams(s, p) == []

    def test_findAnagrams_invalid_input(self):
        s = None
        p = "abc"
        solution = Solution()
        assert solution.findAnagrams(s, p) == []

    def test_findAnagrams_no_anagrams(self):
        s = "abcdef"
        p = "xyz"
        solution = Solution()
        assert solution.findAnagrams(s, p) == []

    def test_findAnagrams_one_anagram(self):
        s = "abcdxyzaxybcw"
        p = "abc"
        solution = Solution()
        assert solution.findAnagrams(s, p) == [0, 7]

    def test_findAnagrams_multiple_anagrams(self):
        s = "abcbcaabcdeabccba"
        p = "abc"
        solution = Solution()
        assert solution.findAnagrams(s, p) == [0, 6, 7, 13]