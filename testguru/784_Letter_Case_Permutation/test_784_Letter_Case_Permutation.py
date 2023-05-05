import pytest

from solution import Solution

def test_letterCasePermutation():
    sol = Solution()
    # Test case where all characters are alphabets
    assert set(sol.letterCasePermutation("aBc")) == set(['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC'])

    # Test case where all characters are numbers
    assert sol.letterCasePermutation("123") == ['123']

    # Test case where all characters are special characters
    assert sol.letterCasePermutation("~!@") == ['~!@']

    # Test case where input string is empty
    assert sol.letterCasePermutation("") == ['']

    # Test case where input string has only one character
    assert set(sol.letterCasePermutation("a")) == set(['a', 'A'])

    # Test case where input string has only one uppercase character
    assert set(sol.letterCasePermutation("A")) == set(['a', 'A'])

    # Test case where input string has only one lowercase character
    assert set(sol.letterCasePermutation("z")) == set(['z', 'Z'])

    # Test case where input string has both uppercase and lowercase characters
    assert set(sol.letterCasePermutation("Abc")) == set(['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC'])

    # Test case where input string has both alphabets and special characters
    assert set(sol.letterCasePermutation("a!b@c#")) == set(['a!b@c#', 'a!b@C#', 'a!B@c#', 'a!B@C#', 'A!b@c#', 'A!b@C#', 'A!B@c#', 'A!B@C#'])