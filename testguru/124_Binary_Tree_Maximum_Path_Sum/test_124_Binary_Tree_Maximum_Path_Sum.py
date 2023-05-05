import pytest

from solution import Solution, TreeNode

@pytest.fixture
def solution():
    return Solution()

@pytest.fixture
def tree():
    t = TreeNode(1)
    t.left = TreeNode(2)
    t.right = TreeNode(3)
    t.left.left = TreeNode(4)
    t.left.right = TreeNode(5)
    t.right.left = TreeNode(6)
    t.right.right = TreeNode(7)
    return t

def test_maxPathSum(solution, tree):
    assert solution.maxPathSum(tree) == 18

def test_maxPathSum_empty_tree(solution):
    assert solution.maxPathSum(None) == 0

def test_getNodeMaxValue_left(solution, tree):
    assert solution.getNodeMaxValue(tree.left) == 5

def test_getNodeMaxValue_right(solution, tree):
    assert solution.getNodeMaxValue(tree.right) == 7

def test_getNodeMaxValue_single_node(solution):
    assert solution.getNodeMaxValue(TreeNode(10)) == 10

def test_getNodeMaxValue_empty_node(solution):
    assert solution.getNodeMaxValue(None) == 0