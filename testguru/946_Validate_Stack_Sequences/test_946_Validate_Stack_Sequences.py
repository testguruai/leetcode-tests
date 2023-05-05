import pytest

from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_validateStackSequences_1(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_2(solution):
    pushed = [2, 1, 0]
    popped = [1, 2, 0]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_3(solution):
    pushed = [1, 0, 3, 2]
    popped = [0, 1, 2, 3]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_4(solution):
    pushed = [1, 2, 3]
    popped = [3, 2, 1]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_5(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_6(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 1, 2]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_7(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [5, 4, 3, 2, 1]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_8(solution):
    pushed = []
    popped = []
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_9(solution):
    pushed = [1]
    popped = [2]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_10(solution):
    pushed = [1]
    popped = [1]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_11(solution):
    pushed = [1, 2, 3]
    popped = [3, 1, 2]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_12(solution):
    pushed = [1, 2, 3]
    popped = [1, 2, 3, 4]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_13(solution):
    pushed = [1, 2, 3]
    popped = [3, 2, 1]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_14(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 2, 3, 4, 5]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_15(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 2, 3, 5, 4]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_16(solution):
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 2, 3, 5, 4, 6]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_17(solution):
    pushed = [1, 2, 3, 4, 5, 6]
    popped = [1, 2, 3, 4, 5, 6]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_18(solution):
    pushed = [1, 2, 3, 4, 5, 6]
    popped = [1, 2, 3, 4, 6, 5]
    assert solution.validateStackSequences(pushed, popped) == False

def test_validateStackSequences_19(solution):
    pushed = [1, 2, 3, 4, 5, 6]
    popped = [6, 5, 4, 3, 2, 1]
    assert solution.validateStackSequences(pushed, popped) == True

def test_validateStackSequences_20(solution):
    pushed = [1, 2, 3, 4, 5, 6]
    popped = [6, 5, 4, 3, 1, 2]
    assert solution.validateStackSequences(pushed, popped) == False