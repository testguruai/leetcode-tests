import pytest

from solution import Solution, TreeNode


class TestSolution:
    def test_min_depth_recursion(self):
        # Test case 1
        root = TreeNode(3)
        node_9 = TreeNode(9)
        node_20 = TreeNode(20)
        node_15 = TreeNode(15)
        node_7 = TreeNode(7)
        root.left = node_9
        root.right = node_20
        node_20.left = node_15
        node_20.right = node_7

        assert Solution().minDepth(root) == 2

        # Test case 2
        left = TreeNode(2)
        right = TreeNode(3)
        root = TreeNode(1)
        root.left = left
        left.left = right

        assert Solution().minDepth(root) == 3

    def test_min_depth_bfs(self):
        # Test case 1
        root = TreeNode(3)
        node_9 = TreeNode(9)
        node_20 = TreeNode(20)
        node_15 = TreeNode(15)
        node_7 = TreeNode(7)
        root.left = node_9
        root.right = node_20
        node_20.left = node_15
        node_20.right = node_7

        assert Solution().minDepth(root) == 2

        # Test case 2
        left = TreeNode(2)
        right = TreeNode(3)
        root = TreeNode(1)
        root.left = left
        left.left = right

        assert Solution().minDepth(root) == 3