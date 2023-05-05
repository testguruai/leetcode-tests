
import pytest
from solution import Solution

class TestSolution:
    def test_combinationSum2_1(self):
        s = Solution()
        candidates = [10, 1, 2, 7, 6, 1, 5]
        target = 8
        output = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
        assert s.combinationSum2(candidates, target) == output
        
    def test_combinationSum2_2(self):
        s = Solution()
        candidates = [2, 5, 2, 1, 2]
        target = 5
        output = [[1, 2, 2], [5]]
        assert s.combinationSum2(candidates, target) == output
        
    def test_combinationSum2_3(self):
        s = Solution()
        candidates = [1, 1, 1]
        target = 3
        output = [[1, 1, 1]]
        assert s.combinationSum2(candidates, target) == output
        
    def test_combinationSum2_4(self):
        s = Solution()
        candidates = [1, 2, 3, 4, 5]
        target = 6
        output = [[1, 2, 3], [1, 5], [2, 4]]
        assert s.combinationSum2(candidates, target) == output

    def test_combinationSum2_5(self):
        s = Solution()
        candidates = [1, 2, 3, 4, 5]
        target = 10
        output = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], 
                  [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], 
                  [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], 
                  [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
        assert s.combinationSum2(candidates, target) == output
