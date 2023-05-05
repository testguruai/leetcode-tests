import pytest
from solution import Solution

def test_subarraySum():
    s = Solution()
    assert s.subarraySum([1, 1, 1], 2) == 2
    assert s.subarraySum([1, 2, 3], 3) == 2
    assert s.subarraySum([1, -1, 0], 0) == 3
    assert s.subarraySum([1, -1, 1], 0) == 2
    assert s.subarraySum([0, 0, 0], 0) == 6