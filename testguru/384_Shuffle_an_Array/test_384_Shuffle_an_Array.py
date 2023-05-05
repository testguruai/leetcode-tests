import pytest
from collections import Counter

@pytest.fixture
def nums():
    return [1, 2, 3, 4]

def test_reset(nums):
    s = Solution(nums)
    assert s.reset() == nums

def test_shuffle(nums):
    s = Solution(nums)
    shuffled_nums = s.shuffle()
    assert Counter(shuffled_nums) == Counter(nums)
    assert shuffled_nums != nums  # Assert that the shuffled list is not the same as the original list
