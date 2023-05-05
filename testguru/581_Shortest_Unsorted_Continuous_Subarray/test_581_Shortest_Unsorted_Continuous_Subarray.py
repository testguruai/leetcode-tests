import pytest

from solution import Solution

def test_findUnsortedSubarray():
    sol = Solution()

    # Test case 1
    nums = [2, 6, 4, 8, 10, 9, 15]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 2
    nums = [1, 2, 3, 4]
    assert sol.findUnsortedSubarray(nums) == 0

    # Test case 3
    nums = [1]
    assert sol.findUnsortedSubarray(nums) == 0

    # Test case 4
    nums = [1, 3, 2, 4, 5, 6, 7, 9, 8]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 5
    nums = [2, 1]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 6
    nums = [1, 2, 3, 5, 4]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 7
    nums = [1, 2, 3, 4, 6, 5, 7, 8]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 8
    nums = [1, 3, 2, 4, 5, 6, 7, 8, 10, 9, 11]
    assert sol.findUnsortedSubarray(nums) == 8

    # Test case 9
    nums = []
    assert sol.findUnsortedSubarray(nums) == 0

    # Test case 10
    nums = [1, 2, 3, 3, 3]
    assert sol.findUnsortedSubarray(nums) == 0

    # Test case 11
    nums = [3, 2, 3, 2, 4]
    assert sol.findUnsortedSubarray(nums) == 4

    # Test case 12
    nums = [1, 2, 4, 5, 3]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 13
    nums = [2, 4, 6, 5, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 14
    nums = [2, 3, 5, 4]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 15
    nums = [3, 2, 1]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 16
    nums = [3, 2, 1, 4, 5]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 17
    nums = [2, 5, 3, 6, 9, 12, 4, 7, 8, 10]
    assert sol.findUnsortedSubarray(nums) == 8

    # Test case 18
    nums = [1, 2, 3, 6, 4, 5, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 19
    nums = [1, 2, 3, 4, 5, 8, 6, 7, 9, 10]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 20
    nums = [1, 2, 3, 5, 4, 6, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 21
    nums = [1, 2, 3, 4, 6, 5, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 22
    nums = [2, 3, 4, 5, 1]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 23
    nums = [3, 2, 4, 5, 6, 1]
    assert sol.findUnsortedSubarray(nums) == 6

    # Test case 24
    nums = [1, 2, 3, 4, 5]
    assert sol.findUnsortedSubarray(nums) == 0

    # Test case 25
    nums = [2, 3, 4, 5, 6, 1]
    assert sol.findUnsortedSubarray(nums) == 6

    # Test case 26
    nums = [5, 4, 3, 2, 1]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 27
    nums = [3, 1, 2, 4]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 28
    nums = [1, 2, 3, 4, 4, 0]
    assert sol.findUnsortedSubarray(nums) == 2

    # Test case 29
    nums = [1, 2, 3, 4, 0, 5]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 30
    nums = [1, 3, 2, 4, 5, 6, 7, 8, 10, 9]
    assert sol.findUnsortedSubarray(nums) == 8

    # Test case 31
    nums = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    assert sol.findUnsortedSubarray(nums) == 9

    # Test case 32
    nums = [1, 2, 3, 4, 5, 5, 5, 5]
    assert sol.findUnsortedSubarray(nums) == 0

    # Test case 33
    nums = [1, 2, 3, 4, 5, 9, 8, 7, 6]
    assert sol.findUnsortedSubarray(nums) == 9

    # Test case 34
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9]
    assert sol.findUnsortedSubarray(nums) == 9

    # Test case 35
    nums = [1, 2, 3, 4, 5, 6, 0, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 7

    # Test case 36
    nums = [3, 4, 6, 5, 7, 9, 11, 10]
    assert sol.findUnsortedSubarray(nums) == 4

    # Test case 37
    nums = [1, 3, 2, 2, 2, 4, 5, 6, 7, 9, 8]
    assert sol.findUnsortedSubarray(nums) == 7

    # Test case 38
    nums = [2, 3, 1, 5, 4, 6, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 39
    nums = [2, 3, 1, 0, 5, 4, 6, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 8

    # Test case 40
    nums = [1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 41
    nums = [2, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 42
    nums = [1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 43
    nums = [1, 3, 0, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 44
    nums = [1, 2, 5, 3, 4, 6, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 45
    nums = [5, 4, 3, 2, 1, 0]
    assert sol.findUnsortedSubarray(nums) == 6

    # Test case 46
    nums = [1, 2, 3, 4, 0, -1, -2, -3, -4, -5]
    assert sol.findUnsortedSubarray(nums) == 10

    # Test case 47
    nums = [1, 2, 3, 4, -5]
    assert sol.findUnsortedSubarray(nums) == 5

    # Test case 48
    nums = [1, 3, 5, 2, 4, 6, 7, 8, 9]
    assert sol.findUnsortedSubarray(nums) == 3

    # Test case 49
    nums = [4, 3, 2, 1]
    assert sol.findUnsortedSubarray(nums) == 4

    # Test case 50
    nums = [4, 3, 2, 1, 0]
    assert sol.findUnsortedSubarray(nums) == 5

test_findUnsortedSubarray()
