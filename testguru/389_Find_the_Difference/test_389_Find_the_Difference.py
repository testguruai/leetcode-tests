import pytest

from solution import Solution

s = Solution()

def test_findTheDifference():
    assert s.findTheDifference("abcd","abcde")=="e"
    assert s.findTheDifference("","x")=="x"
    assert s.findTheDifference("a","aa")=="a"
    assert s.findTheDifference("ae","aea")=="a"
    assert s.findTheDifference("aa","aaa")=="a"