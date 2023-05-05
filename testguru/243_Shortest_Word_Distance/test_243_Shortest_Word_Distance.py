import pytest
from .solution import Solution

@pytest.fixture(scope="module")
def solution():
    return Solution()

def test_shortestDistance_same_words(solution):
    words = ["hello", "world", "world", "python", "world", "programming"]
    assert solution.shortestDistance(words, "world", "world") == 0

def test_shortestDistance_adjacent_words(solution):
    words = ["hello", "world", "python", "programming"]
    assert solution.shortestDistance(words, "hello", "world") == 1

def test_shortestDistance_different_positions(solution):
    words = ["hello", "world", "python", "programming"]
    assert solution.shortestDistance(words, "hello", "programming") == 3

def test_shortestDistance_one_word_does_not_exist(solution):
    words = ["hello", "world", "python", "programming"]
    assert solution.shortestDistance(words, "hello", "javascript") == len(words)

def test_shortestDistance_empty_list(solution):
    words = []
    assert solution.shortestDistance(words, "hello", "world") == len(words)