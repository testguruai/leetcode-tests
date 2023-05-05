import pytest
from solution import TreeNode
from solution import Solution

def test_diameter_empty_tree():
    s = Solution()
    assert s.diameterOfBinaryTree(None) == 0

def test_diameter_single_node_tree():
    s = Solution()
    root = TreeNode(5)
    assert s.diameterOfBinaryTree(root) == 0

def test_diameter_two_node_tree():
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    assert s.diameterOfBinaryTree(root) == 1

def test_diameter_three_node_tree():
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    assert s.diameterOfBinaryTree(root) == 2

def test_diameter_four_node_tree():
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    assert s.diameterOfBinaryTree(root) == 3

def test_diameter_five_node_tree():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert s.diameterOfBinaryTree(root) == 3

def test_diameter_large_tree():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.right.left.right = TreeNode(11)
    root.left.right.left.left = TreeNode(12)
    assert s.diameterOfBinaryTree(root) == 6
