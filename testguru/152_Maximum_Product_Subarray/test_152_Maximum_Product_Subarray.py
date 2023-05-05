import pytest
from solution import Solution

def test_maxProduct_exists():
    sol = Solution()
    assert sol.maxProduct

def test_maxProduct_with_null():
    sol = Solution()
    assert sol.maxProduct(None) == 0

def test_maxProduct_with_empty_list():
    sol = Solution()
    assert sol.maxProduct([]) == 0

def test_maxProduct_with_negative_num():
    sol = Solution()
    assert sol.maxProduct([-2,-3,-1,-4,-5]) == 60

def test_maxProduct_with_positive_num():
    sol = Solution()
    assert sol.maxProduct([1,2,3,4,5]) == 120

def test_maxProduct_with_only_one_num():
    sol = Solution()
    assert sol.maxProduct([5]) == 5

def test_maxProduct_with_mixed_num():
    sol = Solution()
    assert sol.maxProduct([1,2,-3,4,-5]) == 60