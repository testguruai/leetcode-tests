import pytest

from solution import TreeNode
from solution import Solution


def test_lowestCommonAncestor():
    sol = Solution()

    # Test Case 1
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    p = root.left.left
    q = root.left.right
    assert sol.lowestCommonAncestor(root, p, q) == root.left

    # Test Case 2
    #       3
    #      / \
    #     5   1
    #    / \   \
    #   6   2   8
    #      / \
    #     7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    p = root.left
    q = root.right
    assert sol.lowestCommonAncestor(root, p, q) == root

    # Test Case 3
    #      1
    #     / \
    #    2   3
    #   / \   
    #  4   5   
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    p = root.right
    q = root.left.right
    assert sol.lowestCommonAncestor(root, p, q) == root

    # Test Case 4
    #     1
    #      \
    #       2
    #        \
    #         3
    #          \
    #           4
    #            \
    #             5
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    root.right.right.right.right = TreeNode(5)
    p = root.right.right
    q = root.right.right.right.right
    assert sol.lowestCommonAncestor(root, p, q) == p


if __name__ == '__main__':
    pytest.main(["-v", "--tb=line", "-rN", "test_solution.py"])
