import pytest

# Example tree for testing
#     3
#   /   \
#  9     20
#       /  \
#     15    7
@pytest.fixture
def test_tree():
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def test_sumOfLeftLeaves_empty():
    s = Solution()
    assert s.sumOfLeftLeaves(None) == 0

def test_sumOfLeftLeaves_single_node():
    s = Solution()
    root = TreeNode(5)
    assert s.sumOfLeftLeaves(root) == 0

def test_sumOfLeftLeaves_only_right_nodes(test_tree):
    s = Solution()
    root = test_tree
    root.left = None
    assert s.sumOfLeftLeaves(root) == 0

def test_sumOfLeftLeaves_only_left_nodes(test_tree):
    s = Solution()
    root = test_tree
    root.right = None
    assert s.sumOfLeftLeaves(root) == 9

def test_sumOfLeftLeaves_both_sides(test_tree):
    s = Solution()
    root = test_tree
    assert s.sumOfLeftLeaves(root) == 24