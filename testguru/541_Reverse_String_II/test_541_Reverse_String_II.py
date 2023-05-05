import pytest

@pytest.fixture
def solution():
    return Solution()

def test_reverseStr_even_length(solution):
    assert solution.reverseStr("abcdefgh", 2) == "bacdfegh"

def test_reverseStr_odd_length(solution):
    assert solution.reverseStr("abcdefghi", 2) == "bacdfeghgi"

def test_reverseStr_k_greater_than_length(solution):
    assert solution.reverseStr("abcdefg", 10) == "gfedcba"

def test_reverseStr_k_equals_to_length(solution):
    assert solution.reverseStr("abc", 3) == "cba"

def test_reverseStr_empty_string(solution):
    assert solution.reverseStr("", 2) == ""

def test_reverseStr_single_character_not_reversed(solution):
    assert solution.reverseStr("a", 2) == "a" 

def test_reverseStr_single_character_reversed(solution):
    assert solution.reverseStr("a", 1) == "a"
    
def test_reverseStr_all_characters_reversed(solution):
    assert solution.reverseStr("abcdefg", 1) == "gfedcba"