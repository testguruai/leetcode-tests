import pytest
from solution import Solution

s = Solution()

def test_grayCode():
    assert s.grayCode(2) == [0,1,3,2]

def test_grayCode_empty():
    assert not s.grayCode(0)

def test_grayCode_invalid_input():
    with pytest.raises(TypeError):
        s.grayCode('a')
    with pytest.raises(TypeError):
        s.grayCode(1.5)
    with pytest.raises(ValueError):
        s.grayCode(-1)