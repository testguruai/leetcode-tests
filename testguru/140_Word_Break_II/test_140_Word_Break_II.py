import pytest

from typing import List, Set

from .filename import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, wordDict, expected",
    [
        ("leetcode", set(["leet", "code"]), ["leet code"]),
        ("applepenapple", set(["apple", "pen"]), ["apple pen apple"]),
        ("catsanddog", set(["cat", "cats", "and", "sand", "dog"]), ["cats and dog", "cat sand dog"]),
    ]
)
def test_word_break(solution, s: str, wordDict: Set[str], expected: List[str]):
    assert solution.wordBreak(s, wordDict) == expected


def test_word_break_with_empty_input(solution):
    assert solution.wordBreak("", set()) == []


def test_word_break_with_no_words_in_dict(solution):
    assert solution.wordBreak("foo", set(["bar", "baz"])) == []


def test_word_break_with_one_word_in_dict(solution):
    assert solution.wordBreak("bar", set(["bar", "baz"])) == ["bar"]