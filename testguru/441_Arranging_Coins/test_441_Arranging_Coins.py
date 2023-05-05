
import pytest
from solution import Solution

def test_arrangeCoins():
    sol = Solution()
    assert sol.arrangeCoins(0) == 0
    assert sol.arrangeCoins(1) == 1
    assert sol.arrangeCoins(2) == 1
    assert sol.arrangeCoins(3) == 2
    assert sol.arrangeCoins(5) == 2
