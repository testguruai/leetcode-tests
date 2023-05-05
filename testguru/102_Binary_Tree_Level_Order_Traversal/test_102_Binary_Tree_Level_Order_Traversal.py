import pytest

from solution import Solution, TreeNode


@pytest.fixture
def solution():
    return Solution()


def test_level_order_with_no_root(solution):
    assert solution.levelOrder(None) == []


def test_level_order_with_single_node(solution):
    root = TreeNode(1)
    assert solution.levelOrder(root) == [[1]]


def test_level_order_with_three_levels(solution):
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]


def test_level_order_with_unbalanced_tree(solution):
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    assert solution.levelOrder(root) == [[1], [2], [4]]
