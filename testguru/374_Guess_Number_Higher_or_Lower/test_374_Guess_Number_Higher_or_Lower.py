import pytest

from solution import Solution

def test_guessNumber():
    s = Solution()
    assert s.guessNumber(10) == 6
    assert s.guessNumber(1) == 1
    assert s.guessNumber(2) in [1,2]
    assert s.guessNumber(100) == 50
    assert s.guessNumber(200) == 100
    assert s.guessNumber(1000) == 500
