import pytest
from solution import Solution

class TestSolution:
    def test_empty_input(self):
        sol = Solution()
        assert sol.generateTrees(0) == []

    def test_single_node(self):
        sol = Solution()
        expected_tree = TreeNode(1)
        assert sol.generateTrees(1) == [expected_tree]

    def test_multiple_nodes(self):
        sol = Solution()
        expected_tree_1 = TreeNode(1)
        expected_tree_1.right = TreeNode(2)
        expected_tree_2 = TreeNode(2)
        expected_tree_2.left = TreeNode(1)
        assert sol.generateTrees(2) == [expected_tree_1, expected_tree_2]
