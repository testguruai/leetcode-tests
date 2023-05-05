import pytest
from solution import TreeNode
from solution import Solution

def test_preorderTraversal():
    """
    Test case 1:
    root: None
    expected result: []
    """
    root = None
    solution = Solution()
    assert solution.preorderTraversal(root) == []

    """
    Test case 2:
    root: 1
          / \
         2   3
    expected result: [1, 2, 3]
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    solution = Solution()
    assert solution.preorderTraversal(root) == [1, 2, 3]

    """
    Test case 3:
    root: 1
          / \
         2   3
        / \
       4   5
    expected result: [1, 2, 4, 5, 3]
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    solution = Solution()
    assert solution.preorderTraversal(root) == [1, 2, 4, 5, 3]
