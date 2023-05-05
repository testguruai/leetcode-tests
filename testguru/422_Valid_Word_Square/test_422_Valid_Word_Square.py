
import pytest
from solution import Solution

def test_validWordSquare1():
    sol = Solution()
    words = ["abcd", "bnrt", "crmy", "dtye"]
    assert sol.validWordSquare(words) == True
    
def test_validWordSquare2():
    sol = Solution()
    words = ["abcd", "bnrt", "crm", "dt"]
    assert sol.validWordSquare(words) == True
    
def test_validWordSquare3():
    sol = Solution()
    words = ["ball", "area", "read", "lady"]
    assert sol.validWordSquare(words) == False
    
def test_validWordSquare4():
    sol = Solution()
    words = []
    assert sol.validWordSquare(words) == True
    
def test_validWordSquare5():
    sol = Solution()
    words = ["abcd", "efgh"]
    assert sol.validWordSquare(words) == False
