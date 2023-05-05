import pytest

from solution import Solution


@pytest.fixture
def solution():
    return Solution()


def test_isAlienSorted_true(solution):
    assert solution.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz") == True


def test_isAlienSorted_false(solution):
    assert solution.isAlienSorted(["word", "world", "row"], "worldabcefghijkmnpqstuvxyz") == False


def test_isAlienSorted_same_prefix(solution):
    assert solution.isAlienSorted(["apple", "app"], "abcdefghijklmnopqrstuvwxyz") == False


def test_isAlienSorted_empty_words(solution):
    assert solution.isAlienSorted([], "abcdefghijklmnopqrstuvwxyz") == True


def test_isAlienSorted_empty_order(solution):
    assert solution.isAlienSorted(["hello", "leetcode"], "") == True


def test_isAlienSorted_single_word(solution):
    assert solution.isAlienSorted(["hello"], "hlabcdefgijkmnopqrstuvwxyz") == True


def test_isAlienSorted_duplicate_words(solution):
    assert solution.isAlienSorted(["world", "world"], "worldabcefghijkmnpqstuvxyz") == True