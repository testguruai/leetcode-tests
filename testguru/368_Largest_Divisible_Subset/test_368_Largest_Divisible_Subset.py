def test_largestDivisibleSubset():
    obj = Solution()
    assert obj.largestDivisibleSubset([1,2,3]) == [1,2], "Error: Test Case 1"
    assert obj.largestDivisibleSubset([1,2,4,8]) == [1,2,4,8], "Error: Test Case 2"
    assert obj.largestDivisibleSubset([1,2,3,5,7,11]) == [1], "Error: Test Case 3"
    assert obj.largestDivisibleSubset([2,3,4,9,27]) == [3,9,27], "Error: Test Case 4"
    assert obj.largestDivisibleSubset([10,20,30,40,50]) == [10,20,40], "Error: Test Case 5"
    assert obj.largestDivisibleSubset([3,6,9,12,15,18,21,24,27]) == [3,6,9,12,15,18,21,24,27], "Error: Test Case 6"