
def test_checkSubarraySum():
    s = Solution()
    assert s.checkSubarraySum([23, 2, 4, 6, 7], 6) == True
    assert s.checkSubarraySum([23, 2, 6, 4, 7], 6) == True
    assert s.checkSubarraySum([1, 2, 3, 4, 5], 5) == True
    assert s.checkSubarraySum([0, 0], 0) == True
    assert s.checkSubarraySum([1], 1) == False
