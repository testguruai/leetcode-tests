import pytest

from solution import Solution, TreeNode


def test_closest_value_brute_force():
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    assert s.closestValue(root, 3.7142) == 4


def test_closest_value_iterative():
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    assert s.closestValue(root, 3.7142) == 4


def test_closest_value_recursive():
    s = Solution()
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    assert s.closestValue(root, 3.7142) == 4
