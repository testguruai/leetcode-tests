import pytest

class TestSolution:
    def test_combinationSum(self):
        s = Solution()
        assert s.combinationSum([8,7,4,3], 11) == [[3, 4, 4], [3, 8], [4, 7]]
        assert s.combinationSum([1], 1) == [[1]]
        assert s.combinationSum([2,3,6,7], 7) == [[2, 2, 3], [7]]
        assert s.combinationSum([2,3,5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]