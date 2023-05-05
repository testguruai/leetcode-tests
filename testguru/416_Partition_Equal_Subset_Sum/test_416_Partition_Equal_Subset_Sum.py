import pytest

class TestSolution(object):
    def test_canPartition_returns_true_for_valid_input(self):
        sol = Solution()
        assert sol.canPartition([1,5,11,5]) == True
        assert sol.canPartition([2,2,3,5]) == True
        assert sol.canPartition([1,2,3,4,5,6]) == True
    
    def test_canPartition_returns_false_for_invalid_input(self):
        sol = Solution()
        assert sol.canPartition([1,2,3,5]) == False
        assert sol.canPartition([2,3,5,7]) == False
        assert sol.canPartition([5,5,5,5]) == False
        
    def test_canPartition_returns_false_for_empty_input(self):
        sol = Solution()
        assert sol.canPartition([]) == False
        
    def test_canPartition_returns_false_for_None_input(self):
        sol = Solution()
        assert sol.canPartition(None) == False
        
    def test_canPartition_returns_true_for_single_element_input(self):
        sol = Solution()
        assert sol.canPartition([5]) == False
        assert sol.canPartition([6]) == False
        
    def test_canPartition_returns_false_for_odd_sum_input(self):
        sol = Solution()
        assert sol.canPartition([1,2,3,4,5,6,7]) == False
        
    def test_canPartition_returns_true_for_large_input(self):
        sol = Solution()
        nums = [i+1 for i in range(50)]
        assert sol.canPartition(nums) == True
        
pytest.main()