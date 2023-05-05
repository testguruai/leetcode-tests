import pytest
from solution import TreeNode
from solution import Solution

def test_pathSum_empty():
    # Test empty tree
    s = Solution()
    tree = None
    expected_results = []
    assert s.pathSum(tree, 0) == expected_results

def test_pathSum_one_node():
    # Test tree with only one node
    s = Solution()
    tree = TreeNode(5)
    expected_results = [[tree.val]] if tree.val == 5 else []
    assert s.pathSum(tree, 5) == expected_results
    assert s.pathSum(tree, 10) == []

def test_pathSum_positive_num():
    # Test tree with positive numbers
    s = Solution()

    # Test tree:
    #         5
    #       /   \
    #      4     8
    #     / \   / \
    #    11  2 13  4
    #   /   / \     \
    #  7   5   1     1

    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(7)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(1)
    tree.left.right.left = TreeNode(5)
    tree.left.right.right = TreeNode(1)

    expected_results = [[5, 4, 11, 7], [5, 8, 13], [5, 8, 4, 1]] 
    assert s.pathSum(tree, 22) == expected_results

def test_pathSum_negative_num():
    # Test tree with negative numbers

    s = Solution()

    # Test tree:
    #         -5
    #       /   \
    #      4     8
    #     / \   / \
    #   -11 -2 13  -4
    #   /   / \     \
    #  7   -5 -1     1

    tree = TreeNode(-5)
    tree.left = TreeNode(4)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(-11)
    tree.left.left.left = TreeNode(7)
    tree.left.right = TreeNode(-2)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(-4)
    tree.right.right.right = TreeNode(1)
    tree.left.right.left = TreeNode(-5)
    tree.left.right.right = TreeNode(-1)

    expected_results = [[-5, 4, -11, 7], [-5, 4, -2, -1]] 
    assert s.pathSum(tree, -5) == expected_results

def test_pathSum_mixed():
    # Test tree with mixed numbers

    s = Solution()

    # Test tree:
    #         5
    #       /   \
    #    -10     8
    #     / \   / \
    #    11  2  13 4
    #   /   / \    \
    # -10   5   1   10

    tree = TreeNode(5)
    tree.left = TreeNode(-10)
    tree.right = TreeNode(8)
    tree.left.left = TreeNode(11)
    tree.left.left.left = TreeNode(-10)
    tree.left.right = TreeNode(2)
    tree.right.left = TreeNode(13)
    tree.right.right = TreeNode(4)
    tree.right.right.right = TreeNode(10)
    tree.left.right.left = TreeNode(5)
    tree.left.right.right = TreeNode(1)

    expected_results = [[5, -10, 11, -10, 5], [5, 8, 13, 4], [5, -10, 2, 5, 1]] 
    assert s.pathSum(tree, 1) == expected_results

def test_pathSum_zero():
    # Test tree with zeros

    s = Solution()

    # Test tree:
    #         1
    #       /   \
    #      0     0
    #     / \   / \
    #    0   0 0   0
    tree = TreeNode(1)
    tree.left = TreeNode(0)
    tree.right = TreeNode(0)
    tree.left.left = TreeNode(0)
    tree.left.right = TreeNode(0)
    tree.right.left = TreeNode(0)
    tree.right.right = TreeNode(0)

    expected_results = [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0, 0, 0]]
    assert s.pathSum(tree, 1) == expected_results

def test_pathSum_not_exist_sum():
    # Test with sum that does not exist on the tree

    s = Solution()

    # Test tree:
    #         1
    #       /   \
    #      2    -3
    #     / \   / \
    #    4   5 -6  -7
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(-3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(-6)
    tree.right.right = TreeNode(-7)

    expected_results = []
    assert s.pathSum(tree, 100) == expected_results
