import pytest
from solution import Solution

def test_reverseWords():
    s = Solution()

    # Test case with no input
    assert s.reverseWords([]) == None

    # Test case with one word input
    word = ['Hello']
    s.reverseWords(word)
    assert word == ['Hello']

    # Test case with two words input
    words = ['Hello', 'World']
    s.reverseWords(words)
    assert words == ['World', 'Hello']

    # Test case with multiple words input
    sentence = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
    s.reverseWords(sentence)
    assert sentence == ['dog', 'lazy', 'the', 'over', 'jumps', 'fox', 'brown', 'quick', 'The']