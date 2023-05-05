import pytest
from typing import List
from solution import Solution

def test_xorQueries():
    s = Solution()
    # Test case 1
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]
    expected_output = [2,7,14,8]
    assert s.xorQueries(arr, queries) == expected_output
    
    # Test case 2
    arr = [4,8,2,10]
    queries = [[2,3],[1,3]]
    expected_output = [8,0]
    assert s.xorQueries(arr, queries) == expected_output
    
    # Test case 3
    arr = [5,6,7,8]
    queries = [[0,3],[1,2],[2,3]]
    expected_output = [14,1,15]
    assert s.xorQueries(arr, queries) == expected_output
    
    # Test case 4
    arr = [1,1,1,1]
    queries = [[0,0],[1,1],[2,2],[3,3]]
    expected_output = [1,1,1,1]
    assert s.xorQueries(arr, queries) == expected_output
    
    # Test case 5
    arr = [2,2]
    queries = [[1,1]]
    expected_output = [2]
    assert s.xorQueries(arr, queries) == expected_output