import pytest

@pytest.fixture
def solution():
    return Solution()

def test_is_subsequence_with_subsequence(solution):
    assert solution.isSubsequence("abc", "ahbgdc") == True

def test_is_subsequence_without_subsequence(solution):
    assert solution.isSubsequence("axc", "ahbgdc") == False

def test_is_subsequence_with_empty_strings(solution):
    assert solution.isSubsequence("", "") == True

def test_is_subsequence_with_one_empty_string(solution):
    assert solution.isSubsequence("abc", "") == False

def test_is_subsequence_with_one_char_strings(solution):
    assert solution.isSubsequence("a", "a") == True
    assert solution.isSubsequence("a", "b") == False

def test_is_subsequence_with_long_strings(solution):
    assert solution.isSubsequence("hello", "hxlloeozeeflhblloi") == True
    assert solution.isSubsequence("world", "wofzxrld") == False

def test_is_subsequence_with_symbols(solution):
    assert solution.isSubsequence("!!!", "tr!vial!!!") == True
    assert solution.isSubsequence(":-)", "_-:_*)") == False