import pytest

from solution import Solution, TreeNode

def test_inorder_traversal_with_empty_tree():
    solution = Solution()
    root = None
    assert solution.inorderTraversal(root) == []

def test_inorder_traversal_with_single_node_tree():
    solution = Solution()
    root = TreeNode(1)
    assert solution.inorderTraversal(root) == [1]

def test_inorder_traversal_with_full_tree():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert solution.inorderTraversal(root) == [4, 2, 5, 1, 6, 3, 7]

def test_inorder_traversal_with_unbalanced_tree():
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    assert solution.inorderTraversal(root) == [1, 3, 2]

def test_inorder_traversal_with_single_left_tree():
    solution = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert solution.inorderTraversal(root) == [4, 3, 2, 1]

def test_inorder_traversal_with_single_right_tree():
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    assert solution.inorderTraversal(root) == [1, 2, 3, 4]