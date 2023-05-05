import pytest
from .solution_file import Solution, TreeNode

class TestSolution:
    def test_invertTree_recursive(self):
        s = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        expectedRoot = TreeNode(4)
        expectedRoot.left = TreeNode(7)
        expectedRoot.right = TreeNode(2)
        expectedRoot.left.left = TreeNode(9)
        expectedRoot.left.right = TreeNode(6)
        expectedRoot.right.left = TreeNode(3)
        expectedRoot.right.right = TreeNode(1)

        assert s.invertTree(root) == expectedRoot

    def test_invertTree_iterative(self):
        s = Solution()
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(9)

        expectedRoot = TreeNode(4)
        expectedRoot.left = TreeNode(7)
        expectedRoot.right = TreeNode(2)
        expectedRoot.left.left = TreeNode(9)
        expectedRoot.left.right = TreeNode(6)
        expectedRoot.right.left = TreeNode(3)
        expectedRoot.right.right = TreeNode(1)

        assert s.invertTree(root) == expectedRoot