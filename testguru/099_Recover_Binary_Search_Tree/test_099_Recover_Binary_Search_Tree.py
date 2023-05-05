import pytest
from solution import TreeNode
from solution import Solution

def test_recoverTree():
    # Test case 1
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)
    sol.recoverTree(root)
    assert root.val == 3
    assert root.left.val == 1
    assert root.left.right.val == 2
    
    # Test case 2
    sol = Solution()
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    sol.recoverTree(root)
    assert root.val == 4
    assert root.left.val == 2
    assert root.right.val == 3
    assert root.right.left.val == 1

    # Test case 3
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(1)
    sol.recoverTree(root)
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 3

    # Test case 4
    sol = Solution()
    root = TreeNode(2)
    root.left = TreeNode(4)
    root.right = TreeNode(1)
    root.right.left = TreeNode(3)
    sol.recoverTree(root)
    assert root.val == 2
    assert root.left.val == 1
    assert root.right.val == 4
    assert root.right.left.val == 3
