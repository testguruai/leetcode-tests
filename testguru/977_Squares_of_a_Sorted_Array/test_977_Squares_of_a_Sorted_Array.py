import pytest

class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_sortedSquares(self):
        assert self.sol.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
        assert self.sol.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
        assert self.sol.sortedSquares([-8,-4,-3,0,2,5]) == [0,4,9,16,25,64] 
        assert self.sol.sortedSquares([1,2,3,4,5]) == [1,4,9,16,25]
        assert self.sol.sortedSquares([-5,-4,-3,-2,-1]) == [1,4,9,16,25]