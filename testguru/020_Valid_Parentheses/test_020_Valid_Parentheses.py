import pytest
from solution import Solution

def test_isValid():
    solver = Solution()

    # Test empty input
    assert solver.isValid(None) == True
    assert solver.isValid("") == True

    # Test inputs with only one bracket
    assert solver.isValid("(") == False
    assert solver.isValid(")") == False
    assert solver.isValid("{") == False
    assert solver.isValid("}") == False
    assert solver.isValid("[") == False
    assert solver.isValid("]") == False

    # Test inputs with only valid brackets
    assert solver.isValid("()") == True
    assert solver.isValid("[]") == True
    assert solver.isValid("{}") == True
    assert solver.isValid("()[]{}") == True

    # Test inputs with only invalid brackets
    assert solver.isValid("([)]") == False
    assert solver.isValid("{{}") == False
    assert solver.isValid("(()") == False

    # Test inputs with mixed brackets
    assert solver.isValid("([{}])") == True
    assert solver.isValid("([{()}][])") == True
    assert solver.isValid("(){}[({})]") == True
    assert solver.isValid("((){}[()])") == True

    assert solver.isValid("([{}])(){}[({})]") == True
    assert solver.isValid("[{]([}])") == False
    assert solver.isValid("({[}])") == False
    assert solver.isValid("(((()))") == False
    assert solver.isValid("(())))") == False
