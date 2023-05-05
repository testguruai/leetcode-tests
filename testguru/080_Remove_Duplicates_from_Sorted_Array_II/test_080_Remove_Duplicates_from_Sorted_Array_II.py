import pytest
from solution import Solution

def test_removeDuplicates():
    s = Solution()
    
    # Test case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    expected1 = 5
    assert s.removeDuplicates(nums1) == expected1
    
    # Test case 2
    nums2 = [0,0,1,1,1,1,2,3,3]
    expected2 = 7
    assert s.removeDuplicates(nums2) == expected2
    
    # Test case 3
    nums3 = []
    expected3 = 0
    assert s.removeDuplicates(nums3) == expected3
    
    # Test case 4
    nums4 = [1]
    expected4 = 1
    assert s.removeDuplicates(nums4) == expected4
    
    # Test case 5
    nums5 = [1, 2, 3, 4, 5]
    expected5 = 5
    assert s.removeDuplicates(nums5) == expected5
    
    # Test case 6
    nums6 = [1, 1, 1, 1, 1]
    expected6 = 2
    assert s.removeDuplicates(nums6) == expected6
