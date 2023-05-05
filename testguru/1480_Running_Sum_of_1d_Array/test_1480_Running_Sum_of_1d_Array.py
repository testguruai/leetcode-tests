
# Test case 1
def test_runningSum_empty():
    solution = Solution()
    assert solution.runningSum([]) == []

# Test case 2
def test_runningSum_single_value():
    solution = Solution()
    assert solution.runningSum([5]) == [5]

# Test case 3
def test_runningSum_multiple_values():
    solution = Solution()
    assert solution.runningSum([1, 2, 3, 4, 5]) == [1, 3, 6, 10, 15]