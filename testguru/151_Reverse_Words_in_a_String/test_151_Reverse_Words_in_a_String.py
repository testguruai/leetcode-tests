import pytest
from solution import Solution

sol = Solution()

def test_reverseWords_empty_string():
    assert sol.reverseWords("") == ""

def test_reverseWords_only_spaces():
    assert sol.reverseWords("    ") == ""

def test_reverseWords_single_word():
    assert sol.reverseWords("hello") == "hello"

def test_reverseWords_multiple_words():
    assert sol.reverseWords("The sky is blue") == "blue is sky The"

def test_reverseWords_spaces_between_words():
    assert sol.reverseWords("   The    sky  is   blue  ") == "blue is sky The"

def test_reverseWords_complex_string():
    assert sol.reverseWords("      this is a test phrase with spaces and punctuation marks!    ") == "!marks punctuation and spaces with phrase test a is this"
