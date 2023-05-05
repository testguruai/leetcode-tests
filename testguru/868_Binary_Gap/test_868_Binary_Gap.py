import pytest

solution = Solution()

def test_binaryGap():
    assert solution.binaryGap(9) == 2
    assert solution.binaryGap(529) == 4
    assert solution.binaryGap(20) == 1
    assert solution.binaryGap(15) == 0
    assert solution.binaryGap(32) == 0
    assert solution.binaryGap(1) == 0

    
def test_binaryGap_negative_input():
    with pytest.raises(ValueError):
        solution.binaryGap(-5)
    with pytest.raises(ValueError):
        solution.binaryGap(-20)
        
def test_binaryGap_zero_input():
    assert solution.binaryGap(0) == 0