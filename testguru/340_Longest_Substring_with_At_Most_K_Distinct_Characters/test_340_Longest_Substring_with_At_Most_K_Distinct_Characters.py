import pytest

from solution import Solution

def test_lengthOfLongestSubstringKDistinct():
    s1 = "eceba"
    k1 = 2
    s2 = "aa"
    k2 = 1
    s3 = "aaa"
    k3 = 1
    s4 = "abcabcabcabc"
    k4 = 3

    sol = Solution()
    assert sol.lengthOfLongestSubstringKDistinct(s1, k1) == 3
    assert sol.lengthOfLongestSubstringKDistinct(s2, k2) == 2
    assert sol.lengthOfLongestSubstringKDistinct(s3, k3) == 3
    assert sol.lengthOfLongestSubstringKDistinct(s4, k4) == 3

    # Test empty input
    assert sol.lengthOfLongestSubstringKDistinct("", 0) == 0

    # Test when k is greater than length of input
    assert sol.lengthOfLongestSubstringKDistinct("abc", 5) == 3

    # Test when all characters are distinct
    assert sol.lengthOfLongestSubstringKDistinct("abcdefghijklmnopqrstuvwxyz", 26) == 26