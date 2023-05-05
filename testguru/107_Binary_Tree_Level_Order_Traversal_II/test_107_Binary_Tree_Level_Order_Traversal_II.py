import pytest
from solution import TreeNode
from solution import Solution

def test_level_order_bottom_empty_tree():
    root = None
    assert Solution().levelOrderBottom(root) == []

def test_level_order_bottom_single_node_tree():
    root = TreeNode(1)
    assert Solution().levelOrderBottom(root) == [[1]]

def test_level_order_bottom_full_binary_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().levelOrderBottom(root) == [[15,7],[9,20],[3]] 

def test_level_order_bottom_unbalanced_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    root.right.left.right = TreeNode(10)
    assert Solution().levelOrderBottom(root) == [[10,7],[15],[9,20],[3]] 

def test_level_order_bottom_skewed_tree():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert Solution().levelOrderBottom(root) == [[3],[2],[1]]
