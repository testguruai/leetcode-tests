
import pytest
from solution import Solution

def test_empty_list():
    assert Solution().topKFrequent([], 1) == []

def test_single_element_list():
    assert Solution().topKFrequent([1], 1) == [1]

def test_duplicate_elements():
    assert Solution().topKFrequent([1,1,2,2,2,3], 2) == [2, 1]

def test_k_is_greater_than_number_of_unique_elements():
    assert Solution().topKFrequent([1,2,3], 4) == [1, 2, 3]

def test_k_is_equal_to_number_of_unique_elements():
    assert Solution().topKFrequent([1,1,2,3], 3) == [1, 2, 3]

def test_all_elements_are_the_same():
    assert Solution().topKFrequent([1,1,1,1], 1) == [1]
