import pytest

from solution import Solution

def test_peakIndexInMountainArray():
    s = Solution()
    assert s.peakIndexInMountainArray([0,1,0])==1
    assert s.peakIndexInMountainArray([0,2,1,0])==1
    assert s.peakIndexInMountainArray([0,1,2,3,4,5,6,7,5,4,3,2,1,0]) == 7
    assert s.peakIndexInMountainArray([0,1,2,3,4,5,6,7])==7
    assert s.peakIndexInMountainArray([7,6,5,4,3,2,1,0])==0
    assert s.peakIndexInMountainArray([1])==0
    assert s.peakIndexInMountainArray([1,2])==1
    assert s.peakIndexInMountainArray([3,2,1])==0
    assert s.peakIndexInMountainArray([1,2,3])==2
    assert s.peakIndexInMountainArray([3,2,1,3])==0
    assert s.peakIndexInMountainArray([1,2,3,1])==2