import pytest
from solution import Solution, TreeNode

def test_sortedArrayToBST():
    sol = Solution()

    # Test case with empty list
    assert sol.sortedArrayToBST([]) == None

    # Test case with single element
    assert sol.sortedArrayToBST([1]).val == 1

    # Test with two elements
    root = sol.sortedArrayToBST([1,2])
    assert root.val == 2
    assert root.left.val == 1
    assert root.right == None

    # Test with three elements
    root = sol.sortedArrayToBST([1,2,3])
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 3

    # Test case with repeated elements
    root = sol.sortedArrayToBST([2,2,3,7,10])
    assert root.val == 3
    assert root.left.val == 2
    assert root.left.right.val == 2
    assert root.right.val == 10
    assert root.right.left.val == 7

    # Test case with negative elements
    root = sol.sortedArrayToBST([-10,-3,0,5,9])
    assert root.val == 0
    assert root.left.val == -10
    assert root.right.val == 5
    assert root.right.left.val == -3
    assert root.right.right.val == 9