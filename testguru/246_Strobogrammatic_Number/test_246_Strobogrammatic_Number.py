import pytest
from solution import Solution

def test_isStrobogrammatic():
    sol = Solution()
    assert sol.isStrobogrammatic('69') == True
    assert sol.isStrobogrammatic('88') == True
    assert sol.isStrobogrammatic('818') == True
    assert sol.isStrobogrammatic('963') == False
    assert sol.isStrobogrammatic('19') == False
    assert sol.isStrobogrammatic('621') == False
    assert sol.isStrobogrammatic('101') == True
    assert sol.isStrobogrammatic('6009') == True
    assert sol.isStrobogrammatic('6109') == False
    assert sol.isStrobogrammatic('88888') == True
    assert sol.isStrobogrammatic('693') == False