import pytest

class TestSolution(object):
    def test_mergeTrees_empty(self):
        s = Solution()
        res = s.mergeTrees(None, None)
        assert res is None

    def test_mergeTrees_oneTree(self):
        s = Solution()
        t1 = TreeNode(1)
        res = s.mergeTrees(t1, None)
        assert res.val == 1
        assert res.left is None
        assert res.right is None

    def test_mergeTrees_twoTrees(self):
        s = Solution()
        t1 = TreeNode(1)
        t1.left = TreeNode(3)
        t1.right = TreeNode(2)
        t2 = TreeNode(5)
        t2.left = TreeNode(6)
        t2.right = TreeNode(4)
        res = s.mergeTrees(t1, t2)
        assert res.val == 6
        assert res.left.val == 9
        assert res.right.val == 6
        assert res.right.right.val == 4

    def test_mergeTrees_differentTreeSizes(self):
        s = Solution()
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t2 = TreeNode(3)
        t2.left = TreeNode(4)
        t2.right = TreeNode(5)
        t2.right.right = TreeNode(6)
        res = s.mergeTrees(t1, t2)
        assert res.val == 4
        assert res.left.val == 6
        assert res.right.val == 5
        assert res.right.left.val == 6
        assert res.right.right.val == 6

    def test_mergeTrees_sameTree(self):
        s = Solution()
        t1 = TreeNode(1)
        t1.left = TreeNode(2)
        t1.right = TreeNode(3)
        res = s.mergeTrees(t1, t1)
        assert res.val == 2
        assert res.left.val == 4
        assert res.right.val == 6
