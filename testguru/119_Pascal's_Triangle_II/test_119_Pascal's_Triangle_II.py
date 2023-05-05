import pytest
from solution import Solution

def test_Solution():
    s = Solution()
    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1,1]
    assert s.getRow(2) == [1,2,1]
    assert s.getRow(3) == [1,3,3,1]
    assert s.getRow(4) == [1,4,6,4,1]
    assert s.getRow(5) == [1,5,10,10,5,1]
    assert s.getRow(6) == [1,6,15,20,15,6,1]