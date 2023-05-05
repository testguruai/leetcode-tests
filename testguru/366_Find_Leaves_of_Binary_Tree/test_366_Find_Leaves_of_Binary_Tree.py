import pytest
from solution import Solution

class TestSolution:
    def test_findLeaves_emptyTree(self):
        sol = Solution()
        result = sol.findLeaves(None)
        assert result == []

    def test_findLeaves_singleNode(self):
        sol = Solution()
        root = TreeNode(1)
        result = sol.findLeaves(root)
        assert result == [[1]]

    def test_findLeaves_leftChildOnly(self):
        sol = Solution()
        root = TreeNode(1)
        left = TreeNode(2)
        root.left = left
        result = sol.findLeaves(root)
        assert result == [[2], [1]]

    def test_findLeaves_rightChildOnly(self):
        sol = Solution()
        root = TreeNode(1)
        right = TreeNode(2)
        root.right = right
        result = sol.findLeaves(root)
        assert result == [[2], [1]]

    def test_findLeaves_completeTree(self):
        sol = Solution()
        root = TreeNode(1)
        left = TreeNode(2)
        right = TreeNode(3)
        root.left = left
        root.right = right
        left_left = TreeNode(4)
        left.right = left_left
        left_left_left = TreeNode(7)
        left_left.right = left_left_left
        right_left = TreeNode(5)
        right_right = TreeNode(6)
        right.left = right_left
        right.right = right_right
        result = sol.findLeaves(root)
        assert result == [[7, 5, 6], [4], [2], [3], [1]]