import pytest

from solution import Solution
from solution import TreeNode

def test_isSameTree():
    s = Solution()

    # Test empty trees
    assert s.isSameTree(None, None) == True

    # Test trees with a single node
    p = TreeNode(1)
    q = TreeNode(1)
    assert s.isSameTree(p, q) == True

    # Test trees with different values
    p = TreeNode(1)
    q = TreeNode(2)
    assert s.isSameTree(p, q) == False

    # Test trees with different structures
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.left.left = TreeNode(3)
    q.right = TreeNode(4)
    assert s.isSameTree(p, q) == False

    # Test trees with the same structure and values
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    assert s.isSameTree(p, q) == True
