import pytest
from solution import Solution

def test_findMedianSortedArrays():
    s = Solution()
    assert s.findMedianSortedArrays([1,2], [3,4]) == 2.5
    assert s.findMedianSortedArrays([1,2], [3]) == 2.0
    assert s.findMedianSortedArrays([1,3,5,7,9], [2,4,6,8,10]) == 5.5
    assert s.findMedianSortedArrays([1,1], [1,2]) == 1.0
    assert s.findMedianSortedArrays([1,2], []) == 1.5
