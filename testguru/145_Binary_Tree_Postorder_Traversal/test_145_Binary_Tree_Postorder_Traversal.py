import pytest


class TestSolution:
    def test_empty_tree(self):
        s = Solution()
        assert s.postorderTraversal(None) == []

    def test_single_node_tree(self):
        s = Solution()
        root = TreeNode(1)
        assert s.postorderTraversal(root) == [1]

    def test_full_binary_tree(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        assert s.postorderTraversal(root) == [4, 5, 2, 6, 7, 3, 1]

    def test_left_skewed_tree(self):
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        assert s.postorderTraversal(root) == [4, 3, 2, 1]

    def test_right_skewed_tree(self):
        s = Solution()
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        assert s.postorderTraversal(root) == [4, 3, 2, 1]