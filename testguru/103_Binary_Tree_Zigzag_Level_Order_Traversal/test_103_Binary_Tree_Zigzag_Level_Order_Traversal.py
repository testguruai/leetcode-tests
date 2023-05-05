import pytest

from solution import TreeNode, Solution

def test_zigzagLevelOrder_empty():
    s = Solution()
    assert s.zigzagLevelOrder(None) == []

def test_zigzagLevelOrder_single():
    s = Solution()
    root = TreeNode(1)
    assert s.zigzagLevelOrder(root) == [[1]]

def test_zigzagLevelOrder_multiple_levels():
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert s.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

def test_zigzagLevelOrder_multiple_levels_different_order():
    s = Solution()
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right = TreeNode(8)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(10)
    assert s.zigzagLevelOrder(root) == [[5], [8, 3], [2, 4, 6, 10]]