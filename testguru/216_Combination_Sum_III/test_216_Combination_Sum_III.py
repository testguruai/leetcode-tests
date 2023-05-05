
from solution import Solution

def test_combinationSum3():
	sol = Solution()
	
	# Test case 1: k = 3 and n = 7
	assert sol.combinationSum3(3, 7) == [[1,2,4]]
	
	# Test case 2: k = 3 and n = 9
	assert sol.combinationSum3(3, 9) == [[1,2,6], [1,3,5], [2,3,4]]
	
	# Test case 3: k = 4 and n = 1
	assert sol.combinationSum3(4, 1) == []
	
	# Test case 4: k = 2 and n = 30
	assert sol.combinationSum3(2, 30) == []
	
	# Test case 5: k = 0 and n = 0
	assert sol.combinationSum3(0, 0) == []
