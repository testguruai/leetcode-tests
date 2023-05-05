import pytest

from solution import Solution
from solution import TreeLinkNode

def test_case1():
    # Test case with a single node
    root = TreeLinkNode(1)
    solution = Solution()
    solution.connect(root)
    assert root.next == None

def test_case2():
    # Test case with three nodes in a straight line
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    solution = Solution()
    solution.connect(root)
    assert root.next == None
    assert root.left.next == root.right
    assert root.right.next == None

def test_case3():
    # Test case with three nodes in a triangle
    root = TreeLinkNode(1)
    root.left = TreeLinkNode(2)
    root.right = TreeLinkNode(3)
    root.left.left = TreeLinkNode(4)
    root.left.right = TreeLinkNode(5)
    root.right.left = TreeLinkNode(6)
    root.right.right = TreeLinkNode(7)
    solution = Solution()
    solution.connect(root)
    assert root.next == None
    assert root.left.next == root.right
    assert root.right.next == None
    assert root.left.left.next == root.left.right
    assert root.left.right.next == root.right.left
    assert root.right.left.next == root.right.right
    assert root.right.right.next == None
