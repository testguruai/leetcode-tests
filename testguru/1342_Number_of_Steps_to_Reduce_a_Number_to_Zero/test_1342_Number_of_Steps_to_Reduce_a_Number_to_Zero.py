import pytest
from solution import Solution

def test_number_of_steps():
    s = Solution()
    assert s.numberOfSteps(14) == 6
    assert s.numberOfSteps(8) == 4
    assert s.numberOfSteps(123) == 12
    assert s.numberOfSteps(0) == 0
    assert s.numberOfSteps(1) == 1
    assert s.numberOfSteps(2) == 2
    assert s.numberOfSteps(3) == 3
    assert s.numberOfSteps(10) == 5

def test_number_of_steps_large_input():
    s = Solution()
    assert s.numberOfSteps(10**6) == 28

def test_number_of_steps_invalid_input():
    s = Solution()
    with pytest.raises(TypeError):
        s.numberOfSteps("abc")
    with pytest.raises(ValueError):
        s.numberOfSteps(-1)
    with pytest.raises(ValueError):
        s.numberOfSteps(10**7)