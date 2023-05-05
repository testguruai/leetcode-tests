
import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_canPermutePalindrome_true(solution):
    assert solution.canPermutePalindrome("aab") == True
    assert solution.canPermutePalindrome("carerac") == True
    assert solution.canPermutePalindrome("racecar") == True

def test_canPermutePalindrome_false(solution):
    assert solution.canPermutePalindrome("code") == False
    assert solution.canPermutePalindrome("hello") == False

def test_canPermutePalindrome_empty_string(solution):
    assert solution.canPermutePalindrome("") == True

def test_canPermutePalindrome_single_character(solution):
    assert solution.canPermutePalindrome("a") == True

def test_canPermutePalindrome_even_length(solution):
    assert solution.canPermutePalindrome("abccba") == True
    assert solution.canPermutePalindrome("aabbcc") == True

def test_canPermutePalindrome_odd_length(solution):
    assert solution.canPermutePalindrome("abcba") == True
    assert solution.canPermutePalindrome("aaabbbbccc") == False
