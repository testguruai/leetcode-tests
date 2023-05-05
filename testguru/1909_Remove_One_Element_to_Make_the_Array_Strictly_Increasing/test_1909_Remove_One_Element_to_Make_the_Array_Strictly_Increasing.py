import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_canBeIncreasing_1(solution):
    assert solution.canBeIncreasing([1,2,10,5,7]) == True
    
def test_canBeIncreasing_2(solution):
    assert solution.canBeIncreasing([1,2,3,4,5]) == True
    
def test_canBeIncreasing_3(solution):
    assert solution.canBeIncreasing([1,2,3,10,5,6]) == True
    
def test_canBeIncreasing_4(solution):
    assert solution.canBeIncreasing([1,1,1]) == False
    
def test_canBeIncreasing_5(solution):
    assert solution.canBeIncreasing([10,9,8]) == False
    
def test_canBeIncreasing_6(solution):
    assert solution.canBeIncreasing([1,2,3,4,5,6,7,8,9,10]) == True
    
def test_canBeIncreasing_7(solution):
    assert solution.canBeIncreasing([4,5,6,7,1,2,10]) == True
    
def test_canBeIncreasing_8(solution):
    assert solution.canBeIncreasing([3,2,1,5,6,4]) == False
    
def test_canBeIncreasing_9(solution):
    assert solution.canBeIncreasing([1,2,5,3,4,4]) == False
    
def test_canBeIncreasing_10(solution):
    assert solution.canBeIncreasing([1,5,2,3,4]) == True