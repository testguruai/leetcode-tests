import pytest
from solution import Solution

def test_minWindow():
    s = Solution()
    assert s.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
    assert s.minWindow('a', 'a') == 'a'
    assert s.minWindow('a', 'aa') == ''
    assert s.minWindow('abc', 'cba') == ''

def test_first_match():
    s = Solution()
    assert s.first_match('ADOBECODEBANC', 'ABC') == (9, 12, {})
    assert s.first_match('a', 'a') == (0, 0, {})
    assert s.first_match('a', 'aa') == False
    assert s.first_match('abc', 'cba') == False