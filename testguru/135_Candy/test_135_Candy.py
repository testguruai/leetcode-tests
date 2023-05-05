import pytest
from solution import Solution

def test_candy_with_empty_list():   
    s = Solution()
    assert s.candy([]) == 0

def test_candy_with_single_element():  
    s = Solution()
    assert s.candy([2]) == 1

def test_candy_with_two_elements():   
    s = Solution()
    assert s.candy([2,3]) == 2

def test_candy_with_three_elements():
    s = Solution()
    assert s.candy([1,2,2]) == 4

def test_candy_with_multiple_elements():
    s = Solution()
    assert s.candy([1,0,2]) == 5
    assert s.candy([1,2,2,3,2,1]) == 11