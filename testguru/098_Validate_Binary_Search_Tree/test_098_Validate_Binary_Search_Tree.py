import sys
import pytest

from solution import TreeNode
from solution import Solution

# Test case for isValidBST() method
def test_isValidBST():
    # Sample tree 1
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(3)

    # Sample tree 2
    root2 = TreeNode(5)
    root2.left = TreeNode(1)
    root2.right = TreeNode(4)
    root2.right.left = TreeNode(3)
    root2.right.right = TreeNode(6)

    # Sample tree 3
    root3 = TreeNode(10)
    root3.left = TreeNode(5)
    root3.right = TreeNode(15)
    root3.right.left = TreeNode(6)
    root3.right.right = TreeNode(20)

    assert Solution().isValidBST(root1) == True
    assert Solution().isValidBST(root2) == False
    assert Solution().isValidBST(root3) == False

# Test case for isVaild_helper() method
def test_isVaild_helper():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(8)

    assert Solution().isVaild_helper(root, -sys.maxint-1, sys.maxint) == True
    assert Solution().isVaild_helper(root.left, -sys.maxint-1, root.val) == True
    assert Solution().isVaild_helper(root.left.right, root.left.val, root.val) == True
    assert Solution().isVaild_helper(root.right, root.val, sys.maxint) == True
    assert Solution().isVaild_helper(root.right.right, root.val, sys.maxint) == True
    assert Solution().isVaild_helper(root.left.left, -sys.maxint-1, root.left.val) == True
    assert Solution().isVaild_helper(root.right.left, root.val, sys.maxint) == False
