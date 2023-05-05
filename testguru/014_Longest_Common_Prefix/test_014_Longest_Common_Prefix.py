import pytest
from solution import Solution

def test_longestCommonPrefix_case1():
    s = Solution()
    assert s.longestCommonPrefix(["flower","flow","flight"]) == "fl"

def test_longestCommonPrefix_case2():
    s = Solution()
    assert s.longestCommonPrefix(["dog","racecar","car"]) == ""

def test_longestCommonPrefix_case3():
    s = Solution()
    assert s.longestCommonPrefix(["aca","cba"]) == ""

def test_longestCommonPrefix_case4():
    s = Solution()
    assert s.longestCommonPrefix([""]) == ""

def test_longestCommonPrefix_case5():
    s = Solution()
    assert s.longestCommonPrefix([]) == ""
