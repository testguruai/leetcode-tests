import pytest

# create test data
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TestBinaryTreePaths:

    def test_empty_tree(self):
        root = None
        solution = Solution()
        assert solution.binaryTreePaths(root) == []

    def test_single_node_tree(self):
        root = TreeNode(1)
        solution = Solution()
        assert solution.binaryTreePaths(root) == ['1']

    def test_multiple_nodes_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(5)
        root.right = TreeNode(3)

        solution = Solution()
        assert solution.binaryTreePaths(root) == ['1->2->5', '1->3']