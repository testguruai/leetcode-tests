import pytest

from solution import TreeNode, Solution

def test_rob_helper_empty():
    # Test with empty tree
    root = None
    solution = Solution()
    assert solution.rob_helper(root) == [0, 0]

def test_rob_helper():
    # Test with a sample tree
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    solution = Solution()
    assert solution.rob_helper(root) == [7, 4]

def test_rob_empty():
    # Test with empty tree
    root = None
    solution = Solution()
    assert solution.rob(root) == 0

def test_rob():
    # Test with a sample tree
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    solution = Solution()
    assert solution.rob(root) == 7