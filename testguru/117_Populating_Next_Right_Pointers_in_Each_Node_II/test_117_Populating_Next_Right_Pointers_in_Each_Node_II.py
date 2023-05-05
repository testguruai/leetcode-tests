import pytest

from solution import Solution, TreeLinkNode


class TestSolution(object):
    def test_nonexistent_root(self):
        solution = Solution()
        assert solution.connect(None) is None

    def test_single_node_tree(self):
        solution = Solution()
        root = TreeLinkNode(10)
        solution.connect(root)
        assert root.next is None
        assert root.left is None
        assert root.right is None

    def test_full_binary_tree(self):
        solution = Solution()
        root = TreeLinkNode(1)
        root.left = TreeLinkNode(2)
        root.right = TreeLinkNode(3)
        root.left.left = TreeLinkNode(4)
        root.left.right = TreeLinkNode(5)
        root.right.left = TreeLinkNode(6)
        root.right.right = TreeLinkNode(7)
        solution.connect(root)
        assert root.next is None
        assert root.left.next == root.right
        assert root.right.next is None
        assert root.left.left.next == root.left.right
        assert root.left.right.next == root.right.left
        assert root.right.left.next == root.right.right
        assert root.right.right.next is None