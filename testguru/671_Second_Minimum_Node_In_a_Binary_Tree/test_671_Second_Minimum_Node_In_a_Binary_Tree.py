import pytest

from solution import Solution


class TestSolution:
    def test_valid_input(self):
        solution = Solution()

        # Test case 1
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        assert solution.findSecondMinimumValue(root) == 5

        # Test case 2
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        assert solution.findSecondMinimumValue(root) == -1

        # Test case 3
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        assert solution.findSecondMinimumValue(root) == 3

    def test_invalid_input(self):
        solution = Solution()

        # Test case with empty tree
        assert solution.findSecondMinimumValue(None) == -1

        # Test case where tree has only one node
        class TreeNode:
            def __init__(self, x):
                self.val = x
                self.left = None
                self.right = None
        root = TreeNode(2)
        assert solution.findSecondMinimumValue(root) == -1