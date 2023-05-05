
import pytest

from solution import Solution

def test_partition():
    s = Solution()

    assert s.partition("aab") == [['a', 'a', 'b'], ['aa', 'b']]
    assert s.partition("a") == [['a']]
    assert s.partition("abc") == [['a', 'b', 'c']]
    assert s.partition("") == [[]]

def test_isPalindrome():
    s = Solution()

    assert s.isPalindrome("racecar", 0, 6) == True
    assert s.isPalindrome("hello", 0, 4) == False
    assert s.isPalindrome("", 0, 0) == True
    assert s.isPalindrome("a", 0, 0) == True
