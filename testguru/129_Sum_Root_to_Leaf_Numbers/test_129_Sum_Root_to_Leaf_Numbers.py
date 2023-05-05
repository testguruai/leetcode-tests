import pytest

from solution import TreeNode
from solution import Solution

def test_sumNumbers():
    s = Solution()
    
    # Test case 1
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    assert s.sumNumbers(root) == 25
    
    # Test case 2
    root = TreeNode(4)
    root.left = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    root.right = TreeNode(0)
    
    assert s.sumNumbers(root) == 1026
    
    # Test case 3
    root = None
    
    assert s.sumNumbers(root) == 0
    
    # Test case 4
    root = TreeNode(1)
    
    assert s.sumNumbers(root) == 1
    
    # Test case 5
    root = TreeNode(9)
    root.left = TreeNode(8)
    root.right = TreeNode(7)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    
    assert s.sumNumbers(root) == 1846
