import pytest

def test_smallestEvenMultiple():
    solution = Solution()
    
    # Test case when n is already a multiple of 2
    assert solution.smallestEvenMultiple(6) == 6
    
    # Test case when n is odd
    assert solution.smallestEvenMultiple(5) == 10
    
    # Test case for minimum value of n
    assert solution.smallestEvenMultiple(1) == 2
    
    # Test case for maximum value of n
    assert solution.smallestEvenMultiple(1000000) == 1000000 * 2
    
    # Test case for zero
    assert solution.smallestEvenMultiple(0) == 0
    
    # Test case for negative value of n
    with pytest.raises(ValueError):
        solution.smallestEvenMultiple(-3)