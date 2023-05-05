import collections
import pytest

@pytest.fixture
def solution():
    return Solution()

def test_longestWord_empty_list(solution):
    input_list = []
    expected_output = ''
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_one_word(solution):
    input_list = ['apple']
    expected_output = 'apple'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_multiple_words(solution):
    input_list = ['banana', 'apple', 'pear', 'peach', 'grape', 'orange']
    expected_output = 'apple'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_multiple_words_with_similar_lengths(solution):
    input_list = ['banana', 'car', 'butterfly', 'apple', 'pear', 'peach', 'grape', 'orange']
    expected_output = 'apple'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_multiple_words_with_subwords(solution):
    input_list = ['banana', 'ana', 'chlorine', 'ore', 'orange']
    expected_output = 'banana'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_multiple_words_with_same_subword(solution):
    input_list = ['ana', 'banana', 'man', 'woman']
    expected_output = 'banana'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_multiple_words_with_same_prefix(solution):
    input_list = ['apple', 'app', 'approve', 'appliance']
    expected_output = 'apple'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_same_words(solution):
    input_list = ['book', 'book', 'book']
    expected_output = 'book'
    assert solution.longestWord(input_list) == expected_output

def test_longestWord_long_input_list(solution):
    input_list = ['word'*i for i in range(1, 101)]
    expected_output = 'word'*100
    assert solution.longestWord(input_list) == expected_output