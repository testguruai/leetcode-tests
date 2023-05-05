
import pytest
from solution import Solution

class TestSolution:
    def test_convertToTitle_case1(self):
        sol = Solution()
        assert sol.convertToTitle(1) == "A"
        
    def test_convertToTitle_case2(self):
        sol = Solution()
        assert sol.convertToTitle(28) == "AB"
        
    def test_convertToTitle_case3(self):
        sol = Solution()
        assert sol.convertToTitle(701) == "ZY"
        
    def test_convertToTitle_case4(self):
        sol = Solution()
        assert sol.convertToTitle(52) == "AZ"
        
    def test_convertToTitle_case5(self):
        sol = Solution()
        assert sol.convertToTitle(26) == "Z"
