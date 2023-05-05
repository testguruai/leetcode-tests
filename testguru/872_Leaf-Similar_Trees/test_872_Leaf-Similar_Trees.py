import pytest

from solution import Solution
from solution import TreeNode


def test_leaf_similar():
    # create the first tree
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)

    # create the second tree
    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(2)
    root2.left.right.left = TreeNode(7)
    root2.left.right.right = TreeNode(4)
    root2.right.left = TreeNode(9)
    root2.right.right = TreeNode(8)

    assert Solution().leafSimilar(root1, root2) == True

    # create the third tree
    root3 = TreeNode(3)
    root3.left = TreeNode(5)
    root3.right = TreeNode(1)
    root3.left.left = TreeNode(6)
    root3.left.right = TreeNode(7)
    root3.right.left = TreeNode(4)
    root3.right.right = TreeNode(2)
    root3.right.right.left = TreeNode(9)
    root3.right.right.right = TreeNode(8)

    assert Solution().leafSimilar(root1, root3) == False

    # create the fourth tree
    root4 = TreeNode(3)
    root4.left = TreeNode(5)
    root4.right = TreeNode(1)
    root4.left.left = TreeNode(6)
    root4.left.right = TreeNode(2)
    root4.right.left = TreeNode(9)
    root4.right.right = TreeNode(8)

    assert Solution().leafSimilar(root1, root4) == False

    # create the fifth tree
    root5 = TreeNode(3)
    root5.left = TreeNode(5)
    root5.right = TreeNode(1)
    root5.left.left = TreeNode(6)
    root5.right.left = TreeNode(9)
    root5.right.right = TreeNode(8)

    assert Solution().leafSimilar(root1, root5) == False

    # create the sixth tree
    root6 = TreeNode(3)
    root6.left = TreeNode(5)
    root6.right = TreeNode(1)
    root6.left.left = TreeNode(6)
    root6.right.right = TreeNode(8)

    assert Solution().leafSimilar(root1, root6) == False

    # create the seventh tree
    root7 = TreeNode(1)

    assert Solution().leafSimilar(root7, None) == False

    # create the eighth tree
    root8 = TreeNode(1)

    assert Solution().leafSimilar(None, root8) == False

    # create the ninth tree
    root9 = TreeNode(1)

    assert Solution().leafSimilar(None, None) == True
