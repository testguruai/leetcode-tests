
# test_solution.py

from solution import Solution

def test_maxProfit_emptyList():
    sol = Solution()
    assert sol.maxProfit([]) == 0

def test_maxProfit_oneElement():
    sol = Solution()
    assert sol.maxProfit([5]) == 0

def test_maxProfit_increasingPrices():
    sol = Solution()
    assert sol.maxProfit([1, 2, 3, 4, 5]) == 4

def test_maxProfit_decreasingPrices():
    sol = Solution()
    assert sol.maxProfit([5, 4, 3, 2, 1]) == 0

def test_maxProfit_mixedPrices():
    sol = Solution()
    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5

def test_maxProfit_duplicatePrices():
    sol = Solution()
    assert sol.maxProfit([2, 2, 2, 2, 2]) == 0

def test_maxProfit_largeInput():
    sol = Solution()
    prices = [i * 10 for i in range(10000)]
    assert sol.maxProfit(prices) == 99000

pytest test_solution.py
