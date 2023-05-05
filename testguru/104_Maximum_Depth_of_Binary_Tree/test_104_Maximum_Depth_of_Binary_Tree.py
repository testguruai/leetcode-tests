import pytest

from solution import TreeNode, Solution  # Assuming the code is in solution_file.py


@pytest.fixture
def example_binary_tree():
    # Create an example binary tree to test the maxDepth function
    """
            1
           / \
          2   3
         / \   \
        4   5   6
       /
      7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    return root


def test_max_depth_of_empty_tree():
    # Test the maxDepth function on an empty tree
    solution = Solution()
    assert solution.maxDepth(None) == 0


def test_max_depth_of_binary_tree(example_binary_tree):
    # Test the maxDepth function on the example binary tree
    solution = Solution()
    assert solution.maxDepth(example_binary_tree) == 4
