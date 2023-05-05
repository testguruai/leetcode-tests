import pytest
from collections import OrderedDict
from solution import Solution

def test_containsNearbyAlmostDuplicate():
    s = Solution()

    # Test case 1
    nums = [1,2,3,1]
    k = 3
    t = 0
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == True

    # Test case 2
    nums = [1,0,1,1]
    k = 1
    t = 2
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == True

    # Test case 3
    nums = [1,5,9,1,5,9]
    k = 2
    t = 3
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 4
    nums = [1,2,3,4,5]
    k = 4
    t = 0
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 5
    nums = [-1,-1]
    k = 1
    t = -1
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 6
    nums = []
    k = 2
    t = 3
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 7
    nums = [1,2,3,4,5]
    k = 5
    t = 5
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == True

    # Test case 8
    nums = [1,2,3,4,5]
    k = 0
    t = 5
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 9
    nums = [1,2,3,4,5]
    k = 1
    t = 1
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 10
    nums = [1,2,3,4,5]
    k = 3
    t = 2
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == True

    # Test case 11
    nums = [1,2,3,4,5]
    k = 50
    t = 50
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False

    # Test case 12
    nums = [1,2,3,4,5,6]
    k = 2
    t = 2
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == True

    # Test case 13
    nums = [1,2,3,4,5,6]
    k = 1
    t = 2
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == False
