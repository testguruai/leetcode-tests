import pytest

from solution import Solution

def test_numTrees():
    sol = Solution()
    n = 3
    assert sol.numTrees(n) == 5
    
    n = 0
    assert sol.numTrees(n) == 1
    
    n = 1
    assert sol.numTrees(n) == 1
    
    n = 2
    assert sol.numTrees(n) == 2
    
    n = 4
    assert sol.numTrees(n) == 14