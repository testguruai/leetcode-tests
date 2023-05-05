import pytest
from solution import Solution

def test_productExceptSelf():
    s = Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([0,1,2]) == [2, 0, 0]
    assert s.productExceptSelf([5,6,7]) == [42, 35, 30]
    assert s.productExceptSelf([1,2,3,0,5]) == [0, 0, 0, 30, 0]
    assert s.productExceptSelf([1,3,0,2,5]) == [0, 0, 30, 0, 0]
    assert s.productExceptSelf([]) == []
    assert s.productExceptSelf([0]) == [1]