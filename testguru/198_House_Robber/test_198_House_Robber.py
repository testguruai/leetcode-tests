import pytest

from solution import Solution


def test_rob_with_empty_list():
    assert Solution().rob([]) == 0
    
def test_rob_with_list_of_length_one():
    assert Solution().rob([5]) == 5
    
def test_rob_with_list_of_length_two():
    assert Solution().rob([12, 3]) == 12
    assert Solution().rob([3, 12]) == 12
    
def test_rob_with_list_of_length_greater_than_two():
    assert Solution().rob([1, 2, 3, 1]) == 4
    assert Solution().rob([2, 7, 9, 3, 1]) == 12
    
def test_rob_with_negative_numbers():
    assert Solution().rob([-1, -2, -3, -4, -5]) == 0
    assert Solution().rob([-5, -4, -3, -2, -1]) == -2