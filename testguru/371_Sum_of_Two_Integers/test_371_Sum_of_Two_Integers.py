import pytest
from solution import Solution

def test_get_sum():
    sol = Solution()
    
    # Testing with positive numbers
    assert sol.getSum(2, 3) == 5
    assert sol.getSum(10, 15) == 25
    assert sol.getSum(17, 38) == 55
    
    # Testing with negative numbers
    assert sol.getSum(-3, -7) == -10
    assert sol.getSum(-15, -20) == -35
    assert sol.getSum(-50, -100) == -150
    
    # Testing with a negative and positive number
    assert sol.getSum(-5, 8) == 3
    assert sol.getSum(10, -20) == -10
    assert sol.getSum(15, -50) == -35
    
    # Testing with zero
    assert sol.getSum(0, 10) == 10
    assert sol.getSum(0, -10) == -10
    assert sol.getSum(0, 0) == 0