import pytest

from solution import TreeNode, Solution


class TestSolution(object):
    def test_flatten(self):
        # test case 1: root is None
        s = Solution()
        s.flatten(None)
        assert True

        # test case 2: root has only one child (left)
        root = TreeNode(1)
        root.left = TreeNode(2)
        s = Solution()
        s.flatten(root)
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2

        # test case 3: root has only one child (right)
        root = TreeNode(1)
        root.right = TreeNode(2)
        s = Solution()
        s.flatten(root)
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2

        # test case 4: root has both children
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        s = Solution()
        s.flatten(root)
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert root.right.left is None
        assert root.right.right.val == 3

        # test case 5: root has multiple layers of children
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)
        s = Solution()
        s.flatten(root)
        assert root.val == 1
        assert root.left is None
        assert root.right.val == 2
        assert root.right.left is None
        assert root.right.right.val == 3
        assert root.right.right.left is None
        assert root.right.right.right.val == 4
        assert root.right.right.right.left is None
        assert root.right.right.right.right.val == 5
        assert root.right.right.right.right.left is None
        assert root.right.right.right.right.right.val == 6