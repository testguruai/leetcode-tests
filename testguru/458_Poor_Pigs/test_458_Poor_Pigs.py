import pytest
from solution import Solution

def test_poorPigs():
    sol = Solution()

    # Test case with only one bucket
    assert sol.poorPigs(1, 1, 1) == 0
    assert sol.poorPigs(1, 2, 1) == 0
    assert sol.poorPigs(1, 3, 1) == 0

    # Test case with two buckets
    assert sol.poorPigs(2, 1, 1) == 1
    assert sol.poorPigs(2, 1, 3) == 1
    assert sol.poorPigs(2, 2, 3) == 1
    assert sol.poorPigs(2, 3, 3) == 1

    # Test case with three buckets
    assert sol.poorPigs(3, 1, 1) == 1
    assert sol.poorPigs(3, 1, 2) == 2
    assert sol.poorPigs(3, 1, 3) == 2
    assert sol.poorPigs(3, 2, 3) == 1

    # Test case with four buckets
    assert sol.poorPigs(4, 1, 1) == 2
    assert sol.poorPigs(4, 1, 2) == 2
    assert sol.poorPigs(4, 1, 3) == 2
    assert sol.poorPigs(4, 2, 3) == 2
    assert sol.poorPigs(4, 3, 3) == 1 

    # Test case with many buckets
    assert sol.poorPigs(1000, 15, 60) == 5
    assert sol.poorPigs(999, 15, 60) == 5
    assert sol.poorPigs(1000, 10, 60) == 3
    assert sol.poorPigs(999, 10, 60) == 3

test_poorPigs()