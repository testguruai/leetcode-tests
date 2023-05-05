import pytest

from solution import Solution

@pytest.fixture
def solution_obj():
    return Solution()

def test_case_1(solution_obj):
    A = [3, 1, 3, 6]
    assert solution_obj.canReorderDoubled(A) == False

def test_case_2(solution_obj):
    A = [2, 1, 2, 6]
    assert solution_obj.canReorderDoubled(A) == False
    
def test_case_3(solution_obj):
    A = [4, -2, 2, -4]
    assert solution_obj.canReorderDoubled(A) == True
    
def test_case_4(solution_obj):
    A = [1, 2, 4, 16, 8, 4]
    assert solution_obj.canReorderDoubled(A) == True
