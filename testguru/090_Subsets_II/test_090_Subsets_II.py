import pytest
from solution import Solution

class TestSolution:
    def test_subsetsWithDup(self):
        s = Solution()
        assert s.subsetsWithDup([1,2,2]) == [[],[1],[2],[1,2],[2,2],[1,2,2]]
        assert s.subsetsWithDup([4,4,4,1,4]) == [[],[1],[4],[1,4],[4,4],[1,4,4],[4,4,4],[1,4,4,4],[4,4,4,4]]
        assert s.subsetsWithDup([2,2,3,3]) == [[],[2],[3],[2,2],[2,3],[2,2,3],[3,3],[2,3,3],[2,2,3,3]]
        assert s.subsetsWithDup([]) == [[]]
        assert s.subsetsWithDup([1]) == [[],[1]]