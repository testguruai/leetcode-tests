import pytest

class TestPathSum:
    def test_empty_tree(self):
        # Tests pathSum() on an empty tree
        s = Solution()
        assert s.pathSum(None, 0) == 0

    def test_single_node_tree(self):
        # Tests pathSum() on a single node tree
        s = Solution()
        root = TreeNode(1)
        assert s.pathSum(root, 1) == 1
        assert s.pathSum(root, 0) == 0

    def test_binary_tree(self):
        # Tests pathSum() on a binary tree
        s = Solution()
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        assert s.pathSum(root, 8) == 3
        assert s.pathSum(root, 1) == 1
        assert s.pathSum(root, 6) == 1
        assert s.pathSum(root, 9) == 2