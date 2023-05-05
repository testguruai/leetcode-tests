import pytest

class TestSolution:
    
    def test_empty_prices(self):
        sol = Solution()
        assert sol.maxProfit([]) == 0
    
    def test_single_price(self):
        sol = Solution()
        assert sol.maxProfit([1]) == 0
    
    def test_increasing_prices(self):
        sol = Solution()
        assert sol.maxProfit([1, 2, 3, 4, 5]) == 4
    
    def test_decreasing_prices(self):
        sol = Solution()
        assert sol.maxProfit([5, 4, 3, 2, 1]) == 0
    
    def test_alternating_prices_1(self):
        sol = Solution()
        assert sol.maxProfit([1, 2, 1, 2, 1, 2]) == 2
    
    def test_alternating_prices_2(self):
        sol = Solution()
        assert sol.maxProfit([2, 1, 2, 1, 2, 1]) == 1
    
    def test_random_prices_1(self):
        sol = Solution()
        assert sol.maxProfit([10, 1, 5, 3, 8, 9]) == 15
    
    def test_random_prices_2(self):
        sol = Solution()
        assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

    def test_random_prices_3(self):
        sol = Solution()
        assert sol.maxProfit([13, 14, 15, 12, 16, 20, 18, 17, 23, 21, 19]) == 16