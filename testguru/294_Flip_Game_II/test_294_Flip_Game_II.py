import pytest
from solution import Solution

def test_Solution():
    s = Solution()

    assert s.canWin(None) == False
    assert s.canWin("") == False
    assert s.canWin("++") == True
    assert s.canWin("+") == False
    assert s.canWin("+++++") == True
    assert s.canWin("+--") == False
    assert s.canWin("+--++-++") == True
    assert s.canWin("+-+++-++--++") == False
    assert s.canWin("--++-++--+++") == True
    assert s.canWin("-+-+-+") == False