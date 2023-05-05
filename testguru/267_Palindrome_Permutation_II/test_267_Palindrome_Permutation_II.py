import pytest
from solution import Solution

def test_generatePalindromes_returns_correct_output():
    s = "aab"
    expected_output = ['aba', 'aab', 'baa']
    assert Solution().generatePalindromes(s) == expected_output

def test_generatePalindromes_returns_empty_list_if_odd_count_of_chars_greater_than_1():
    s = "aabbcc"
    assert Solution().generatePalindromes(s) == []

def test_permute_returns_correct_output():
    res = []
    num = ['a', 'b', 'c']
    index = 0
    Solution().permute(res, num, index)
    expected_output = [['a', 'b', 'c'], ['a', 'c', 'b'], ['b', 'a', 'c'], ['b', 'c', 'a'], ['c', 'b', 'a'], ['c', 'a', 'b']]
    assert res == expected_output

def test_permute_returns_correct_output_with_repeated_chars():
    res = []
    num = ['a', 'a', 'b']
    index = 0
    Solution().permute(res, num, index)
    expected_output = [['a', 'a', 'b'], ['a', 'b', 'a'], ['b', 'a', 'a']]
    assert res == expected_output

def test_permute_returns_correct_output_with_empty_list():
    res = []
    num = []
    index = 0
    Solution().permute(res, num, index)
    expected_output = [[]]
    assert res == expected_output