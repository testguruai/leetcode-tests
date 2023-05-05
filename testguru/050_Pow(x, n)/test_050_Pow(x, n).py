import pytest

from solution import Solution


def test_myPow():
    sol = Solution()
    
    # Test case 1
    assert round(sol.myPow(2, 10), 2) == 1024.00
    
    # Test case 2
    assert round(sol.myPow(2.1, 3), 2) == 9.26
    
    # Test case 3
    assert round(sol.myPow(2, -2), 2) == 0.25
    
    # Test case 4
    assert round(sol.myPow(0.00001, 2147483647), 5) == 0.0
    
    # Test case 5
    assert sol.myPow(0, 0) == 1.0
    
    # Test case 6
    assert sol.myPow(3, 0) == 1.0
    
    # Test case 7
    assert round(sol.myPow(2, -4), 2) == 0.06
    
    # Test case 8
    assert round(sol.myPow(-1, -2147483648), 5) == 1.0