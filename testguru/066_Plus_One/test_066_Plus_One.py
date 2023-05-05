import pytest
from solution import Solution

def test_plusOne():
    s = Solution()
    assert s.plusOne([1,2,3]) == [1,2,4] # Normal case where adding 1 to the last digit
    assert s.plusOne([4,3,2,1]) == [4,3,2,2] # Adding 1 at the end with carry
    assert s.plusOne([9,9,9]) == [1,0,0,0] # Adding 1 at the end with multiple carry
    assert s.plusOne([0]) == [1] # Only one digit
    assert s.plusOne([0,0,0]) == [1,0,0,0] # Multiple zero digits in the middle

def test_plusOne_negative():
    s = Solution()
    assert s.plusOne([1,2,3]) != [1,3,4] # Wrong addition
    assert s.plusOne([4,3,2,1]) != [4,3,2,3] # Wrong carry addition
    assert s.plusOne([9,9,9]) != [1,0,0] # Wrong carry addition
    assert s.plusOne([0]) != [0] # Only one digit but wrong output
    assert s.plusOne([0,0,0]) != [1,0,0] # Multiple zero digits with wrong output.