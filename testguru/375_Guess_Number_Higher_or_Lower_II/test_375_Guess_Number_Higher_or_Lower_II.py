import pytest
from solution import Solution

def test_top_down_dp():
    s = Solution()
    assert s.getMoneyAmount(5) == 6
    assert s.getMoneyAmount(10) == 16
    
def test_bottom_up_dp():
    s = Solution()
    assert s.getMoneyAmount(5) == 6
    assert s.getMoneyAmount(10) == 16