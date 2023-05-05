import pytest

# First, let's define a sample tree to use for testing
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
root.right.left.right = TreeNode(4)
root.left.left.left.left = TreeNode(5)


# Tests for Solution class
def test_solution_balanced_tree():
    s = Solution()
    assert s.isBalanced(root) == True

def test_solution_unbalanced_tree():
    s = Solution()
    root.left.left.left.left.left = TreeNode(6)
    assert s.isBalanced(root) == False

def test_solution_empty_tree():
    s = Solution()
    assert s.isBalanced(None) == True

def test_solution_single_node_tree():
    s = Solution()
    root = TreeNode(1)
    assert s.isBalanced(root) == True

def test_solution_two_node_tree():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert s.isBalanced(root) == True

def test_solution_two_node_unbalanced_tree():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    assert s.isBalanced(root) == False

# Tests for TreeNode class
def test_TreeNode_creation():
    n = TreeNode(7)
    assert n.val == 7

def test_TreeNode_left_child():
    n = TreeNode(7)
    n.left = TreeNode(8)
    assert n.left.val == 8

def test_TreeNode_right_child():
    n = TreeNode(7)
    n.right = TreeNode(9)
    assert n.right.val == 9