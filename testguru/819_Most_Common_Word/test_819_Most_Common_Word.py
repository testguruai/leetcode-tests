import pytest
from solution import Solution

def test_mostCommonWord():
    solution = Solution()
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    assert solution.mostCommonWord(paragraph, banned) == "ball"

    # empty paragraph
    paragraph = ""
    banned = ["hit"]
    assert solution.mostCommonWord(paragraph, banned) == ""

    # all words in paragraph are banned
    paragraph = "hello world"
    banned = ["hello", "world"]
    assert solution.mostCommonWord(paragraph, banned) == ""

    # multiple words with same frequency
    paragraph = "a a b b c"
    banned = []
    assert solution.mostCommonWord(paragraph, banned) in ["a", "b"]

    # all words have same frequency
    paragraph = "hello world"
    banned = []
    assert solution.mostCommonWord(paragraph, banned) in ["hello", "world"]