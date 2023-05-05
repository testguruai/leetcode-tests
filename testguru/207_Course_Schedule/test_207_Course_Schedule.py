import pytest
from collections import defaultdict

from solution import Solution

def test_canFinish():
    s = Solution()
    
    # Test case where there is no cycle
    assert s.canFinish(3, [[0,1], [1,2]]) == True
    
    # Test case where there is a cycle
    assert s.canFinish(3, [[0,1], [1,2], [2,0]]) == False
    
    # Test case where number of courses is 0
    assert s.canFinish(0, []) == True
    
    # Test case where there is only 1 course
    assert s.canFinish(1, []) == True
    
    # Test case where there are multiple prerequisites for a single course
    assert s.canFinish(3, [[0,1], [0,2]]) == True
    
    # Test case where all courses have prerequisites
    assert s.canFinish(3, [[1,0], [2,1], [2,0]]) == True
    
    # Test case where all courses have prerequisites and there is a cycle
    assert s.canFinish(3, [[1,0], [2,1], [2,0], [0,2]]) == False