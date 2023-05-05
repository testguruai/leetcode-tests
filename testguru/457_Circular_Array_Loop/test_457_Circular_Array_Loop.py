import pytest
from typing import List
from solution import Solution

def test_circularArrayLoop():
    s = Solution()

    nums1 = [2,-1,1,2,2]
    assert s.circularArrayLoop(nums1) == True

    nums2 = [-1,2]
    assert s.circularArrayLoop(nums2) == False

    nums3 = [-2,1,-1,-2,-2]
    assert s.circularArrayLoop(nums3) == False

    nums4 = [1,1,1,1,1]
    assert s.circularArrayLoop(nums4) == True

    nums5 = [2,2,-1,2,2]
    assert s.circularArrayLoop(nums5) == True

    nums6 = [2,2,-3,2,2]
    assert s.circularArrayLoop(nums6) == False

    nums7 = [-2,5,-1,-2,-3]
    assert s.circularArrayLoop(nums7) == True

    nums8 = [1,2,3,4,5]
    assert s.circularArrayLoop(nums8) == False

pytest.main(["-v", "--tb=line", "-rN", "test_solution.py"])