
import pytest

from solution import Solution

def test_canWinNim_true():
    s = Solution()
    assert s.canWinNim(1) == True
    assert s.canWinNim(2) == True
    assert s.canWinNim(3) == True
    
def test_canWinNim_false():
    s = Solution()
    assert s.canWinNim(4) == False
    assert s.canWinNim(8) == False
    assert s.canWinNim(12) == False
    
def test_canWinNim_zero():
    s = Solution()
    assert s.canWinNim(0) == False
    
def test_canWinNim_negative():
    s = Solution()
    with pytest.raises(ValueError):
        s.canWinNim(-1)
