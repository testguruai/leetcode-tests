import pytest

from solution import TreeNode, Solution

def test_hasPathSum():
    # create test cases
    # Test case 1 : Empty Tree
    tree1 = None
    target1 = 1
    output1 = False
    
    # Test Case 2 : Root only binary tree
    tree2 = TreeNode(7)
    target2 = 7
    output2 = True
    
    # Test Case 3 : internal nodes binary tree
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    tree3 = TreeNode(5)
    tree3.left = TreeNode(4)
    tree3.right = TreeNode(8)
    tree3.left.left = TreeNode(11)
    tree3.left.left.left = TreeNode(7)
    tree3.left.left.right = TreeNode(2)
    tree3.right.left = TreeNode(13)
    tree3.right.right = TreeNode(4)
    tree3.right.right.right = TreeNode(1)
    target3 = 22
    output3 = True
    
    # invoke the code
    assert Solution().hasPathSum(tree1, target1) == output1
    assert Solution().hasPathSum(tree2, target2) == output2
    assert Solution().hasPathSum(tree3, target3) == output3

    # add more test cases based on the function requirements to make sure it handles all possible inputs and outputs.
