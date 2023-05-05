import pytest

from solution import Solution

def test_searchInsert():
    s = Solution()
    assert s.searchInsert([1,3,5,6], 5) == 2
    assert s.searchInsert([1,3,5,6], 2) == 1
    assert s.searchInsert([1,3,5,6], 7) == 4
    assert s.searchInsert([1,3,5,6], 0) == 0
    assert s.searchInsert([], 5) == 0
    
    # additional tests
    assert s.searchInsert([1,3,5,6], 6) == 3
    assert s.searchInsert([1,3,5,6], 4) == 2
    assert s.searchInsert([1,3,5,6], 3) == 1
    assert s.searchInsert([1], 1) == 0
    assert s.searchInsert([1], 2) == 1
    assert s.searchInsert([1,2,3,4,5,6,7,8,9,10], 5) == 4
    assert s.searchInsert([1,2,3,4,5,6,7,8,9,10], 11) == 10
    assert s.searchInsert([1,2,3,4,5,6,7,8,9,10], 0) == 0
    
if __name__ == '__main__':
    pytest.main(['test_solution.py'])