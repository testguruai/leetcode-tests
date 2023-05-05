import pytest

@pytest.fixture
def solution():
    from solution import Solution
    return Solution()

def test_empty_string(solution):
    assert solution.lengthOfLastWord('') == 0

def test_one_word(solution):
    assert solution.lengthOfLastWord('hello') == 5

def test_multiple_spaces(solution):
    assert solution.lengthOfLastWord('     ') == 0

def test_multiple_words(solution):
    assert solution.lengthOfLastWord('hello world') == 5

def test_last_word_has_spaces(solution):
    assert solution.lengthOfLastWord('hello world    ') == 5

def test_first_word_has_spaces(solution):
    assert solution.lengthOfLastWord('   hello') == 5

def test_all_spaces_except_one_word(solution):
    assert solution.lengthOfLastWord('       hello     ') == 5

def test_only_spaces(solution):
    assert solution.lengthOfLastWord('       ') == 0

def test_unicode_string(solution):
    assert solution.lengthOfLastWord('💻 hello world') == 5

def test_numbers_in_string(solution):
    assert solution.lengthOfLastWord('hello123') == 7