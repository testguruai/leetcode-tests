
import pytest
from solution import Solution

def test_max_profit():
    sol = Solution()
    
    # Test case 1: Empty input list
    assert sol.maxProfit([]) == 0
    
    # Test case 2: List with only one item
    assert sol.maxProfit([7]) == 0
    
    # Test case 3: Increasing prices
    assert sol.maxProfit([1,2,3,4,5]) == 4
    
    # Test case 4: Decreasing prices
    assert sol.maxProfit([5,4,3,2,1]) == 0
    
    # Test case 5: Increasing, then decreasing prices
    assert sol.maxProfit([1,2,3,4,5,4,3,2,1]) == 4
    
    # Test case 6: Decreasing, then increasing prices
    assert sol.maxProfit([5,4,3,2,1,2,3,4,5]) == 4
    
    # Test case 7: Multiple local maximums
    assert sol.maxProfit([1,2,3,2,3,4,3,4,5]) == 4
    
    # Test case 8: Multiple local minimums
    assert sol.maxProfit([5,4,3,6,5,4,7,6,5]) == 4
