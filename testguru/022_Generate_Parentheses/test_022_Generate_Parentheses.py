import pytest

from solution import Solution

def test_generateParenthesis():
    sol = Solution()
    assert sol.generateParenthesis(1) == ['()']
    assert sol.generateParenthesis(2) == ['()()', '(())']
    assert sol.generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'] 
    assert sol.generateParenthesis(0) == [] # Edge case: empty string
    assert sol.generateParenthesis(-1) == [] # Edge case: negative integer