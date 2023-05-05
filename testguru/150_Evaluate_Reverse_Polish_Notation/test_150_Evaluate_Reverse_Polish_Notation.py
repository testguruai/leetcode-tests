import pytest

def test_evalRPN():
    solution = Solution()
    assert solution.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert solution.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert solution.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert solution.evalRPN(["3", "4", "+"]) == 7
    assert solution.evalRPN(["10", "5", "/", "3", "*"]) == 6
    assert solution.evalRPN(["3"]) == 3
    assert solution.evalRPN([]) == None