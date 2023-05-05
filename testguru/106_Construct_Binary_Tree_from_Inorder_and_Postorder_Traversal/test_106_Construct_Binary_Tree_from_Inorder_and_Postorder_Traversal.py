import pytest
from solution import TreeNode, Solution

def build_tree_helper(inorder, postorder):
    solution = Solution()
    return solution.buildTree(inorder, postorder)

def test_buildTree():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    root = build_tree_helper(inorder, postorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7

    inorder = [1,2,3]
    postorder = [3,2,1]
    root = build_tree_helper(inorder, postorder)
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3

    inorder = []
    postorder = []
    root = build_tree_helper(inorder, postorder)
    assert root == None