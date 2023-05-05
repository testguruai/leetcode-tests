import pytest

from solution import Solution

def test_lengthOfLongestSubstringTwoDistinct():
    sol = Solution()
    
    assert sol.lengthOfLongestSubstringTwoDistinct('eceba') == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('ccaabbb') == 5
    assert sol.lengthOfLongestSubstringTwoDistinct('abcabcbb') == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('abcddefghijklmnopqrstuvwxyz') == 2
    assert sol.lengthOfLongestSubstringTwoDistinct('') == 0
    assert sol.lengthOfLongestSubstringTwoDistinct('a') == 1
    assert sol.lengthOfLongestSubstringTwoDistinct('aa') == 2
    assert sol.lengthOfLongestSubstringTwoDistinct('aaa') == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('ab') == 2
    assert sol.lengthOfLongestSubstringTwoDistinct('aab') == 3
    assert sol.lengthOfLongestSubstringTwoDistinct('aaaababccdf') == 4
