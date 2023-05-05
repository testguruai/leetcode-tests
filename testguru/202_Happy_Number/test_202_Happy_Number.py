import pytest
from solution import Solution

sol = Solution()

def test_happy_number():
    assert sol.isHappy(19) == True
    assert sol.isHappy(7) == True
    assert sol.isHappy(139) == True
    assert sol.isHappy(82) == True
    assert sol.isHappy(30) == False
    assert sol.isHappy(0) == False
    assert sol.isHappy(-7) == False
    assert sol.isHappy(2.5) == False

def test_happy_number_with_invalid_input():
    with pytest.raises(TypeError):
        assert sol.isHappy("19")
        assert sol.isHappy("number")
        assert sol.isHappy([19, 20])
        assert sol.isHappy(True, False)