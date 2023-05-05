import pytest

from solution import Solution

def test_minOperationsMaxProfit1():
    s = Solution()
    assert s.minOperationsMaxProfit([10,10,6,4,7], 3, 8) == 9

def test_minOperationsMaxProfit2():
    s = Solution()
    assert s.minOperationsMaxProfit([10,10,6,4,7], 4, 4) == 5

def test_minOperationsMaxProfit3():
    s = Solution()
    assert s.minOperationsMaxProfit([10,10,6,4,7], 43, 54) == 993

def test_minOperationsMaxProfit4():
    s = Solution()
    assert s.minOperationsMaxProfit([10,10,6,4,7], 92, 92) == 243550

def test_minOperationsMaxProfit5():
    s = Solution()
    assert s.minOperationsMaxProfit([], 3, 8) == -1