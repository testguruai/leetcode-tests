import pytest

def test_threeSum():
    s = Solution()
    assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert s.threeSum([0, 0, 0, 0]) == [[0,0,0]]
    assert s.threeSum([-1,0,1,0]) == [[-1,0,1]]
    assert s.threeSum([]) == []
    assert s.threeSum([1,2,3,4]) == []
    assert s.threeSum([1,2,3]) == []
    assert s.threeSum([0,1]) == []
    assert s.threeSum([-2,0,0,2,2]) == [[-2,0,2],[0,0,0],[0,2,2],[-2,2,0]]
    assert s.threeSum([1,-1,-1,0]) == [[-1,0,1]]
    assert s.threeSum([3,0,-2,-1,1,2]) == [[-2,-1,3],[-2,0,2],[-1,0,1]]
    assert s.threeSum([0,0,0]) == [[0,0,0]]
    assert s.threeSum(list(range(-1000, 1000))) == []
    
test_threeSum()