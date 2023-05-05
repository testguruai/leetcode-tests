
def test_search():
    s = Solution()
    
    # Test case where target is found in the middle of the array
    assert s.search([4,5,6,7,0,1,2], 0) == 4
    
    # Test case where target is found at the beginning of the array
    assert s.search([4,5,6,7,0,1,2], 4) == 0
    
    # Test case where target is found at the end of the array
    assert s.search([4,5,6,7,0,1,2], 2) == 6
    
    # Test case where target is not in the array
    assert s.search([4,5,6,7,0,1,2], 3) == -1
    
    # Test case where the array is empty
    assert s.search([], 0) == -1
    
    # Test case where the array has length 1 and target is in the array
    assert s.search([3], 3) == 0
    
    # Test case where the array has length 1 and target is not in the array
    assert s.search([3], 4) == -1
