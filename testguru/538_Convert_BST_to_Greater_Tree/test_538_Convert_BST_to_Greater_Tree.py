import pytest

from solution import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.fixture
def binary_search_tree():
    class BinaryTreeNode():
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    node_4 = BinaryTreeNode(4)
    node_1 = BinaryTreeNode(1)
    node_0 = BinaryTreeNode(0)
    node_2 = BinaryTreeNode(2)
    node_3 = BinaryTreeNode(3)
    node_6 = BinaryTreeNode(6)
    node_5 = BinaryTreeNode(5)
    node_7 = BinaryTreeNode(7)

    node_4.left = node_1
    node_1.left = node_0
    node_1.right = node_2
    node_2.right = node_3
    node_4.right = node_6
    node_6.left = node_5
    node_6.right = node_7

    return node_4


def test_convert_bst_should_return_the_root_with_correct_values(solution, binary_search_tree):
    result_root = solution.convertBST(binary_search_tree)

    assert result_root.val == 22
    assert result_root.left.val == 29
    assert result_root.left.left.val == 29
    assert result_root.left.right.val == 31
    assert result_root.left.right.right.val == 34
    assert result_root.right.val == 7
    assert result_root.right.left.val == 12
    assert result_root.right.right.val == 0


def test_convert_bst_should_return_none_when_given_none_as_root(solution):
    result_root = solution.convertBST(None)

    assert result_root is None