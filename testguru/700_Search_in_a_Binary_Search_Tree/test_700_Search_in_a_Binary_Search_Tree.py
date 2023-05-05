import pytest
from solution import Solution, TreeNode

@pytest.fixture
def tree():
    """
    Create a binary search tree for testing purposes
                4
               / \
              2   7
             / \
            1   3
    """
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root

def test_searchBST_recursive(tree):
    s = Solution()
    assert s.searchBST(tree, 2) == tree.left
    assert s.searchBST(tree, 5) is None
    
def test_searchBST_iterative(tree):
    s = Solution()
    assert s.searchBST(tree, 2) == tree.left
    assert s.searchBST(tree, 5) is None

def test_searchBST_empty():
    s = Solution()
    assert s.searchBST(None, 3) is None